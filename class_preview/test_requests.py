import base64
import json

import requests


def test_encode():
    url = 'http://127.0.0.1:9999/demo.txt'
    r = requests.get(url=url)
    print(r.content)
    res = json.loads(base64.b64decode(r.content))
    print(res)
