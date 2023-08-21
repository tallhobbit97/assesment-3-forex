import currencies
from app import app
from unittest import TestCase

class AppTests(TestCase):
    
    def setUp(self):
        """Stuff to have ready for every test"""
        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_homepage(self):
        response = self.client.get('/')
        self.assertIn(b'Converting from', response.data)
    
    def test_check_currency(self):
        self.assertTrue(currencies.check_currency('USD'))
        self.assertFalse(currencies.check_currency('YYY'))