from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

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


# 日報削除
class ReportModelFormDeleteView(DeleteView):
    template_name = "day_repo/day-repo-delete.html"
    model = ReportModel
    success_url = reverse_lazy('day_repo_list')


# 画像アップロード(ディレクトリ)
class ImageUploadView(CreateView):
    form_class = ImageUploadForm
    template_name = "day_repo/image-upload.html"
    success_url = "/day_repo"
