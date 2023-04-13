from BaseTest import TestBase
from django.urls import reverse


class PortifolioURLsTest(TestBase):
    def test_portifolio_home_url_is_correct(self):
        self.make_profile()
        url = reverse('portifolio:home', kwargs={'slug':'test-tester'})  # noqa
        self.assertEqual(url, '/test-tester')

    def test_portifolio_home_status_code_is_200(self):
        self.make_profile()
        response = self.client.get(reverse('portifolio:home', kwargs={'slug':'test-tester'}))  # noqa
        self.assertEqual(response.status_code, 200)

    def test_portifolio_status_code_404_if_no_profile_matched_url(self):
        response = self.client.get(reverse('portifolio:home', kwargs={'slug':'no-profile'}))  # noqa
        self.assertEqual(response.status_code, 404)
