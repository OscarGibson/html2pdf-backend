from django.conf.urls import url
from .views import FacebookLogin

urlpatterns = [
    url(r'^$', FacebookLogin.as_view(), name='fb_login')
]
