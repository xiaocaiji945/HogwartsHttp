import requests
import yaml

'''
需要二次封装requests，对请求进行定制化。
将请求的结构体的url从一个写死的ip地址改为一个（任意的）域名。
使用一个env配置文件，存放各个环境的配置信息。
然后将请求结构体中的url替换为`env`配置文件中个人选择的url。
将env配置文件使用yaml进行管理。
'''


class Api:
    env = yaml.safe_load(open("env.yaml"))

    # data 是一个请求信息
    def send(self, data: dict):
        # 替换
        data["url"] = str(data["url"]).replace("testing-studio", self.env["testing-studio"][self.env["default"]])

        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r
