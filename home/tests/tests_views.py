from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class HomeViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('home:home_view'))
        self.assertAlmostEqual(response.status_code, 200)
