import requests
from jsonpath import jsonpath
from requests_xml import XMLSession
from hamcrest import *


class TestAssert:
    def test_hamcrest(self):
        url = 'https://ceshiren.com/categories.json'
        r = requests.get(url)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to("社区治理"))
        assert_that(jsonpath(r.json(), '$..name')[0], equal_to('社区治理'))


    def test_xml_assert(self):
        url = 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss'
        session = XMLSession()
        r = session.get(url)
        r.xml.links
        item = r.xml.xpath('//item', first=True)
        print(item.text)

    def test_hogwarts_jsonpath(self):
        url = 'https://ceshiren.com/categories.json'
        r = requests.get(url)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "社区治理"
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == "社区治理"

    def test_hogwarts(self):
        url = 'https://ceshiren.com/categories.json'
        r = requests.get(url)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "社区治理"
