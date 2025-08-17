from flask import request, jsonify
from src.views.interfaces.view import IView
from src.types.http import HttpRequest

class FlaskAdapter:
    def __init__(self, view: IView) -> None:
        self.__view = view

    def route_handler(self, params: dict = None, token_info: dict = None):
        body = None
        if request.is_json:
            body = request.json

        http_request = HttpRequest(
            body=body,
            params=params,
            query=request.args.to_dict(),
            headers=request.headers,
            token_info=token_info,
        )
        http_response = self.__view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
