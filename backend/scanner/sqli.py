import requests
from config import SQLI_PAYLOADS

def detect_sqli(base_url):
    url = f"{base_url}/rest/user/login"

    for payload in SQLI_PAYLOADS:
        data = {
            "email": payload,
            "password": payload
        }

        try:
            res = requests.post(url, json=data)
            response = res.text.lower()

            if "authentication failed" not in response:
                return {
                    "vulnerable": True,
                    "payload": payload,
                    "fix": "Use parameterized queries and ORM"
                }
        except:
            pass

    return {"vulnerable": False}