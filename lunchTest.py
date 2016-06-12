"""Test suite for lunch.py.

Written by: Harpreet Singh
""" 
import unittest
from lunch import IntercomLunch


class LunchTest(unittest.TestCase):

	def test_usual_customer_list(self):
		ob = IntercomLunch()
		customerList = [{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"},
		{"latitude": "53.2451022", "user_id": 4, "name": "Ian Kehoe", "longitude": "-6.238335"}]
		qualifiedCustomer = [{"latitude": "53.2451022", "user_id": 4, "name": "Ian Kehoe", "longitude": "-6.238335"}]
		
		self.assertEqual(ob.findCustomersToInvite(customerList), qualifiedCustomer)

	def test_empty_customer_list(self):
		ob = IntercomLunch()
		customerList = []
		qualifiedCustomer = []
		self.assertEqual(ob.findCustomersToInvite(customerList), qualifiedCustomer)

if __name__ == '__main__':
	unittest.main()

