import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "placeholder"
account_sid = "placeholder"
auth_token = "placeholder"

weather_params = {
    "lat": "placeholder(latittude coordinates)",
    "lon": "placeholder(longitude coordinates)",
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain. Bring a jacket or umbrella",
        from_="placeholder(phonenumber)",
        to="placeholder(phonenumber)"
    )
