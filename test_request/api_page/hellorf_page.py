from test_request.api_page.base_pai import BaseApi


class HellorfPage(BaseApi):
    def keywords(self):
        data = {
            "method": "get",
            "url": "https://api.hellorf.com/hellorf/user/latest-keywords",
            "params" : {"platform": "image"}
        }
        result = self.send_cookie_api(data)
        return result
