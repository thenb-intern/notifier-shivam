# Import necessary modules
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.core.doctype.communication.email import make


class Events(Document):
    pass

@frappe.whitelist()
def send_sms(docname):
    try:
        # Fetch the event document
        event_doc = frappe.get_doc('Events', docname)
       
        participants = event_doc.get('participants')  
        
        # Print each participant's name and phone number
        for participant in participants:
            phone_number = participant.phone_number
            participants_name = participant.participants_name
          
            if phone_number:
                print("---------------------------------------------------------------")
                print(f'Participant Name: {participants_name}, Phone Number: {phone_number}')
        
        return 'success'
    except Exception as e:
        frappe.log_error(_('Failed to fetch data: {0}').format(str(e)))
        return 'error'

@frappe.whitelist()
def send_email(docname):
    try:
        # Fetch the event document
        event_doc = frappe.get_doc('Events', docname)
        
        participants = event_doc.get('participants')
        
        # Print each participant's name and email address
        for participant in participants:
            email = participant.email
            participants_name = participant.participants_name
            
            if email:
                print("---------------------------------------------------------------")
                print(f'Participant Name: {participants_name}, Email: {email}')
                # subject = _('Event Notification')
                # message = _('Hello {0},<br><br>This is a reminder for the upcoming event.<br><br>Best regards,<br>Event Organizer').format(participants_name)
                
                # # Send email using Frappe's make function
                # make(subject=subject, content=message, recipients=email, send_email=True)
                
                # # Optionally, you can log or print confirmation
                # print(f'Email sent successfully to {participants_name}, Email: {email}')
        
        return 'success'
    except Exception as e:
        frappe.log_error(_('Failed to send emails: {0}').format(str(e)))
        return 'error'
    
# events.py

# @frappe.whitelist()
# def create_event_participant(event_name, participant_name, participant_email, participant_phone):
#     try:
#         # Create a new participant document and link it to the event
#         participant = frappe.new_doc('Participants')
#         participant.update({
#             'participant_name': participant_name,
#             'participant_email': participant_email,
#             'participant_phone': participant_phone,
#             'event': event_name
#         })
#         participant.insert(ignore_permissions=True)
#         frappe.db.commit()
#         return 'success'
#     except Exception as e:
#         frappe.log_error(f"Error creating participant for event {event_name}: {str(e)}")
#         return 'failed'

# @frappe.whitelist()
# def get_event_participants(event_name):
#     participants = frappe.get_all('Participants', filters={'event': event_name},
#                                   fields=['participant_name', 'participant_email', 'participant_phone'])
#     return participants
# @frappe.whitelist()
# def add_participant_to_event_table(docname, participant_name, participant_email, participant_phone):
#     event_doc = frappe.get_doc('Events', docname)
#     event_doc.append('participants', {
#         'participants_name': participant_name,
#         'email': participant_email,
#         'phone_number': participant_phone
#     })
#     event_doc.save(ignore_permissions=True)
#     return 'success'

