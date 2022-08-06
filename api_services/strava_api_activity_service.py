from api_services.api_service_base import ApiServiceBase

class StravaApiActivityService(ApiServiceBase):
    def __init__(self, api_keys):
        self.act_uri_base = 'https://www.strava.com/api/v3/athlete/activities?'
        self.api_keys = api_keys

    def get_activities(self):
        uri_params = self._build_activity_query_dict()

        # Build the final URI string
        uri = self.build_uri(uri_base=self.act_uri_base,
                             uri_param_dict=uri_params)

        results = self.http_get(uri)

        if results.valid() is False:
            print(f'StravaApiActivityService: HTTP BAD: {results.http_status}')
            return

        activities = results.json_data
        return activities
                
    def _build_activity_query_dict(self):
        activity_query_dict = {}
        activity_query_dict["access_token"] = self.api_keys.access_token

        return activity_query_dict