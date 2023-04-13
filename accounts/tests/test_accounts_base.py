from django.test import TestCase
from accounts.models import CustomUser, Profile, Experience, Education


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
                     user=None,
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

    def make_experience(self,
                        profile=None,
                        company="test company",
                        start=2010,
                        end=2019,
                        work="tester"
                        ):
        return Experience.objects.create(
            profile=self.make_profile(),
            company=company,
            start=start,
            end=end,
            work=work
        )
    
    def make_education(self,
                       profile=None,
                       school="test school",
                       start=2010,
                       end=2019,
                       title="tester"
                       ):
        return Education.objects.create(
            profile=self.make_profile(),
            school=school,
            start=start,
            end=end,
            title=title
        )
