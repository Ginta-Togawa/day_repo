from django.urls import path

from day_repo.views import *

# URLパターン(day_repo配下)
urlpatterns = [
    # 一覧表示
    path("", ReportModeListView.as_view(), name="day_repo_list"),
    # 詳細表示(パラメータにPK)
    path("detail/<int:pk>/", ReportModelDetailView.as_view(), name="day_repo_detail"),
    # 日報作成入力
    path("create/input/", day_repo_create_input_view, name="day_repo_create_input"),
    # 日報作成登録
    path("create/register/", day_repo_create_register_view, name="day_repo_create_register"),
    # 日報編集入力
    path("edit/input/<int:id>/", day_repo_edit_input_view, name="day_repo_edit_input"),
    # 日報編集更新
    path("edit/update/<int:id>/", day_repo_edit_update_view, name="day_repo_edit_update"),
    # 日報削除確認
    path("delete/confirm/<int:id>/", day_repo_delete_confirm_view, name="day_repo_delete_confirm"),
    # 日報削除実行
    path("delete/execute/<int:id>/", day_repo_delete_execute_view, name="day_repo_delete_execute"),
    # 画像アップロード画面
    path("image-upload/", ImageUploadView.as_view(), name="image-upload"),
]
