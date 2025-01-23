import unittest
from shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"hat": 10, "pant": 20, "cloth": 30})

    def test_get_total_amount(self):
        self.assertEqual(self.shopping_list.get_total_amount(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 60)
