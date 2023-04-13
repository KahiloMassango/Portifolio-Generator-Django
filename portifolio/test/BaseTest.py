from django.test import TestCase
from accounts.models import CustomUser, Profile


class TestBase(TestCase):
    def make_user(self,
                  username="test",
                  email="test@test.com",
                  password="Password1@"):

        return CustomUser.objects.create(
                                username=username,
                                email=email,
                                password=password)

    def make_profile(self,
                     full_name="test tester",
                     user_url="test-tester",
                     country="AO",
                     stack="BackEnd Developer"
                     ):

        return Profile.objects.create(
            user=self.make_user(),
            full_name=full_name,
            user_url=user_url,
            stack=stack
        )
