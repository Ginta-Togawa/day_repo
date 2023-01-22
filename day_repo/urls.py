from django.urls import path

from day_repo.views import day_repo_list_view

# URLパターン(day_repo配下)
urlpatterns = [
    # 指定なし(day_repo/)
    path("", day_repo_list_view),
]
