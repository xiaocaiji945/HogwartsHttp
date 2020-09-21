import json
import requests
from jsonschema import validate


class TestSchema:

    def test_json_schema(self):
        url = 'http://testerhome.com/api/v3/topics.json'
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_schema(self):
        url = 'https://ceshiren.com/categories.json'
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        print(data)
        # validate(data, schema=schema)
