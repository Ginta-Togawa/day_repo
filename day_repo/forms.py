from django import forms

from day_repo.models import ImageUpload, ReportModel


# 作成・編集画面のフォーム
class ReportModelForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)


# 画像アップロード用フォーム
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"
