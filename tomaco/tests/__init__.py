import json
from flask import url_for


class BaseTest:
    def get(self, client):
        return client.get(url_for(self.url_name))

    def post(self, client, data):
        return client.post(
            url_for(self.url_name),
            data=json.dumps(data),
            content_type="application/json",
        )
