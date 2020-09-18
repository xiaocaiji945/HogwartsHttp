import requests


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header demo"})
        # print(r.status_code)
        print(r.text)
        # print(r.json())
        # print(f"\n{r.headers}")
        print(r.cookies)
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1