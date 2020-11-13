from test_request.api_page.base_pai import BaseApi


class WeWorkUtils(BaseApi):
    def get_token(self, corpsecret, corpid="ww5b005eced8645715"):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        result = self.send_api(data)
        return result["access_token"]
