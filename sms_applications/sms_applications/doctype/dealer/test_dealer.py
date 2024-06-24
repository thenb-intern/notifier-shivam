# Copyright (c) 2024, shivam kumar singh and Contributors
# See license.txt

# import frappe
import frappe
import unittest

class TestDealer(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_dealer(self):
        # Test the creation of a Dealer
        dealer = frappe.get_doc({
            "doctype": "Dealer",
            "dealer_name": "Test Dealer",
            "phone_number": "+91-9876543210"
        })
        dealer.insert()

        # Fetch the created dealer
        created_dealer = frappe.get_doc("Dealer", dealer.name)

        # Assert that the created dealer's name and phone number are correct
        self.assertEqual(created_dealer.dealer_name, "Test Dealer")
        self.assertEqual(created_dealer.phone_number, "+91-9876543210")

        # Cleanup
        created_dealer.delete()

    def test_duplicate_dealer_name(self):
        # Test that duplicate dealer names are not allowed
        dealer_1 = frappe.get_doc({
            "doctype": "Dealer",
            "dealer_name": "Unique Dealer",
            "phone_number": "+91-9876543211"
        })
        dealer_1.insert()

        # Attempt to create a duplicate dealer
        dealer_2 = frappe.get_doc({
            "doctype": "Dealer",
            "dealer_name": "Unique Dealer",
            "phone_number": "+91-9876543212"
        })

        with self.assertRaises(frappe.DuplicateEntryError):
            dealer_2.insert()

        # Cleanup
        dealer_1.delete()

if __name__ == '__main__':
    unittest.main()
