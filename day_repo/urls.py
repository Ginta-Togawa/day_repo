from django.urls import path

from day_repo.views import *

# URLパターン(day_repo配下)
urlpatterns = [
    # 一覧表示
    path("", ReportModeListView.as_view(), name="day_repo_list"),
    # 詳細表示(パラメータにPK)
    path("detail/<int:pk>/", ReportModelDetailView.as_view(), name="day_repo_detail"),
    # 日報作成
    path("create/", ReportModelFormCreateView.as_view(), name="day_repo_create"),
    # 日報編集
    path("edit/<int:pk>/", ReportModelFormUpdateView.as_view(), name="day_repo_edit"),
    # 日報削除
    path("delete/execute/<int:id>/", day_repo_delete_execute_view, name="day_repo_delete_execute"),
    # 画像アップロード画面
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
]
