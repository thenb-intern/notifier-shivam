import frappe
from frappe.model.document import Document

class Vendor(Document):
    def validate(self):
        # Create Supplier document when Vendor is validated
        supplier_exists = frappe.db.exists('Supplier', {'supplier_name': self.vendor_name})
        if not supplier_exists:
            supplier_doc = frappe.get_doc({
                "doctype": "Supplier",
                "supplier_name": self.vendor_name,
            })
            supplier_doc.insert()
            frappe.db.commit()

    def after_insert(self):
        # Trigger item price creation after Vendor document is inserted
        self.create_item_prices()

    def after_save(self):
        # Trigger item price creation after Vendor document is saved
        self.create_item_prices()

    def create_item_prices(self):
        # Retrieve vendor's price list from the items child table
        vendor_price_list = self.get_vendor_price_list()

        if vendor_price_list:
            # Fetch all active items
            items = frappe.get_all('Item', filters={'disabled': 0}, fields=['name'])
            for item in items:
                item_name = item['name']
                price_list_rate = vendor_price_list.get(item_name, None)

                if price_list_rate is not None:
                    # Check if Item Price already exists
                    item_price_exists = frappe.db.exists('Item Price', {
                        'item_code': item_name,
                        'price_list': 'Standard Selling',
                        'vendor': self.name,
                        'supplier': self.vendor_name
                    })

                    if not item_price_exists:
                        # Create Item Price document
                        frappe.get_doc({
                            'doctype': 'Item Price',
                            'item_code': item_name,
                            'price_list': 'Standard Selling',
                            'price_list_rate': price_list_rate,
                            'valid_from': frappe.utils.today(),
                            'vendor': self.name,
                            'currency': 'INR',  # Set your default currency here
                            'supplier': self.vendor_name
                        }).insert(ignore_permissions=True)

            frappe.db.commit()
        else:
            frappe.log_error(f"No price list found for vendor {self.name}", "Vendor Price List Error")

    def get_vendor_price_list(self):
        # Fetch the items child table entries for this Vendor
        vendor_price_list = {}
        if not self.items:
            frappe.logger().debug(f"No items found for vendor {self.name}")
            return None

        for item in self.items:
            vendor_price_list[item.item_name] = item.price
        return vendor_price_list
