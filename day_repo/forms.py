from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

from day_repo.models import ImageUpload, ReportModel


# 作成・編集画面のフォーム
class ReportModelForm(forms.ModelForm):
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )

    class Meta:
        model = ReportModel
        # ユーザはログイン情報から紐づけて、スラッグは自動採番のため、入力フォーム画面から除外
        exclude = ["user", "slug"]

    def __init__(self, user=None, *args, **kwargs):
        # 項目名単位にループ
        for key, field in self.base_fields.items():
            # "release_flag"の場合、Bootstrapの別クラス「form-check-input」を適用してチェックボックス化する。
            if key == "release_flag":
                field.widget.attrs["class"] = "form-check-input"
            # それ以外の場合、Bootstrapの別クラス「form-control」を適用してテキストボックス化する。
            else:
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
