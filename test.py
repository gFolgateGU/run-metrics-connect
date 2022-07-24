import requests

import unit_conversions as uc
from api_key_parser import ApiKeyParser

# Load in API Keys for Strava API
file_name = 'api_keys.yaml'
api_key_parser = ApiKeyParser(file_name)
api_keys = api_key_parser.get_data_for_source("strava")

# Build URI String to Get Activity Data from Personal Account
base_uri = 'https://www.strava.com/api/v3/'
option = 'athlete/activities?'
access_token = '76298ad3e2ae4e3ecd3ed43481955d11660effe7'
access_token_str = f'access_token={api_keys.access_token}'
uri = base_uri + option + access_token_str

# Perform an HTTP Get on the URI to get Data
response = requests.get(uri)

# Get some example JSON data as a starting point
status = response.status_code
data = response.json()

# Most recent run data.
run_length_meters = data[0]['distance']
run_length_miles = run_length_meters * uc.METERS_TO_MILES

print(f'HTTP Status: {status}')
print(f'Most recent run length (miles): {run_length_miles}')
