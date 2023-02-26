import django_filters
from django.forms.widgets import Select

from day_repo.models import ReportModel

# 一覧画面上の公開フラグフィルターのセレクトボックス要素
release_flag_choices = ((0, "全て"), (1, "公開済のみ"), (2, "ドラフトのみ"))


# 日報モデル用フィルタークラス
class ReportModelFilter(django_filters.FilterSet):
    # 公開・非公開を入力
    release_flag = django_filters.TypedChoiceFilter(
        # セレクトボックスの要素
        choices=release_flag_choices,
        # フィルタリングメソッドとの紐づけ
        method="release_flag_chosen",
        # 画面上の項目表示名(非表示)
        label="",
        # セレクトボックスのHTML設定
        widget=Select(attrs={"class": "form-select"}))
    # 年月日によるもの
    date = django_filters.TypedChoiceFilter(
        # フィルタリングメソッドとの紐づけ
        method="timestamp_checker",
        # 画面上の項目表示名
        label="作成月",
        # セレクトボックスのHTML設定
        widget=Select(attrs={"class": "form-select"}))

    #
    profile = django_filters.NumberFilter(method="get_profile_day_repo")

    class Meta:
        # 元モデルクラス
        model = ReportModel
        # 項目(作成日、公開フラグ)
        fields = ["date", "release_flag"]

    def __init__(self, *args, **kwargs):
        qs = kwargs["queryset"]
        choice_option = [(obj.date.year, obj.date.month) for obj in qs]
        choice_option = list(set(choice_option))
        choice_option.sort(reverse=True)
        DATE_OPTIONS = [
            ((year, month), f"{year}年{month}月") for year, month in choice_option
        ]
        DATE_OPTIONS.insert(0, (None, "---"))
        self.base_filters["date"].extra["choices"] = DATE_OPTIONS
        super().__init__(*args, **kwargs)

    # セレクトボックスの値と作成日の紐づけ
    def timestamp_checker(self, queryset, name, value):
        qs = queryset
        if value is not None:
            year, month = eval(value)
            qs = queryset.filter(date__year=year).filter(date__month=month)
        return qs

    # セレクトボックスの値と公開フラグの紐づけ
    def release_flag_chosen(self, queryset, name, value):
        qs = queryset
        if value == "1":
            qs = qs.filter(release_flag=True)
        elif value == "2":
            qs = qs.filter(release_flag=False)
        return qs

    def get_profile_day_repo(self, queryset, name, value):
        from accounts.models import Profile
        qs = queryset
        if Profile.objects.filter(id=value).exists():
            qs = qs.filter(user__profile__id=value)
        else:
            qs = qs.none()
        return qs
