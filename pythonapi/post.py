import requests

# API endpoint
api_endpoint = "http://shivam.nbnext.in:8000/api/method/sms_applications.api.add_dummyapi_data"

# API key and secret
api_key = "193239ff4b8ef83"
api_secret = "1b743dfc02794b0"
# Data to be sent
data = {
    "names": "John Doe",
    "email": "johndoe@gmail.com",
    "age": 30
}


headers = {
    'Authorization': f'token {api_key}:{api_secret}',
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(api_endpoint, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    try:
        print("Data successfully added to dummyapi.")
        print(f"Document Name: {response.json()}")
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
else:
    print(f"Failed to add data. HTTP Status Code: {response.status_code}, Message: {response.text}")
