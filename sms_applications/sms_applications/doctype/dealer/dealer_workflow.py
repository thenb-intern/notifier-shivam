from frappe.model.workflow import Workflow

def setup_dealer_workflow():
    # Define states
    states = [
        {"state": "Draft"},
        {"state": "Approved"},
        {"state": "Rejected"}
    ]
    
    # Define transitions
    transitions = [
        {"state": "Draft", "action": "Submit", "next_state": "Approved"},
        {"state": "Draft", "action": "Reject", "next_state": "Rejected"},
        {"state": "Approved", "action": "Reject", "next_state": "Rejected"},
        {"state": "Rejected", "action": "Revise", "next_state": "Draft"}
        # Define more transitions as needed
    ]
    
    # Attach workflow to DocType 'Dealer'
    Workflow(
        "Dealer",
        states=states,
        transitions=transitions
    ).setup()

# Call the function to set up the workflow
setup_dealer_workflow()
