from random import randint

from django.shortcuts import render


# Create your views here.

# テンプレート用HTML表示メソッド
def day_repo_list_view(request):
    # テンプレート用HTML"day-repo-list.html"を描画
    return render(request, "day_repo/day-repo-list.html")


# 日報詳細表示
def day_repo_detail_view(request):
    template_name = "day_repo/day-repo-detail.html"
    random_int = randint(1, 10)
    context = {
        "random_number": random_int,
    }
    return render(request, template_name, context)
