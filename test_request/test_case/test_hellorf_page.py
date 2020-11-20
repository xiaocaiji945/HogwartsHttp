import requests

from test_request.api_page.hellorf_page import HellorfPage


class TestHellorfPage:

    def setup_class(self):
        self.hell = HellorfPage()
        self.hell.set_cookie({"access-token": "40adc929313ca1f9457c287e8f9b154861a3928b"})


    def test_keywords(self):
        print(self.hell.keywords())


    def test_demo(self):
        s = requests.Session()
        to = "877af4d867b62e85e00b76fe11df95bbefcb8483"
        # s.cookies = {"access_token": "dc327f3b9cb781b68969224abbde8dfca4f41f47"}
        s.headers= {"access-token":"40adc929313ca1f9457c287e8f9b154861a3928b"}
        r = s.get(url="https://api.hellorf.com/hellorf/user/latest-keywords",
                          params={"platform":"image"})
        # r = requests.get(url="https://api.hellorf.com/hellorf/user/latest-keywords",
        #                 params={"platform":"image"}, headers={"access_token":"e699c95d404ea0d955250554342f85c33ed31d3d"})
        print(r.headers)
        print(r.json())
