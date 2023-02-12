from django import forms

from day_repo.models import ImageUpload, ReportModel


# 作成・編集画面のフォーム
class ReportModelForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        # ユーザはログイン情報から紐づけ
        exclude = ["user"]

    def __init__(self, user=None, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
            # 引数からユーザを設定
            self.user = user
        super().__init__(*args, **kwargs)

    # 登録処理
    def save(self, commit=True):
        report_obj = super().save(commit=False)
        # 日報へのユーザの紐づけ
        if self.user:
            report_obj.user = self.user
        if commit:
            # 登録
            report_obj.save()
        return report_obj


# 画像アップロード用フォーム
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"
