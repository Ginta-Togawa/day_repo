from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse_lazy


# 自作自動遷移用クラス
class MyDayRepoAdapter(DefaultAccountAdapter):

    # ログイン後自動遷移メソッド
    def get_login_redirect_url(self, request):
        # 遷移先URL
        resolved_url = super().get_login_redirect_url(request)

        # ユーザ名が未入力(初回ログイン時)の場合、プロファイル更新画面に遷移
        if not request.user.profile.username:
            resolved_url = reverse_lazy("profile-update", kwargs={"pk": request.user.profile.pk})

        return resolved_url
