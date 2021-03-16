import requests
import os
from twilio.rest import Client

API_KEY = "6a76a3d9af68bbda9719e17e4424d6eb"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
LAT = -1.2833
LON = 36.8167
parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:21]

will_rain = False
for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It will rain today. Remember to carry an umbrella ☔☔.",
            from_='+15034064177',
            to='+254707371677'
        )

    print(message.sid)

# You can use PythonAnywhere to automate this.
