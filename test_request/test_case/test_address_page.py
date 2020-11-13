import requests
from jsonpath import jsonpath

from test_request.api_page.address_page import AddressPage
from test_request.api_page.wework_utils import WeWorkUtils


class TestAddressPage():

    def setup(self):
        self.address = AddressPage()
        # assert jsonpath(result.json(), "$.errmsg")[0] == 'deleted'

    def test_get_member_info(self):
        member_message = self.address.get_member_info()
        assert member_message["errcode"] in [60111, 0]

    def test_add_member(self):
        member_message = self.address.add_member()
        print(member_message)
        assert member_message["errcode"] in [0, 60104]
        assert member_message["errmsg"] == "created"

    def test_update_member(self):
        member_message = self.address.update_member()
        assert member_message["errcode"] in [0, 60111]
        assert member_message["errmsg"] == "updated"

    def test_delete_member(self):
        member_message = self.address.delete_member()
        assert member_message["errcode"] in [0, 60111]
        assert member_message["errmsg"] == "deleted"

    def test_session(self):
        s = requests.session()
        _corpsecret = "UZu4N8ruskIwKmofJI0s9P4AaLel6srpSNXSYJEHjGY"
        s.params = {"access_token": WeWorkUtils().get_token(_corpsecret)}
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"userid": "labixiaoxin"}
        }
        print(s.request(**data).json())