import requests
import json
import re
import string

def upload_json(json_object):
    json_object = {'file':json_object}
    newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://127.0.0.1:5001/api/v0/add', files=json_object)
    return response.json()['Hash']

def get_json(json_hash):
    response = requests.get("http://localhost:8080/ipfs/"+json_hash )
    return json.loads(response.text)

def get_url(hash):
    return "localhost:8080/ipfs/"+hash