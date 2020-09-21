import requests
from requests.auth import HTTPBasicAuth


def test_oauth():
    url = 'https://httpbin.testing-studio.com/basic-auth/banana/123'
    r = requests.get(url=url, auth=HTTPBasicAuth("banana", "123"))
    print(r)
