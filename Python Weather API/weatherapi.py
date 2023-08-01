import datetime as dt
import requests

def kel_to_cel_far(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "7aad69acc2856368ef12defd30eb29ef"
CITY = "Belmont, CA"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kel_to_cel_far(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kel_to_cel_far(feels_like_kelvin)

humidity = response['main']['humidity']

description = response['weather'][0]['description']

sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

windspeed = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_fahrenheit:.2f}")
print(f"Current Condition: {description}")

#print(response)