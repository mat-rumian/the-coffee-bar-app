import logging as log
import requests
from flask import Flask, Response, request, make_response

from src.utils.utils import to_json


class EndpointAction:

    def __init__(self, action):
        self.action = action
        self.response = Response(mimetype='application/json')

    def __call__(self, *args, **kwargs):
        data = to_json(request.json)
        result = self.action(data)

        if isinstance(result, dict):
            self.response.status_code = 200
            self.response.set_data(str(result))
        elif isinstance(result, requests.models.Response):
            self.response.status_code = result.status_code
            self.response.set_data(str(result.text))
        elif isinstance(result, ValueError):
            self.response.status_code = 500
            self.response.set_data(str(result))

        return self.response


class HttpServer:
    app = None

    def __init__(self, name: str, host: str, port: int):
        self.app = Flask(name)
        self.host = host
        self.port = port

    def run(self):
        self.app.run(host=self.host, port=self.port, debug=True)

    def add_endpoint(self, endpoint: str = None, endpoint_name: str = None, handler: staticmethod = None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler), methods=['POST', 'GET', 'HEAD'])
