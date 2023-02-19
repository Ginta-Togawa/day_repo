from django import template

register = template.Library()


@register.filter
def user_display(user):
    user_display = "ゲスト"
    if user.is_authenticated:
        if not user.profile.username:
            user_display = "ユーザ名が設定されていません"
        else:
            user_display = user.profile.username
    return user_display
