from unittest import TestCase

from day_repo.models import ReportModel


class DayRepoTestCase(TestCase):
    def setUp(self):
        obj = ReportModel(
            title="testTitle1", content="testContent1")
        obj.save()

    def test_saved_single_object(self):
        qs_counter = ReportModel.objects.count()
        self.assertEqual(qs_counter, 1)
