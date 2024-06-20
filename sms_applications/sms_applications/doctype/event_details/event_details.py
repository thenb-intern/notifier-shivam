# Copyright (c) 2024, shivam kumar singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class event_details(Document):
	pass
@frappe.whitelist()
def add_participant_to_event_table(docname, participant_name, participant_email, participant_phone):
    event_doc = frappe.get_doc('event_details', docname)
    event_doc.append('participants', {
        'participants_name': participant_name,
        'email': participant_email,
        'phone_number': participant_phone
    })
    event_doc.save(ignore_permissions=True)
    return 'success'
