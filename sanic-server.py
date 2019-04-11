from sanic import Sanic
from sanic.response import json

from rq import Queue
from worker import conn

from jobs.utils import count_words_at_url


q = Queue(connection=conn)

app = Sanic()


@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/start-instabot')
async def start_instabot(request):

    job = q.enqueue(count_words_at_url, 'http://nvie.com')

    return json({'status': 'Job Submitted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
