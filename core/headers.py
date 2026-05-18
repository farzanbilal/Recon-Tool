SECURITY_HEADERS = [
    "content-security-policy",
    "strict-transport-security",
    "x-frame-options",
    "x-content-type-options",
    "referrer-policy"
]


def analyze_headers(headers):
    results = {}

    for header in SECURITY_HEADERS:
        results[header] = header in headers

    return results