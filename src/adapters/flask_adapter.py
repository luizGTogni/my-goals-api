from flask import request, jsonify
from src.views.interfaces.view import IView
from src.types.http import HttpRequest

class FlaskAdapter:
    def __init__(self, view: IView) -> None:
        self.__view = view

    def route_handler(self, params: dict = None):
        http_request = HttpRequest(
            body=request.json,
            params=params,
            query=request.args,
            headers=request.headers,
        )
        http_response = self.__view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
