from django import forms


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
