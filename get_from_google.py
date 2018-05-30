from googlemapbase import GoogleMapRequest


api_key = ''


if __name__ == '__main__':
    n = GoogleMapRequest()
    new_address = 'Paris'
    result = n.get(
        '/place/autocomplete/json', params={
            'input': new_address,
            'types': 'geocode',
            'key': api_key
        }
    ).json()
    lat_lon = n.get(
        '/place/details/json?placeid=' + result['predictions'][0]['place_id'] + '&key=' + api_key
    ).json()
    print(lat_lon['result']['geometry']['location'])
