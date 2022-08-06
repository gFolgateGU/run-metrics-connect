import requests

import unit_conversions as uc
from api_key_mgr import ApiKeyMgr

# Services
from api_services.strava_api_key_service import StravaApiKeyService
from api_services.strava_api_activity_service import StravaApiActivityService

# Load in API Keys
file_name = 'api_keys.yaml'
api_key_parser = ApiKeyMgr(file_name)

# Refreshing API Keys
strava_api_key_service = StravaApiKeyService(api_key_parser)
strava_api_key_service.refresh_api_keys()

# Obtaining latest and greatest API Keys for Strava
api_keys = api_key_parser.get_data_for_source("strava")

# Get a default amount of activities for a user.
strava_act_service = StravaApiActivityService(api_keys)
activities = strava_act_service.get_activities()

# Print out a list of activities for the user.
print(activities)