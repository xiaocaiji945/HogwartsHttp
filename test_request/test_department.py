from jsonpath import jsonpath
import requests


class TestMenber:
    _de_name = "霍格沃兹研发中心"
    _de_name_en = "Hogwarts"
    _de_id = 999

    def get_url(self, func):
        return f"https://qyapi.weixin.qq.com/cgi-bin/department/{func}?access_token={self.get_token()}"

    def get_token(self):
        corpid = "ww5b005eced8645715"
        corpsecret = "UZu4N8ruskIwKmofJI0s9B5Gr_HQsUxrmQkWC7CpdAE"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        token = requests.get(url).json()["access_token"]
        return token

    def test_add(self):
        data = {
            "name": f"{self._de_name}",
            "name_en": f"{self._de_name_en}",
            "parentid": 1,
            "order": 1,
            "id": self._de_id
        }
        result = requests.post(self.get_url("create"), json=data)
        print(result.json())
        assert jsonpath(result.json(), "$.errmsg")[0] == 'created'

    def test_get(self):
        result = requests.get(self.get_url("list"), params={"id": self._de_id})
        print(result.json())
        print(result.url)
        assert jsonpath(result.json(), "$.errmsg")[0] == 'ok'

    def test_update(self):
        data = {
            "id": self._de_id,
            "name": f"{self._de_name}—编辑",
        }
        result = requests.post(self.get_url("update"), json=data)
        print(result.json())
        assert jsonpath(result.json(), "$.errmsg")[0] == 'updated'

    def test_delete(self):
        result = requests.get(self.get_url("delete"), params={"id": self._de_id})
        print(result.json())
        assert jsonpath(result.json(), "$.errmsg")[0] == 'deleted'
