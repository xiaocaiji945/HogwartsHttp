import base64
import json

import requests


class ApiRequests:

    def deconde_send(self, data: dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        elif data["encoding"] == "private":
            return requests.post("url", data=res.content)
