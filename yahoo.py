import requests
import os


class YahooMapRequest:
    base_url = "https://map.yahooapis.jp/geocode/V1"
    headers = {
        'Content-Type': 'application/json',
    }

    def get(self, uri):
        return requests.get(
            self.base_url + uri,
            headers=self.headers
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


