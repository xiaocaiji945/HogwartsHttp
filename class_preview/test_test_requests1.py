from class_preview import test_requests1


class TestApiRequests:
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }

    def test_deconde_send(self):
        ar = test_requests1.ApiRequests()
        print(ar.deconde_send(self.req_data))
