# tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu  # Import Menu model from your app
from Restaurant.serializers import MenuSerializer  # Import MenuSerializer from your app

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu_item1 = Menu.objects.create(name="Pasta", price=12.99)
        self.menu_item2 = Menu.objects.create(name="Pizza", price=9.99)
        self.menu_item3 = Menu.objects.create(name="Burger", price=8.99)

        # Initialize the API client for testing views
        self.client = APIClient()

    def test_getall(self):
        # Use Django's reverse function to get the URL of the view you want to test
        url = reverse('menu-list')  # Ensure this is the correct name for your menu list view

        # Make a GET request to the view
        response = self.client.get(url)

        # Retrieve all the Menu objects from the database
        menu_items = Menu.objects.all()

        # Serialize the retrieved objects
        serializer = MenuSerializer(menu_items, many=True)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data matches the serialized data
        self.assertEqual(response.data, serializer.data)
