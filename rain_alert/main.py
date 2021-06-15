import requests
from decouple import config

api_key = config('API_KEY')
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT =13.756331
MY_LONG =100.501762
parameters={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code)<700:
        will_rain = True

if will_rain:
    #implement send message if you want!!!
    print("Bring an umbrella with you!")

