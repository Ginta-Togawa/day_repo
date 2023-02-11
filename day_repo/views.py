from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from day_repo.forms import ImageUploadForm, ReportModelForm
from day_repo.models import ReportModel


# Create your views here.

# 日報一覧表示
# 1.modelで指定したデータベーステーブルからQuerySetを取得する
# 2.「object_list」という変数にQuerySetを格納する
# 3.HTMLテンプレートへコンテキストとしてQuerySetを渡す
class ReportModeListView(ListView):  # クラス作成
    template_name = "day_repo/day-repo-list.html"
    model = ReportModel


# 日報詳細表示
# 1.ブラウザから「pk」を受け取る
# 2.データベースから「pk」が一致するデータを取り出す
# 3.コンテキストとしてHTMLテンプレートへ渡す
class ReportModelDetailView(DetailView):
    template_name = "day_repo/day-repo-detail.html"
    model = ReportModel


# 日報作成入力・登録
class ReportModelFormCreateView(CreateView):
    template_name = "day_repo/day-repo-form.html"
    form_class = ReportModelForm
    success_url = reverse_lazy('day_repo_list')


# 日報編集入力・更新
class ReportModelFormUpdateView(UpdateView):
    template_name = "day_repo/day-repo-form.html"
    model = ReportModel
    form_class = ReportModelForm
    success_url = reverse_lazy('day_repo_list')


# 日報削除確認
def day_repo_delete_confirm_view(request, id):
    # DBからの検索(ID指定取得)
    select_result = get_object_or_404(ReportModel, pk=id)

    context = {
        # 削除フラグを設定
        "delete_flag": True,
        # 詳細データをレスポンスに設定
        "report_model": select_result,
    }

    # 詳細画面に遷移
    template_name = "day_repo/day-repo-detail.html"
    return render(request, template_name, context)


# 日報削除確認
def day_repo_delete_execute_view(request, id):
    # DBからの検索(ID指定取得)
    select_result = get_object_or_404(ReportModel, pk=id)
    # DBから削除
    select_result.delete()
    # 一覧画面にリダイレクト
    return redirect("day_repo_list")


# 画像アップロード(ディレクトリ)
class ImageUploadView(CreateView):
    form_class = ImageUploadForm
    template_name = "day_repo/image-upload.html"
    success_url = "/day_repo"
