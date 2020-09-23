import requests


def test_demo():
    url = 'https://httpbin.testing-studio.com/cookies'
    header = {
        'User-Agent': "hogwarts"
    }
    cookie_data = {
        "hogwarts": "school",
        "teacher": "lyd"
    }
    # cookie_data = dict(cookie_are='working2')
    r = requests.get(url=url, headers=header, cookies=cookie_data)
    print(r.request.headers)
