from flask import Flask, jsonify
from flask_restx import Resource, Api
import asyncio

from api import Proxies

app = Flask(__name__)
api = Api(app, doc=False)
pr = Proxies()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@api.route('/v1/random')
class Random(Resource):
    def get(self):
        proxy_list = asyncio.run(pr.getRandomProxies())

        return jsonify(proxy_list)


@api.route('/v1/http')
class Random(Resource):
    def get(self):
        proxy_list = asyncio.run(pr.getHttpProxies())

        return jsonify(proxy_list)


@api.route('/v1/socks')
class Random(Resource):
    def get(self):
        proxy_list = asyncio.run(pr.getSocksProxies())

        return jsonify(proxy_list)


if __name__ == '__main__':
    app.run()
