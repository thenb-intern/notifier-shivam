// frappe.ui.form.on('event_details', {
//     refresh: function (frm) {
//         // Check if the document name is available
//         if (frm.doc.name) {
//             // Log the document name for debugging
//             console.log('Document Name:', frm.doc.name);

//             // Make an API call to fetch the linked event ID using the event_details document name
//             frappe.call({
//                 method: "frappe.client.get_value",
//                 args: {
//                     doctype: "Events",
//                     fieldname: "name",
//                     filters: { event_name: frm.doc.name }
//                 },
//                 callback: function (response) {
//                     if (response.message) {
//                         const event_id = response.message.name;

//                         // Log the event ID for debugging
//                         console.log('Linked Event ID:', event_id);

//                         // Make another API call to fetch the event details
//                         frappe.call({
//                             method: "frappe.client.get",
//                             args: {
//                                 doctype: "Events",
//                                 name: event_id
//                             },
//                             callback: function (eventResponse) {
//                                 if (eventResponse.message) {
//                                     // Log the fetched event data for debugging
//                                     console.log('Fetched Event Data:', eventResponse.message);

//                                     // Check if the participants field contains data
//                                     const participantsData = eventResponse.message.participants;
//                                     if (participantsData && participantsData.length > 0) {
//                                         // Add "Show Participant" button if participants field has rows
//                                         frm.add_custom_button(__('Show Participant'), function () {
//                                             // Redirect to the linked Event document
//                                             const event_url = `/app/events/${event_id}`;
//                                             window.location.href = event_url;
//                                         });
//                                     } else {
//                                         // Add "Add Participant" button if participants field is empty
//                                         frm.add_custom_button(__('Add Participant'), function () {
//                                             // Redirect to the linked Event document
//                                             const event_url = `/app/events/${event_id}`;
//                                             window.location.href = event_url;
//                                         });
//                                     }
//                                 } else {
//                                     frappe.msgprint(__('No linked event details found.'));
//                                 }
//                             }
//                         });
//                     } else {
//                         frappe.msgprint(__('No linked event found.'));
//                     }
//                 }
//             });
//         } else {
//             frappe.msgprint(__('No linked event found.'));
//         }
//     }
// });
frappe.ui.form.on('event_details', {
    refresh: function(frm) {
        // Add a custom button 'Add Participant' to add participant to Event_table
        frm.add_custom_button(__('Add Participant'), function() {
            frappe.prompt([
                { 'fieldname': 'participant_name', 'fieldtype': 'Data', 'label': 'Participant Name' },
                { 'fieldname': 'participant_email', 'fieldtype': 'Data', 'label': 'Email' },
                { 'fieldname': 'participant_phone', 'fieldtype': 'Data', 'label': 'Phone' }
            ],
            function(values) {
                addParticipantToEventTable(frm, values.participant_name, values.participant_email, values.participant_phone);
            }, 'Add Participant', 'Add');
        }).addClass('btn-primary');
        console.log("Added Add Participant button");
    }
});

// Function to add participant to Event_table and save to database
function addParticipantToEventTable(frm, participant_name, participant_email, participant_phone) {
    if (!frm.doc.participants) {
        frm.doc.participants = [];
    }

    if (participant_phone && !participant_phone.startsWith('+91-')) {
        participant_phone = '+91-' + participant_phone.trim();
    }

    frm.doc.participants.push({
        'participants_name': participant_name,
        'email': participant_email,
        'phone_number': participant_phone
    });

    frm.refresh_field('participants');

    frappe.call({
        method: 'sms_applications.sms_applications.doctype.event_details.event_details.add_participant_to_event_table',
        args: {
            docname: frm.doc.name,
            participant_name: participant_name,
            participant_email: participant_email,
            participant_phone: participant_phone
        },
        callback: function(response) {
            if (response.message === 'success') {
                frappe.msgprint('Participant added successfully.');
            } else {
                frappe.msgprint('Failed to save participant to database.');
            }
        }
    });
}
