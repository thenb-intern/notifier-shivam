import requests

# API endpoint 
api_endpoint = "http://shivam.nbnext.in:8000/api/method/sms_applications.api.get_dummyapi_data"

# API key and secret 
api_key = "193239ff4b8ef83"
api_secret = "1b743dfc02794b0"


auth = requests.auth.HTTPBasicAuth(api_key, api_secret)


response = requests.get(api_endpoint, auth=auth)

# Check the response
if response.status_code == 200:
    try:
        data = response.json()
        print("Data retrieved from API:",data["message"])
        for entry in data["message"]:
            print(f"Name: {entry['name']}, Email: {entry['email']}, Age: {entry['age']}")
    except ValueError as e:
        print(f"Failed to parse JSON response: {e}")
else:
    print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}, Message: {response.text}")
