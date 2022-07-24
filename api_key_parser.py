import yaml

class ApiKeyData:
    def __init__(
        self,
        access_token,
        refresh_token=None,
        client_id=None,
        client_secret=None
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret

class ApiKeyParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.api_data = None
        self.load_yaml_file()

    def load_yaml_file(self):
        with open(self.file_name, "r") as stream:
            try:
                self.api_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_data_for_source(self, source):
        if source in self.api_data:
            data = self.api_data[source]
            client_id = data['client_id']
            client_secret = data['client_secret']
            acs_tkn = data['access_token']
            rfrsh_tkn = data['refresh_token']
            return ApiKeyData(acs_tkn, rfrsh_tkn, client_id, client_secret)
        else:
            return None