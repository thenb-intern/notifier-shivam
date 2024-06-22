# sms_applications/sms_applications/api.py
import frappe
from frappe import _

@frappe.whitelist()
def get_dummyapi_data():
    data = frappe.get_all('dummyapi', fields=['name', 'email', 'age'])
    return data

@frappe.whitelist(allow_guest=True)
def add_dummyapi_data():
    try:
        # Get request data
        request_data = frappe.request.json
        print("---------------------------------",request_data)

        # Extract parameters
        names = request_data.get('names')
        email = request_data.get('email')
        age = request_data.get('age')

        # Create a new 'dummyapi' document
        doc = frappe.new_doc('dummyapi')
        doc.names = names
        doc.email = email
        doc.age = age
        doc.insert()

        frappe.db.commit()

        # Return the name of the inserted document
        return {
            'data': doc.name
        }

    except Exception as e:
        frappe.log_error(f"Error adding dummyapi data: {e}", _("API Error"))
        frappe.throw(_("Failed to add dummyapi data"))
