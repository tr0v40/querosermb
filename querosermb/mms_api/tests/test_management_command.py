from django.core.management import call_command
from ..management.commands import incremental_request
from django.test import TestCase

class TestIncrementalRequest(TestCase):
    def call_command(self):
        call_command('incremental_request')
    
    def test_handler(self):
        print(self.call_command())