from django.test import TestCase
from accounts import views
from django.urls import reverse, resolve


class AccountsHomeViewTest(TestCase):
    def test_accounts_login_view_function_is_correct(self):
        view = resolve(reverse('accounts:login'))
        self.assertEqual(view.func, views.custom_login)

    def test_accounts_login_view_loads_the_correct_template(self):
        view = self.client.get('/accounts/login')
        self.assertTemplateUsed(view, 'login.html')

   
