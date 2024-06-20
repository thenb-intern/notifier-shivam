import frappe

def execute(filters=None):
    columns = get_columns()
    data = []

    # Fetch data from 'Max Stock Level' doctype
    max_stock_levels = fetch_max_stock_levels()
    
    for level in max_stock_levels:
        item = level.item
        stock_level = level.number  

        # Additional processing if needed
        processed_data = process_data(item, stock_level)
        data.append(processed_data)

    return columns, data

def fetch_max_stock_levels():
    # Fetch data from 'Max Stock Level' doctype 
    max_stock_levels = frappe.get_all(
        'Max_Stock_Level',
        fields=['item', 'number'] 
    )
    
    return max_stock_levels

def process_data(item, number): 
    # Process
    processed_data = {
        "item": item,
        "number": number, 
    }
    return processed_data

def get_columns():
    # Define the columns structure for the report
    columns = [
        {"label": "Item", "fieldname": "item", "fieldtype": "Link", "options": "Item", "width": 120},
        {"label": "Day-1", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
        {"label": "Day-2", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
		{"label": "Day-3", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
		{"label": "Day-4", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
		{"label": "Day-5", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
		{"label": "Day-6", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
		{"label": "Day-7", "fieldname": "number", "fieldtype": "Int", "width": 150}, 
		{"label": "Day-8", "fieldname": "number", "fieldtype": "Int", "width": 150}, 

    ]
    return columns
