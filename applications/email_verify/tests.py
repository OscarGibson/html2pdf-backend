from django.test import TestCase

from django.core.mail.message import EmailMessage


class TestCase1(TestCase):

    def case1(self):
        email = EmailMessage(subject='Test case', body='<h1>Hello</h1>', from_email='html2pdf@mymail.com',
            to=['ostaphuba@gmail.com'], headers = {'Reply-To': 'support@coffeehouse.com'})
        a = email.send()
	assert a
