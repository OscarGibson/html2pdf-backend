from django.shortcuts import render, redirect
import requests
import urllib
from urllib.parse import urlencode
import json
from src.settings.local import FRONTEND_HOST, LOGIN_REGISTER_URLS

def email_verify(request, verify_id):
    post_data = {'key': verify_id}
    response = requests.post(EMAIL_VERIFY_URL, data=post_data)
    try:
        content = json.loads(response.text)
    except Exception as e:
        raise e

    if content['detail'] == 'ok':
        return redirect(LOGIN_REGISTER_URLS['emailVerify'])

    template = 'test_app/index.html'
    context = {}
    return render(request, template, context)
