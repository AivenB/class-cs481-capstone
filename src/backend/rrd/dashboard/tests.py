from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TestViews(TestCase):
    
    # Setup method to run before each test
    def setUp(self):
        self.client = Client()

        # URL paths
        self.dashboard = reverse('dashboard')

    # Test index/home view
    # def test_index_GET(self):

        # Get the response from the index URL
        # response = self.client.get(self.index_url)

        # write assertions to test the response
        # print(response)
        # self.assertEquals(response.status_code, 201) # purposefully failing test
        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'index.html')
    
    # Test dashboard view
    def test_dashboard_GET(self):
        # Get the response from the dashboard URL
        # response = self.client.get(reverse('dashboard'))
        response = self.client.get(self.dashboard)

        # Check if the response status code is 200 (OK)
        self.assertEquals(response.status_code, 200)

        # Check if the correct template was used
        self.assertTemplateUsed(response, 'dashboard.html')