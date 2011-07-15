# taken from Splinter source code

from flask import Flask
from flask import request
from multiprocessing import Process
from urllib import urlopen

EXAMPLE_APP = "http://localhost:5000/"

EXAMPLE_HTML = """\
<html>
  <head>
    <title>Example Title</title>
  </head>
  <body>
    <h1 id="firstheader" name="header">Example Header</h1>
  </body>
</html>"""

app = Flask(__name__)

@app.route('/')
def index():
    return EXAMPLE_HTML

class Env(object):
    pass

env = Env()
env.process = None
env.host, env.port = 'localhost', 5000
env.browser = None

def start_flask_app(host, port):
    """Runs the server."""
    app.run(host=host, port=port)
    app.config['DEBUG'] = False
    app.config['TESTING'] = False

def wait_until_start():
    while True:
        try:
            urlopen(EXAMPLE_APP)
            break
        except IOError:
            pass

def wait_until_stop():
    while True:
        try:
            results = urlopen(EXAMPLE_APP)
            if results.code == 404:
                break
        except IOError:
            break

def start_server():
    env.process = Process(target=start_flask_app, args=(env.host, env.port))
    env.process.daemon = True
    env.process.start()
    wait_until_start()

def stop_server():
    env.process.terminate()
    wait_until_stop()

