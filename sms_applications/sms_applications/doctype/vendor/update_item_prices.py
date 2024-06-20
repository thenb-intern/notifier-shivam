# # sms_applications/sms_applications/doctype/vendor/update_item_prices.py

# import frappe

# def update_item_prices(doc, method):
   
#     vendor_name = doc.vendor_name
#     items = doc.items

#     # Check if supplier exists, if not, create one
#     if not frappe.db.exists("Supplier", vendor_name):
#         create_supplier(vendor_name)

#     for item in items:
#         item_name = item.item_name
#         price = item.price

#         # Check if item exists
#         if not frappe.db.exists("Item", item_name):
#             frappe.throw(f"Item {item_name} does not exist")

#         # Update the item master
#         item_doc = frappe.get_doc("Item", item_name)
#         item_doc.supplier = vendor_name
#         item_doc.standard_rate = price
#         item_doc.save()

# def create_supplier(vendor_name):
#     supplier_doc = frappe.get_doc({
#         "doctype": "Supplier",
#         "supplier_name": vendor_name,
#         # "supplier_type": "Manufacturer"  # Adjust as per your requirements
#     })
#     print("-----------------------------------------------------------------")
#     supplier_doc.insert()
#     frappe.db.commit()  
