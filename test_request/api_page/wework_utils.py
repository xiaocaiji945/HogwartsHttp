from test_request.api_page.base_pai import BaseApi


class WeWorkUtils(BaseApi):
    def get_token(self, corpsecret, corpid="ww5b005eced8645715"):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        result = self.send_api(data)
        return result["access_token"]

    def get_hellorf_token(self):
        return "877af4d867b62e85e00b76fe11df95bbefcb8483"

