from api_services.api_service_base import ApiServiceBase

class StravaApiKeyService(ApiServiceBase):
    def __init__(self, api_key_mgr):
        self.api_key_mgr = api_key_mgr
        self.api_key_name = 'strava'
        self.refresh_token_uri_base = 'https://www.strava.com/oauth/token?'

    def refresh_api_keys(self):
        '''
        Genereate and refresh API keys for Strava
        '''
        # Attempt to load API Key Data
        api_key_data = self._load_existing_keys()

        # If there is no data associated with this API Key, then return.
        if api_key_data is None:
            print(f'ERROR: No API Key Data found for Key: {self.api_key_name}')
            return

        # Build associated parameters for the HTTP Post Request
        uri_params = self._build_refresh_query_dict(api_key_data=api_key_data)

        # Build the final URI string
        uri = self.build_uri(uri_base=self.refresh_token_uri_base,
                             uri_param_dict=uri_params)
        
        results = self.http_post(uri)

        if results.valid() is False:
            print(f'StravaApiKeyService: HTTP BAD: {results.http_status}')
            return

        new_tokens = results.json_data

        print(new_tokens)

        self._store_new_api_keys(new_tokens, api_key_data)
   
    def _load_existing_keys(self):
        '''
        Load existing API keys from file
        '''
        api_key_data = self.api_key_mgr.get_data_for_source(self.api_key_name)
        return api_key_data

    def _build_refresh_query_dict(self, api_key_data):
        '''
        Builds Paramters Associated with HTTP Request associated with Refresh.
        '''
        refresh_query_dict = {}
        refresh_query_dict['client_id'] = api_key_data.client_id
        refresh_query_dict['client_secret'] = api_key_data.client_secret
        refresh_query_dict['refresh_token'] = api_key_data.refresh_token
        refresh_query_dict['grant_type'] = 'refresh_token'

        return refresh_query_dict

    def _store_new_api_keys(self, new_tokens_json, api_key_data):
        '''
        Persists the new API Key Data for the Strava Service
        '''
        access_token = new_tokens_json['access_token']
        api_key_data.access_token = access_token
        self.api_key_mgr.store_data_for_source(self.api_key_name, api_key_data)