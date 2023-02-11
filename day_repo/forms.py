from django import forms

from day_repo.models import ImageUpload


# 登録画面のフォーム
class ReportForm(forms.Form):
    # タイトル
    title = forms.CharField(label="タイトル")
    # 内容
    content = forms.CharField(label="内容", widget=forms.Textarea())

    # 入力画面の設定
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class": "form-control"})
        super().__init__(*args, **kwargs)


# 画像アップロード用フォーム
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"
