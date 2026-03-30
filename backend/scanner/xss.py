from config import XSS_PAYLOADS
from scanner.utils import send_get_request
import html

def detect_xss(base_url):
    for payload in XSS_PAYLOADS:
        test_url = f"{base_url}/rest/products/search?q={payload}"
        response = send_get_request(test_url)

        # Normalize response
        decoded_payload = html.escape(payload)

        if payload in response or decoded_payload in response:
            return {
                "vulnerable": True,
                "payload": payload,
                "fix": "Sanitize input and implement proper output encoding"
            }

    return {"vulnerable": False}