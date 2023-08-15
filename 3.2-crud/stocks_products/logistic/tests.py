from rest_framework.test import APIClient
from unittest import TestCase

class SampleTestCase(TestCase):
    def test_bad_case(self):
        client = APIClient()
        response = client.get('/api/v1/sample')
        self.assertEqual(response.status_code, 404)

    def test_successful(self):
        client = APIClient()
        response = client.get('/api/v1/test/')
        self.assertEqual(response.status_code, 200)


