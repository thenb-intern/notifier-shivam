frappe.ui.form.on('Events', {
    // Triggered when the form is refreshed
    refresh: function(frm) {
        // Add a custom button 'Send SMS' to send SMS
        frm.add_custom_button(__('Send SMS'), function() {
            sendSMS(frm);
        }).addClass('btn-primary');

        // Add a custom button 'Send Email' to send Email
        frm.add_custom_button(__('Send Email'), function() {
            sendEmail(frm);
        }).addClass('btn-primary');

        // Add a custom button 'Add Participant' to add participant to Event_table
        frm.add_custom_button(__('Add Participant'), function() {
            frappe.prompt([
                {'fieldname': 'participant_name', 'fieldtype': 'Data', 'label': 'Participant Name'},
                {'fieldname': 'participant_email', 'fieldtype': 'Data', 'label': 'Email'},
                {'fieldname': 'participant_phone', 'fieldtype': 'Data', 'label': 'Phone'}
            ],
            function(values){
                addParticipantToEventTable(frm, values.participant_name, values.participant_email, values.participant_phone);
            }, 'Add Participant', 'Add');
        }).addClass('btn-primary');

        // Add a custom button 'Show Participants' to display participants from Event_table
        frm.add_custom_button(__('Show Participants'), function() {
            showParticipants(frm);
        }).addClass('btn-primary');
    },

    // Setup function for additional field configurations
    setup: function(frm) {
        frm.fields_dict['location'].get_query = function() {
            return {
                filters: {
                    'is_group': 0  // Example filter condition
                }
            };
        };
    }
});

// Function to send SMS
function sendSMS(frm) {
    frappe.call({
        method: 'sms_applications.sms_applications.doctype.events.events.send_sms',
        args: {
            docname: frm.doc.name
        },
        callback: function(response) {
            if (response.message === 'success') {
                frappe.msgprint('SMS sent successfully.');
                // Optionally, you can refresh the form or do other actions here
            } else {
                frappe.msgprint('Failed to send SMS.');
            }
        }
    });
}

// Function to send Email
function sendEmail(frm) {
    frappe.call({
        method: 'sms_applications.sms_applications.doctype.events.events.send_email',
        args: {
            docname: frm.doc.name
        },
        callback: function(response) {
            if (response.message === 'success') {
                frappe.msgprint('Email sent successfully.');
                // Optionally, you can refresh the form or do other actions here
            } else {
                frappe.msgprint('Failed to send Email.');
            }
        }
    });
}

// Function to add participant to Event_table
// Function to add participant to Event_table and save to database
// Function to add participant to Event_table and save to database
function addParticipantToEventTable(frm, participant_name, participant_email, participant_phone) {
    // Ensure 'participants' field exists in Event_table
    if (!frm.doc.participants) {
        frm.doc.participants = [];
    }

    // Add default country code and separator if phone_number doesn't already have one
    if (participant_phone && !participant_phone.startsWith('+91-')) {
        participant_phone = '+91-' + participant_phone.trim();
    }

    // Add participant to Event_table
    frm.doc.participants.push({
        'participants_name': participant_name,
        'email': participant_email,
        'phone_number': participant_phone
    });

    // Refresh 'participants' field
    frm.refresh_field('participants');
    // frappe.msgprint('Participant added successfully.');

    // Make a server-side call to save participant data
    frappe.call({
        method: 'sms_applications.sms_applications.doctype.events.events.add_participant_to_event_table',
        args: {
            docname: frm.doc.name,
            participant_name: participant_name,
            participant_email: participant_email,
            participant_phone: participant_phone
        },
        callback: function(response) {
            if (response.message === 'success') {
                frappe.msgprint('Participant added successfully.');
                // Optionally, you can refresh the form or do other actions here
            } else {
                frappe.msgprint('Failed to save participant to database.');
            }
        }
    });
}


// Function to show participants from Event_table
// Function to show participants from the 'participants' table field
function showParticipants(frm) {
    if (frm.doc.participants && frm.doc.participants.length > 0) {
        var participants_html = '<h4>Participants:</h4><table class="table table-bordered"><thead><tr><th>Name</th><th>Email</th><th>Phone</th></tr></thead><tbody>';
        
        frm.doc.participants.forEach(function(participant) {
            participants_html += '<tr><td>' + participant.participants_name + '</td><td>' + participant.email + '</td><td>' + participant.phone_number + '</td></tr>';
        });

        participants_html += '</tbody></table>';
        frappe.msgprint(participants_html, 'Event Participants');
    } else {
        frappe.msgprint('No participants found for this event.');
    }
}

