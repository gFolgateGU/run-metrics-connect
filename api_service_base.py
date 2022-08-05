import requests

class ApiResults:
    def __init__(self, http_status, json_data):
        self.http_status = http_status
        self.json_data = json_data

    def valid(self):
        if self.http_status == 200:
            return True
        return False

class ApiServiceBase:
    def __init__(self):
        pass

    def build_uri(self, uri_base, uri_param_dict):
        uri = uri_base

        for key in uri_param_dict:
            uri += f'{key}={uri_param_dict[key]}&'
        
        # Remove the trailing "&" at the end.
        uri = uri[:-1]

        return uri

    def http_post(self, uri):
        response = requests.post(uri)
        results = ApiResults(response.status_code, response.json())
        return results
    
    def http_get(self, uri):
        response = requests.get(uri)
        results = ApiResults(response.status_code, response.json())
        return results