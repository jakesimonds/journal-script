import sys
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_temp():

    key = os.environ.get('KEY')
    base_url = "http://api.weatherapi.com/v1"
    q = os.environ.get('ZIPCODE')
    aqi = "no"
    url = f"{base_url}/current.json?key={key}&q={q}&aqi={aqi}"

    response = requests.get(url)
    data = response.json()
    temp = data['current']['temp_f']

    return temp if temp else 'Weather API issue!'