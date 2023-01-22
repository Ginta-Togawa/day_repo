from django.shortcuts import render


# Create your views here.

# テンプレート用HTML表示メソッド
def day_repo_list_view(request):
    # テンプレート用HTML"day-repo-list.html"を描画
    return render(request, "day_repo/day-repo-list.html")
