from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from accounts.views import connexion

class TestUrls(SimpleTestCase):
    def test_url(self):
        url = reverse('accounts:connexion')
        self.assertEquals(resolve(url).func, connexion)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("accounts:connexion")

    def test_login_GET(self):
        res=self.client.get(self.login_url)
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'accounts/login.html')