from sanic import Sanic
from sanic.response import json, text
import os

from rq import Queue
from worker import conn

from jobs.instabot import start_smart_run
from jobs.instabot_api import run_the_bot
from jobs.hashtags import generate_hashtags


q = Queue(connection=conn, default_timeout=-1)

app = Sanic()

@app.route('/_healthz')
async def test(request):
    return json({'status': 'ok'})

@app.route('/hashtags')
async def test(request):
    arguments = request.args
    version = ""
    if arguments.get('version') != None:
        version = arguments['version'][0]
    hashtag_set = generate_hashtags(version)
    return text(hashtag_set)

@app.route('/start-instabot')
async def start_instabot(request):
    arguments = request.args
    arguments_valid = True
    for attr in ['username', 'passkey', 'hashtags', 'influencers']:
        if not (attr in arguments.keys()):
            arguments_valid = False
            break

    if arguments_valid:
        job = q.enqueue(start_smart_run, arguments)
        message = json({'message': 'Job Submitted', 'job_id': job.id})
    else:
        message = json({'error': 'Invalid Arguments'})

    return message

@app.route('/start-instabot-api')
async def start_instabot(request):
    arguments = request.args
    arguments_valid = True
    for attr in ['username', 'passkey', 'hashtags', 'target_nickname']:
        if not (attr in arguments.keys()):
            arguments_valid = False
            break

    if arguments_valid:
        job = q.enqueue(run_the_bot, arguments)
        message = json({'message': 'Job Submitted', 'job_id': job.id})
    else:
        message = json({'error': 'Invalid Arguments'})

    return message

if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port)
