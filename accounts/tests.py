from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

User = get_user_model()
signup_url = reverse("account_signup")
login_url = reverse("account_login")


# test関数2つ
class AdapterTestCase(TestCase):
    # signupページでユーザーを作成し、Eメール確認も済にする
    def setUp(self):
        self.request = RequestFactory()
        self.email = "test@itc.tokyo"
        self.password = "somepass"
        self.res = self.client.post(signup_url, {"email": self.email,
                                                 "password1": self.password,
                                                 "password2": self.password})
        self.user_obj = User.objects.first()
        self.email_obj = self.user_obj.emailaddress_set.first()
        self.email_obj.verified = True
        self.email_obj.save()
        self.user_obj.profile.username = "something_changed"

    # プロフィールが変わったユーザーのテスト
    def test_login_with_profile_user(self):
        from accounts.adapter import MyDayRepoAdapter as adapter
        adapter_obj = adapter(self.user_obj)
        self.request.user = self.user_obj
        redirect_url = adapter_obj.get_login_redirect_url(self.request)
        self.assertEqual(redirect_url, reverse("day_repo_list"))

    # プロフィールが同一のユーザーのテスト
    def test_login_without_profile(self):
        res = self.client.post(signup_url, {"email": "test2@itc.tokyo",
                                            "password1": self.password,
                                            "password2": self.password})
        user2 = User.objects.last()
        email_obj2 = user2.emailaddress_set.first()
        email_obj2.verified = True
        email_obj2.save()
        from accounts.adapter import MyDayRepoAdapter as adapter
        adapter_obj = adapter(user2)
        self.request.user = user2
        redirect_url = adapter_obj.get_login_redirect_url(self.request)
        self.assertEqual(redirect_url, reverse("profile-update", kwargs={"pk": user2.profile.pk}))
