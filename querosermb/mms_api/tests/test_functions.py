from django.test import TestCase
from datetime import datetime, timedelta

from ..functions import today, converter_to_date

class TestFunctionToday(TestCase):
    def setUp(self):
        self.today = datetime.now()
    
    def test_today_true(self):
        self.assertEqual(self.today, today())
    
    def test_today_false(self):
        self.assertNotEqual(self.today-timedelta(1), today())

class TestFunctionConverterToTimestamp(TestCase):
    def setUp(self):
        self.ts = datetime.fromtimestamp(1577836800)
    
    def test_converter_to_timestamp_true(self):
        self.assertEqual(self.ts, converter_to_date(1577836800))

