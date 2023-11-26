import sys
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather():
        try: 
            key = os.environ.get('KEY')
            base_url = "http://api.weatherapi.com/v1"
            q = os.environ.get('ZIPCODE')
            aqi = "no"
            url = f"{base_url}/current.json?key={key}&q={q}&aqi={aqi}"

            response = requests.get(url)
            data = response.json()

            return data

        except Exception as e:
            print("get_weather() Weather API issue!!")
            return None


def get_temp(weather_data):
    try:
        temp = weather_data['current']['temp_f']
        return temp
    except Exception as e:
        print("get_temp() Weather API issue!!")
        return "Weather API either not set up or broken. Consider journalling about any disappointment you might be feeling right now."