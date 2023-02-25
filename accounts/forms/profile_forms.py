from django import forms

from accounts.models import Profile


# プロファイル更新用フォーム
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

    # バリデーションチェック(ユーザ名)
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user_email = self.instance.user.email
        # ユーザ名に自身のメールアドレスが指定されたとき
        if username == user_email:
            raise forms.ValidationError("ユーザー名を変更してください")
        # ユーザ名に@が有力されているとき
        elif "@" in username:
            raise forms.ValidationError("ユーザー名にEメールアドレスは使用できません")
        return username
