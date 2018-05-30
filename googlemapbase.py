import requests
import os


class GoogleMapRequest:
    base_url = "https://maps.googleapis.com/maps/api"
    headers = {
        'Content-Type': 'application/json',
    }

    def get(self, uri, params=None):
        return requests.get(
            self.base_url + uri,
            headers=self.headers,
            params=params
        )

    def post(self, uri, body):
        return requests.post(
            self.base_url + uri,
            str(body).encode('utf-8'),
            headers=self.headers
        )

    def put(self, uri, body):
        return requests.put(
            self.base_url + uri,
            str(body).encode('utf-8'),
            headers=self.headers
        )

    def patch(self, uri, body):
        return requests.patch(
            self.base_url + uri,
            str(body).encode('utf-8'),
            headers=self.headers
        )


