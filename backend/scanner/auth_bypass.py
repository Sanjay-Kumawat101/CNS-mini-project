import requests
from config import AUTH_BYPASS_PAYLOADS

def detect_auth_bypass(base_url):
    url = f"{base_url}/rest/user/login"

    for creds in AUTH_BYPASS_PAYLOADS:
        try:
            res = requests.post(url, json={
                "email": creds["username"],
                "password": creds["password"]
            })

            response = res.text.lower()

            if "authentication failed" not in response:
                return {
                    "vulnerable": True,
                    "payload": creds,
                    "fix": "Implement proper authentication and validation"
                }
        except:
            pass

    return {"vulnerable": False}