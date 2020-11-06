import requests
import json

def upload_json(json_object):
    json_object = {'file':json_object}
    newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://127.0.0.1:5001/api/v0/add', files=json_object)
    print(response.json())

def get_json(json_hash):
    params = (('arg', json_hash),)
    response = requests.post('http://127.0.0.1:5001/api/v0/block/get?arg='+json_hash)
    txt = response.text.strip()
    return txt[5:-1]

def get_url(hash):
    return "localhost:8080/ipfs/"+hash