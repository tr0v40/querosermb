from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestCriptoValoresViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_response_200_btc_mms20(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLBTC', 'mms':20}))
        self.assertEqual(response.status_code, 200)
    
    def test_response_200_btc_mms50(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLBTC', 'mms':50}))
        self.assertEqual(response.status_code, 200)
    
    def test_response_200_btc_mms200(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLBTC', 'mms':200}))
        self.assertEqual(response.status_code, 200)
    
    def test_response_200_eth_mms20(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLETH', 'mms':20}))
        self.assertEqual(response.status_code, 200)
    
    def test_response_200_eth_mms50(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLETH', 'mms':50}))
        self.assertEqual(response.status_code, 200)
  
    def test_response_200_eth_mms200(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLETH', 'mms':200}))
        self.assertEqual(response.status_code, 200)    
    
    def test_response_forbidden_critpo(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'EURBTC', 'mms':50}))
        self.assertEqual(response.status_code, 403)
    
    def test_response_forbidden_mms(self):
        response = self.client.get(reverse('mms_api:criptovalores', kwargs={'pair': 'BRLBTC', 'mms':0}))
        self.assertEqual(response.status_code, 403)
    
    def test_response_200_btc_frrom_to(self):
        response = self.client.get('/BRLBTC/200/?from=1577836800&to=1606565306')
        self.assertEqual(response.status_code, 200)
    
    def test_response_200_eth_frrom_to(self):
        response = self.client.get('/BRLETH/200/?from=1577836800&to=1606565306')
        self.assertEqual(response.status_code, 200)