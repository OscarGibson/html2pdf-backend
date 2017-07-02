# html2pdf-backend
backend on django for 'html2pdf' app

### Problems
This project is on alpha-testing phase, so it's not ready to production.
Email verify not working

## Get started
### Requirements:
1. Python 3.x
2. pip
3. virtualenv (on Linux)

To run project on you local machine (Linux):
```
virtualenv <your-virtual-env-name> -p python3
source <your-virtual-env-name>/bin/activate
```
After you need to install all django pakedges:
```
pip install -r requirements/requirements.txt
```
Create local.py in src/settings/ with options (here is default values, you can customize all):
```
from src.settings.common import *

SECRET_KEY = # create your secret key
DEBUG = 
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
#Django registration
ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
REST_SESSION_LOGIN = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Host for sending e-mail.
EMAIL_HOST = 'smtp.<mail-host>.com'
# Port for sending e-mail.
EMAIL_PORT = 2525
# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = <your-email>
EMAIL_HOST_PASSWORD = <your-pass>
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL =
SERVER_EMAIL = 
EMAIL_SEND_TO = 

BACKEND_HOST = 'http://127.0.0.1:8000'
FRONTEND_HOST = 'http://127.0.0.1:4200'
CORS_ORIGIN_WHITELIST = (
    FRONTEND_HOST, 
)

LOGIN_REGISTER_URLS = {
    'loginByToken' : '%s/rest-auth/user/' % BACKEND_HOST,
    'emailVerify' : '%s/rest-auth/registration/verify-email/' % BACKEND_HOST
}
```
Then run server on locahost:8000
```
python manage.py runserver
```
