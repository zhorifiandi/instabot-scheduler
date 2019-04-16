from sanic import Sanic
from sanic.response import json, text
import os

from rq import Queue
from worker import conn

from jobs.instabot import start_smart_run


q = Queue(connection=conn, default_timeout=-1)

app = Sanic()

@app.route('/_healthz')
async def test(request):
    return json({'status': 'ok'})

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

if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port)
