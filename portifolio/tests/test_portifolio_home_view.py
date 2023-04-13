from .test_portifolio_base import TestBase
from portifolio import views
from django.urls import reverse, resolve


class PortifolioHomeViewTest(TestBase):
    def test_portifolio_home_view_function_is_correct(self):
        self.make_profile(user_url='test-tester')
        view = resolve(reverse('portifolio:home', kwargs={'slug':'test-tester'}))  # noqa
        self.assertEqual(view.func, views.home)

    def test_portifolio_home_view_loads_the_correct_template(self):
        self.make_profile(user_url='test-tester')
        view = self.client.get('/test-tester')  # noqa
        self.assertTemplateUsed(view, 'index.html')

   
