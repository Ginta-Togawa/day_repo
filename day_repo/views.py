from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from day_repo.forms import ImageUploadForm, ReportModelForm
from day_repo.models import ReportModel


# Create your views here.

# UserPassesTestMixinを継承したログインユーザと日報作成者の紐づけクラス
class OwnerOnly(UserPassesTestMixin):

    # 引数の日報作成者とログインユーザの比較結果を返却
    def test_func(self):
        report_instance = self.get_object()
        return report_instance.user == self.request.user

    # 権限がない場合、詳細ページに遷移
    def handle_no_permission(self):
        messages.error(self.request, "編集・削除はご自身の日報のみ可能です。")
        return redirect("day_repo_detail", pk=self.kwargs["pk"])


# 日報一覧表示
# 1.modelで指定したデータベーステーブルからQuerySetを取得する
# 2.「object_list」という変数にQuerySetを格納する
# 3.HTMLテンプレートへコンテキストとしてQuerySetを渡す
class ReportModeListView(LoginRequiredMixin, ListView):
    template_name = "day_repo/day-repo-list.html"
    model = ReportModel


# 日報詳細表示
# 1.ブラウザから「pk」を受け取る
# 2.データベースから「pk」が一致するデータを取り出す
# 3.コンテキストとしてHTMLテンプレートへ渡す
class ReportModelDetailView(LoginRequiredMixin, DetailView):
    template_name = "day_repo/day-repo-detail.html"
    model = ReportModel


# 日報作成入力・登録
class ReportModelFormCreateView(LoginRequiredMixin, CreateView):
    template_name = "day_repo/day-repo-form.html"
    form_class = ReportModelForm
    success_url = reverse_lazy('day_repo_list')

    # formクラスへのユーザ情報を渡す
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


# 日報編集入力・更新
class ReportModelFormUpdateView(OwnerOnly, LoginRequiredMixin, UpdateView):
    template_name = "day_repo/day-repo-form.html"
    model = ReportModel
    form_class = ReportModelForm
    success_url = reverse_lazy('day_repo_list')


# 日報削除
class ReportModelFormDeleteView(OwnerOnly, LoginRequiredMixin, DeleteView):
    template_name = "day_repo/day-repo-delete.html"
    model = ReportModel
    success_url = reverse_lazy('day_repo_list')


# 画像アップロード(ディレクトリ)
class ImageUploadView(LoginRequiredMixin, CreateView):
    form_class = ImageUploadForm
    template_name = "day_repo/image-upload.html"
    success_url = "/day_repo"
