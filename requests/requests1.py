import requests

try:
    url = "https://qa-api.lendisoft.com/api/clients/payment_methods"

    headers = {
        # "Authorization": "Bearer YOUR_TOKEN",
        "Content-Type": "application/json",
        # "Custom-Header": "value123"
    }

    params = {
        "token": "U6u6uTms63Dhc4YbwrCxEYmdqnvVAQIh"
    }

    response = requests.get(url, headers=headers, params=params)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    if response.status_code == 200:
        print("Success")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
except Exception as e:
    print(f"Error occurred: {e}")
