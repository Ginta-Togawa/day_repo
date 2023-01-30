from django import forms

from day_repo.models import ImageUpload


# 登録画面のフォーム
class ReportForm(forms.Form):
    title = forms.CharField(
        label="タイトル",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'タイトル...',
            }
        ),
    )
    content = forms.CharField(
        label="内容",
        widget=forms.Textarea(
            attrs={
                'placeholder': '内容...',
            }
        ),
    )


# 画像アップロード用フォーム
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"
