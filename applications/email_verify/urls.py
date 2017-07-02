from django.conf.urls import url
from .views import email_verify

urlpatterns = [
    url(r'^(?P<verify_id>.+)/$', email_verify, name="email_verify")
]
