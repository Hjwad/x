import os
import requests

def configure_quota_guard():
    quota_guard_url = os.environ.get('QUOTAGUARDSHIELD_URL')

    session = requests.Session()
    session.proxies = {"http": quota_guard_url, "https": quota_guard_url}

    response = session.get(quota_guard_url)
    print(response.text)