import requests
import json

def test_logintoken():
    host = "http://10.0.7.25/stage-api/auth/"
    url = host + "login"
    data = {
        "username": "LE02054",
        "password": "123456"
    }
    header = {
        "Content-Type": "application/json",
    }
    rev_data = requests.post(headers=header, url=url, data=json.dumps(data))
    print(json.loads(rev_data.content).get("data").get("access_token"))


if __name__ == '__main__':
    test_logintoken()