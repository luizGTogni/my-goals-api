class HttpRequest:
    def __init__(
            self,
            body: dict = None,
            params: dict = None,
            query: dict = None,
            headers: dict = None,
            token_info: dict = None,
        ) -> None:
        self.body = body
        self.params = params
        self.query = query
        self.headers = headers
        self.token_info = token_info
