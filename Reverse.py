import requests

# Replace 'YOUR_API_KEY' with your actual OpenCage API key
API_KEY = 'c59d1124652340dea253de6cf72a6c3f'

# Latitude and Longitude coordinates obtained from forward geocoding
latitude = 4.2921
longitude = 34.8219

# Create the API request URL for reverse geocoding
base_url = 'https://api.opencagedata.com/geocode/v1/json'
params = {
    'q': f'{latitude},{longitude}',  # Format coordinates as 'latitude,longitude'
    'key': API_KEY
}

# Send the request to the OpenCage API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data['status']['code'] == 200:
        # Extract the formatted address from the response
        formatted_address = data['results'][0]['formatted']

        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
        print(f'Address: {formatted_address}')
    else:
        print(f'Error: {data["status"]["message"]}')
else:
    print(f'HTTP Error: {response.status_code}')
