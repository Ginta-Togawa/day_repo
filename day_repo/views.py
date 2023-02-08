from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView

from day_repo.forms import ReportForm, ImageUploadForm
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
def day_repo_detail_view(request, id):
    # DBからの検索(ID指定取得)
    select_result = get_object_or_404(ReportModel, pk=id)

    context = {
        # 詳細データをレスポンスに設定
        "report_model": select_result,
    }

    # 詳細画面に遷移
    template_name = "day_repo/day-repo-detail.html"
    return render(request, template_name, context)


# 日報作成入力
def day_repo_create_input_view(request):
    context = {
        # 日報フォームクラスをレスポンスに設定
        "report_form": ReportForm,
    }

    # フォーム画面に遷移
    template_name = "day_repo/day-repo-form.html"
    return render(request, template_name, context)


# 日報作成登録
def day_repo_create_register_view(request):
    # リクエストデータをもとにフォームを作成(空の場合も作成)
    report_form = ReportForm(request.POST or None)

    # フォームのバリデーションチェック結果で問題がない場合に登録処理を行う
    if report_form.is_valid():
        # リクエストデータからインスタンスを生成
        report_model = ReportModel(
            title=report_form.cleaned_data["title"],
            content=report_form.cleaned_data["content"]
        )
        # DBに登録
        report_model.save()
        # 一覧画面にリダイレクト
        return redirect("day_repo_list")

    # バリデーションチェック結果に問題がある場合、エラーメッセージを設定して応答
    context = {
        "report_form": report_form,
        "error_message": "入力内容に誤りがあります。",
    }

    # フォーム画面に遷移
    template_name = "day_repo/day-repo-form.html"
    return render(request, template_name, context)


# 日報編集入力
def day_repo_edit_input_view(request, id):
    # DBからの検索(ID指定取得)
    select_result = get_object_or_404(ReportModel, pk=id)

    # 検索結果を基に更新画面フォームのインスタンスを生成
    report_form = ReportForm(
        {
            "title": select_result.title,
            "content": select_result.content,
        }
    )

    # 応答データへの設定
    context = {
        # 更新対象のID
        "id": id,
        # 日報フォームクラスを返却値に設定
        "report_form": report_form,
    }

    # フォーム画面に遷移
    template_name = "day_repo/day-repo-form.html"
    return render(request, template_name, context)


# 日報編集更新
def day_repo_edit_update_view(request, id):
    # DBからの検索(ID指定取得)
    select_result = get_object_or_404(ReportModel, pk=id)

    # 更新内容、もしくは、検索結果を基に更新データフォームのインスタンスを生成
    report_form = ReportForm(
        request.POST or {
            "title": select_result.title,
            "content": select_result.content,
        }
    )

    # フォームのバリデーションチェック結果で問題がない場合に登録処理を行う
    if report_form.is_valid():
        update_data = select_result
        update_data.title = report_form.cleaned_data["title"]
        update_data.content = report_form.cleaned_data["content"]
        update_data.save()
        # 詳細画面にリダイレクト
        return redirect("day_repo_detail", id)

    # バリデーションチェック結果に問題がある場合、エラーメッセージを設定して応答
    context = {
        "report_form": report_form,
        "error_message": "入力内容に誤りがあります。",
    }
    # フォーム画面に遷移
    template_name = "day_repo/day-repo-form.html"
    return render(request, template_name, context)


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
