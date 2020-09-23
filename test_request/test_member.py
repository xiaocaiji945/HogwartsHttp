from jsonpath import jsonpath
import requests


class TestMenber:
    _userid = "labixiaoxin"

    def get_url(self, func):
        return f"https://qyapi.weixin.qq.com/cgi-bin/user/{func}?access_token={self.get_token()}"

    def get_token(self):
        corpid = "ww5b005eced8645715"
        corpsecret = "UZu4N8ruskIwKmofJI0s9B5Gr_HQsUxrmQkWC7CpdAE"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        token = requests.get(url).json()["access_token"]
        return token

    def test_add(self):
        data = {
            "userid": f"{self._userid}",
            "name": "张三",
            "mobile": "13800000001",
            "department": [1]
        }
        result = requests.post(self.get_url("create"), json=data)
        print(result.json())
        assert jsonpath(result.json(), "$.errmsg")[0] == 'created'

    def test_get(self):
        result = requests.get(self.get_url("get"), params={"userid": f"{self._userid}"})
        print(result.json())
        print(result.url)
        assert jsonpath(result.json(), "$.errmsg")[0] == 'ok'

    def test_update(self):
        data = {
            "userid": f"{self._userid}",
            "name": "李四",
        }
        result = requests.post(self.get_url("update"), json=data)
        print(result.json())
        assert jsonpath(result.json(), "$.errmsg")[0] == 'updated'

    def test_delete(self):
        result = requests.get(self.get_url("delete"), params={"userid": f"{self._userid}"})
        print(result.json())
        assert jsonpath(result.json(), "$.errmsg")[0] == 'deleted'
