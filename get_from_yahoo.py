import pandas as pd
import numpy as np
import urllib
from yahoo import YahooMapRequest


api_key = ''


def get_lat_lon(address, pref):
    new_address = None
    if address.find(pref) == -1:
        new_address = pref + address
    else:
        new_address = address

    new_address = urllib.parse.quote_plus(new_address, encoding='utf-8')

    n = YahooMapRequest()
    res = n.get(
        '/geoCoder?appid=' + api_key + '&ei=UTF-8&output=json&query=' + new_address
    )
    result = res.json()
    if result['ResultInfo']['Count'] == 0:
        return None
    else:
        return result['Feature'][0]['Geometry']['Coordinates']


if __name__ == '__main__':
    aichi = pd.read_csv('aichi.csv')
    aichi['lat_lon'] = aichi['住所'].apply(lambda x: get_lat_lon(x.strip(), '愛知県'))
