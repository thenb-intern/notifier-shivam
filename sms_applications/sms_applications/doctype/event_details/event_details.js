frappe.ui.form.on('event_details', {
    refresh: function (frm) {
        // Check if the document name is available
        if (frm.doc.name) {
            // Log the document name for debugging
            console.log('Document Name:', frm.doc.name);

            // Make an API call to fetch the linked event ID using the event_details document name
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "Events",
                    fieldname: "name",
                    filters: { event_name: frm.doc.name }
                },
                callback: function (response) {
                    if (response.message) {
                        const event_id = response.message.name;

                        // Log the event ID for debugging
                        console.log('Linked Event ID:', event_id);

                        // Make another API call to fetch the event details
                        frappe.call({
                            method: "frappe.client.get",
                            args: {
                                doctype: "Events",
                                name: event_id
                            },
                            callback: function (eventResponse) {
                                if (eventResponse.message) {
                                    // Log the fetched event data for debugging
                                    console.log('Fetched Event Data:', eventResponse.message);

                                    // Check if the participants field contains data
                                    const participantsData = eventResponse.message.participants;
                                    if (participantsData && participantsData.length > 0) {
                                        // Add "Show Participant" button if participants field has rows
                                        frm.add_custom_button(__('Show Participant'), function () {
                                            // Redirect to the linked Event document
                                            const event_url = `/app/events/${event_id}`;
                                            window.location.href = event_url;
                                        });
                                    } else {
                                        // Add "Add Participant" button if participants field is empty
                                        frm.add_custom_button(__('Add Participant'), function () {
                                            // Redirect to the linked Event document
                                            const event_url = `/app/events/${event_id}`;
                                            window.location.href = event_url;
                                        });
                                    }
                                } else {
                                    frappe.msgprint(__('No linked event details found.'));
                                }
                            }
                        });
                    } else {
                        frappe.msgprint(__('No linked event found.'));
                    }
                }
            });
        } else {
            frappe.msgprint(__('No linked event found.'));
        }
    }
});
