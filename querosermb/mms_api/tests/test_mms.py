from django.test import TestCase
from datetime import datetime, timedelta, date
from mms_api.functions import mms_days


class TestTimestampSequence(TestCase):
    def setUp(self):
        self.fix = [
            date(2021, 4, 1),
            date(2021, 3, 31),
            date(2021, 3, 30),
            date(2021, 3, 29),
            date(2021, 3, 28),
            date(2021, 3, 27),
            date(2021, 3, 26),
            date(2021, 3, 25),
            date(2021, 3, 24),
            date(2021, 3, 23),
            date(2021, 3, 22),
            date(2021, 3, 21),
            date(2021, 3, 20),
            date(2021, 3, 19),
            date(2021, 3, 18),
            date(2021, 3, 17),
            date(2021, 3, 16),
            date(2021, 3, 15),
            date(2021, 3, 14)]
        self.datetimestamp = 1617383611

    def test_create_dates(self):
        data_set = set(self.fix[0] - timedelta(x) for x in range(len(self.fix)))
        result = sorted(data_set - set(mms_days(self.datetimestamp, 20)))
        self.assertListEqual(result, [])

