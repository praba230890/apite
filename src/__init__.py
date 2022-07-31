import requests
import json
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def main():
    print("main")
    load_yaml('/Volumes/Data/playground/testAutomationFrameworks/apite/tests/example_test.yaml')

def load_yaml(file_name):
    with open(file_name, 'r') as f:
        test = yaml.load(f, Loader=Loader)
        print(test)
        run_test(test)

def get_api(test_data):
    host = test_data['service']['connection']['host']
    endpoint = host
    if test_data['service']['connection']['https'] == True:
        endpoint = 'https://' + endpoint
    else:
        endpoint = 'http://' + endpoint
    endpoint = endpoint+test_data.get('service').get('endpoints')[0].get('path')
    print("endpoint, ", endpoint)
    return endpoint

def get_assert_response(test_data):
    return json.loads(test_data.get('service').get('endpoints')[0].get('response'))

def run_test(test_data):
    endpoint = get_api(test_data)
    res = requests.get(endpoint)
    response = get_assert_response(test_data)
    print(response, " response")
    print(res.json(), " res.json")
    assert res.json() == response