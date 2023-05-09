import request
from ru import yaml
import json

def test_logintoken():
    host = "http://10.0.7.25/stage-api/auth/"
    url = host + "login"
    data = {
        'usename': "LE02054",
        "password": "123456"
    }
    