from test_request.api_page.base_pai import BaseApi
from test_request.api_page.wework_utils import WeWorkUtils


class AddressPage(BaseApi):
    '''
    通讯录管理，包括增删改查
    '''

    def __init__(self):
        self._userid = "labixiaoxin"
        _corpsecret = "UZu4N8ruskIwKmofJI0s9P4AaLel6srpSNXSYJEHjGY"
        utils = WeWorkUtils()
        self.token = utils.get_token(_corpsecret)

    def _get_url(self, func):
        return f"https://qyapi.weixin.qq.com/cgi-bin/user/{func}?access_token={self.token}"

    def get_member_info(self):
        data = {
            "method": "get",
            "url": self._get_url("get"),
            "params": {"userid": self._userid}
        }
        result = self.send_api(data)
        return result

    def add_member(self):
        data = {
            "method": "post",
            "url": self._get_url("create"),
            "json": {"userid": f"{self._userid}",
                     "name": "张三",
                     "mobile": "13800000001",
                     "department": [1]}
        }
        result = self.send_api(data)
        return result

    def update_member(self):
        data = {
            "method": "post",
            "url": self._get_url("update"),
            "json": {"userid": f"{self._userid}",
                     "name": "李四"}
        }
        result = self.send_api(data)
        return result

    def delete_member(self):
        data = {
            "method": "get",
            "url": self._get_url("delete"),
            "params": {"userid": self._userid}
        }
        result = self.send_api(data)
        return result
        # assert jsonpath(result.json(), "$.errmsg")[0] == 'deleted'
