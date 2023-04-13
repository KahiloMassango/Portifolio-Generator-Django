from .test_accounts_base import TestBase


class TestAccountsModels(TestBase):
    def test_has_profile_CustomUser_is_false_by_default(self):
        user = self.make_user()
        self.assertFalse(user.has_profile)

    def test_CustomUser_str_returns_username(self):
        user = self.make_user(username="user")
        self.assertEqual(user.__str__(), user.username)

    def test_profile_str_returns_full_name(self):
        profile = self.make_profile(full_name="test tester")
        self.assertEqual(profile.__str__(), profile.full_name)

    def test_experience_str_returns_work(self):
        exp = self.make_experience()
        self.assertEqual(exp.__str__(), exp.work)

    def test_education_str_returns_title(self):
        edu = self.make_education()
        self.assertEqual(edu.__str__(), edu.title)
