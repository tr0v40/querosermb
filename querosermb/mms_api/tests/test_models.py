from django.test import TestCase

from ..models import CriptoValores

class TestMmsModel(TestCase):
    def setUp(self):
        self.cripto = CriptoValores.objects.create(
            pair = 1,
            mms_timestamp = 1617374756,
            close = 1.1,
        )
    
    def test_choice_btc_true(self):
        btc = CriptoValores.objects.get(mms_timestamp=self.cripto.mms_timestamp)
        self.assertEqual(btc.get_pair_display(), 'BRLBTC')
    
    def test_choice_btc_false(self):
        btc = CriptoValores.objects.get(mms_timestamp=self.cripto.mms_timestamp)
        self.assertNotEqual(btc.get_pair_display(), 'BRLETH')

    def test_return_true(self):
        btc = CriptoValores.objects.get(mms_timestamp=self.cripto.mms_timestamp)
        self.assertEqual(btc.__str__(), '1617374756')
    
    def test_return_False(self):
        btc = CriptoValores.objects.get(mms_timestamp=self.cripto.mms_timestamp)
        self.assertNotEqual(btc.__str__(), '222222')
    
    def test_return_create_new(self):
        btc = CriptoValores.objects.create(
            pair = 2,
            mms_timestamp = 1617374756,
            close = 1.1,
        )
        self.assertEqual(btc.get_pair_display(), 'BRLETH')


