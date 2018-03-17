import os
import json
from sanic import Sanic
# from sanic.response import json_response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SANIC_HOST = os.environ.get('SANIC_HOST', '127.0.0.1')
SANIC_PORT = os.environ.get('SANIC_PORT', 8000)
SANIC_DEBUG = os.environ.get('SANIC_DEBUG', False)

CONNECTIONS = set()

app = Sanic()

# Serving static files
app.static('/static', os.path.join(BASE_DIR, 'static/'))

# Serving index page
app.static('/', os.path.join(BASE_DIR, 'templates/index.html'), name='index')


@app.websocket('/chat')
async def chat(request, ws):
    nickname = request.args.get('nickname')
    if not nickname:
        return await ws.send(json.dumps({'error': 'nickname is required'}))

    for user in CONNECTIONS:
        if user.nickname == nickname:
            return await ws.send(json.dumps({'error': 'nickname already in use'}))

    ws.nickname = nickname
    CONNECTIONS.add(ws)
    print("{} has been connected!".format(nickname))

    try:
        while True:
            msg = await ws.recv()
            msg = json.dumps({"nickname": nickname, "message": msg})
            for user in CONNECTIONS:
                await user.send(msg)
    finally:
        CONNECTIONS.remove(ws)
        print("{} has been disconnected!".format(nickname))

if __name__ == '__main__':
    app.run(host=SANIC_HOST, port=SANIC_PORT, debug=SANIC_DEBUG)
