import os
import socket

import redis
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
r = redis.StrictRedis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"], password=os.environ["REDIS_PASSWORD"], ssl=os.environ["REDIS_USE_SSL"].lower() == 'true')


@api.route('/hello')
class Hello(Resource):
    def get(self):
        return {'status': 'Flask application running properly!'}


@api.route('/redis')
class Redis(Resource):
    def get(self):
        r.incr('views')
        return {'count': f"This site has been visited {int(r.get('views'))}, the hostname is {socket.gethostname()}"}
