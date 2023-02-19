from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms.fields import DateField

from .models import User, Profile, GENDER_CHOICE


# 管理者ユーザ用フォームクラス
class CustomAdminChangeForm(UserChangeForm):
    # ユーザ名
    username = forms.CharField(max_length=100)
    # 部署名
    department = forms.CharField(max_length=100, required=False)
    # 電話番号
    phone_number = forms.IntegerField(required=False)
    # 性別(リストはmodels.pyにて定義)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, required=False)
    # 生年月日
    birthday = DateField(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    # Profileが存在する場合は、初期値にデータを格納する
    def __init__(self, *args, **kwargs):
        user_obj = kwargs["instance"]
        if hasattr(user_obj, "profile"):
            profile_obj = user_obj.profile
            self.base_fields["username"].initial = profile_obj.username
            self.base_fields["department"].initial = profile_obj.department
            self.base_fields["phone_number"].initial = profile_obj.phone_number
            self.base_fields["gender"].initial = profile_obj.gender
            self.base_fields["birthday"].initial = profile_obj.birthday
        super().__init__(*args, **kwargs)

    # 保存機能の定義
    def save(self, commit=True):
        user_obj = super().save(commit=False)
        username = self.cleaned_data.get("username")
        department = self.cleaned_data.get("department")
        phone_number = self.cleaned_data.get("phone_number")
        gender = self.cleaned_data.get("gender")
        birthday = self.cleaned_data.get("birthday")
        if hasattr(user_obj, "profile"):
            profile_obj = user_obj.profile
        else:
            profile_obj = Profile(user=user_obj)
        if username is not None:
            profile_obj.username = username
        if department is not None:
            profile_obj.department = department
        if phone_number is not None:
            profile_obj.phone_number = phone_number
        if gender is not None:
            profile_obj.gender = gender
        if birthday is not None:
            profile_obj.birthday = birthday
        profile_obj.save()
        if commit:
            user_obj.save()
        return user_obj


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
