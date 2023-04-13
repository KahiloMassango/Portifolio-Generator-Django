from django.test import TestCase
from django.urls import reverse


class AccountsURLsTest(TestCase):

    # login
    def test_accounts_login_url_is_correct(self):
        url = reverse('accounts:login')  # noqa
        self.assertEqual(url, '/accounts/login')

    def test_accounts_login_status_code_is_200(self):
        response = self.client.get(reverse('accounts:login'))  # noqa
        self.assertEqual(response.status_code, 200)

    # Register
    def test_accounts_register_url_is_correct(self):
        url = reverse('accounts:register')  # noqa
        self.assertEqual(url, '/accounts/register')

    def test_accounts_register_status_code_is_200(self):
        response = self.client.get(reverse('accounts:register'))  # noqa
        self.assertEqual(response.status_code, 200)
