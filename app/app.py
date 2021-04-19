import socket

import redis
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)


@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'status': 'Flask application running properly!'}


@api.route('/redis')
class Redis(Resource):
    def get(self):
        r.incr('views')
        return {'count': f"This site has been visited {int(r.get('views'))}, the hostname is {socket.gethostname()}"}
