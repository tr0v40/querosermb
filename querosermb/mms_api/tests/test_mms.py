from decimal import Decimal
from django.test import TestCase

from datetime import datetime, timedelta, date

from mms_api.models import CriptoValores 
from mms_api.functions import mms_days, calc_mms


class TestTimestampSequence(TestCase):
    def setUp(self):
        self.fix = [
            datetime(2021, 4, 1, 0, 0, 0),
            datetime(2021, 3, 31, 0, 0, 0),
            datetime(2021, 3, 30, 0, 0, 0),
            datetime(2021, 3, 29, 0, 0, 0),
            datetime(2021, 3, 28, 0, 0, 0),
            datetime(2021, 3, 27, 0, 0, 0),
            datetime(2021, 3, 26, 0, 0, 0),
            datetime(2021, 3, 25, 0, 0, 0),
            datetime(2021, 3, 24, 0, 0, 0),
            datetime(2021, 3, 23, 0, 0, 0),
            datetime(2021, 3, 22, 0, 0, 0),
            datetime(2021, 3, 21, 0, 0, 0),
            datetime(2021, 3, 20, 0, 0, 0),
            datetime(2021, 3, 19, 0, 0, 0),
            datetime(2021, 3, 18, 0, 0, 0),
            datetime(2021, 3, 17, 0, 0, 0),
            datetime(2021, 3, 16, 0, 0, 0),
            datetime(2021, 3, 15, 0, 0, 0),
            datetime(2021, 3, 14, 0, 0, 0)]
        self.datetimestamp = 1617383611
        self.epoch = [
        ]

    def test_create_dates(self):
        data_set = set(self.fix[0].date() - timedelta(x) for x in range(len(self.fix)))
        result = sorted(data_set - set(mms.date() for mms in mms_days(self.datetimestamp, 20)))
        self.assertListEqual(result, [])

    def test_create_dates_fail(self):
        data_set = set(self.fix[0].date() - timedelta(x) for x in range(len(self.fix)))
        result = sorted(data_set - set(mms.date() for mms in mms_days(1617159600, 20)))
        self.assertNotEqual(result, [])
    
    def test_create_dates_return_none(self):
        self.assertEqual(mms_days(), None)

class TestMmsCalculated(TestCase):
    def setUp(self):
        self.fix = (
            (1, 1617246000, 5),
            (1, 1617159600, 5),
            (1, 1617073200, 3),
            (1, 1616986800, 7),
            (1, 1616900400, 5),
            (1, 1616814000, 8),
            (1, 1616727600, 9),
            (1, 1616641200, 1),
            (1, 1616554800, 2),
            (1, 1616468400, 5),
            (1, 1616382000, 7),
            (1, 1616295600, 4),
            (1, 1616209200, 20),
            (1, 1616122800, 3),
            (1, 1616036400, 12),
            (1, 1615950000, 54),
            (1, 1615863600, 22),
            (1, 1615777200, 32),
            (1, 1615690800, 6)
        )
        for pair, tstamp, close in self.fix:
            CriptoValores.objects.create(
                pair = pair,
                mms_timestamp = tstamp,
                close = close,
            )

    def test_mms3(self):
        self.assertEqual(calc_mms(1,1615950000,3), 36)

    def test_mms3_except(self):
        self.assertEqual(calc_mms(1,1615863600, 36), None)
    
    def test_mms3_true(self):
        self.assertEqual(Decimal(calc_mms(1,1616986800, 3)), Decimal('6.66667'))
    

