from class_preview.env import env_demo


class TestApi:
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo.txt",
        "headers": None
    }

    def test_send(self):
        api = env_demo.Api()
        rs = api.send(self.data)
        print(rs.content)