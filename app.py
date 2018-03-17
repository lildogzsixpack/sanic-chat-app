import os
from sanic import Sanic
from sanic.response import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SANIC_HOST = os.environ.get('SANIC_HOST', '127.0.0.1')
SANIC_PORT = os.environ.get('SANIC_PORT', 8000)
SANIC_DEBUG = os.environ.get('SANIC_DEBUG', False)

app = Sanic()
# Serving static files
app.static('/static', os.path.join(BASE_DIR, 'static/'))
# Serving index page
app.static('/', os.path.join(BASE_DIR, 'templates/index.html'), name='index')

@app.route('/chat')
async def chat(request):
    return json({'Hello2': 'World2'})

if __name__ == '__main__':
    app.run(host=SANIC_HOST, port=SANIC_PORT, debug=SANIC_DEBUG)
