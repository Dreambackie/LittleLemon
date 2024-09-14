from django.test import TestCase
from Restaurant.models import Menu

class TestMenu(TestCase):
    def setUp(self):
        # Set up any initial data or state needed for the tests
        self.menu_item = Menu.objects.create(title="Ice cream", price=10.99, inventory = 9)

    def test_menu_str(self):
        # Compare the string representation of the menu item with the expected value
        self.assertEqual(str(self.menu_item), "Ice cream")
       