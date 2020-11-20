import json
import requests


class BaseApi:
    _s = requests.Session()
    '''
    api的抽象类
    '''

    def send_api(self, data: dict):
        '''
        发送api
        '''
        print(json.dumps(data, indent=2))
        return requests.request(**data).json()

    def send_cookie_api(self, data: dict):
        print(json.dumps(data, indent=2))

        re = self._s.request(**data)
        print(re.json())
        print(re.headers)
        return re.json()

    def set_cookie(self, data):
        self._s.headers = data
        return self

