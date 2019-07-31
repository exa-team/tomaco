from flask import url_for


class BaseTest:
    def get(self, client):
        return client.get(url_for(self.url_name))
