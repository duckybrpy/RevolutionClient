from .utils.constants import host, port
import requests

class RevolutionRequest:
    def __init__(self, token = None):
        self.token = token
        self.req = requests
        pass

    def request(self, method, endpoint, body = None, web: bool = False):
        url = f"http://{host}:{port}/"
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}/"
        if web:
            endpoint = f"/api/{endpoint}/"

        if body:
            if method.upper() == "POST":
                return self.req.post(f"{url}{endpoint}", json=body).text
            else:
                return self.req.get(f"{url}{endpoint}", json=body).text

        else:
            if method.upper() == "POST":
                return self.req.post(f"{url}{endpoint}").text
            else:
                return self.req.get(f"{url}{endpoint}").text
