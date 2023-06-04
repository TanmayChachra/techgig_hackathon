# Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

import sys
import requests
import json
import argparse

# function to get current weather

def current_weather(city):
    api_key = 'd5c9e7321c866988a9ab571ffc2e6526'

    #get city coordinates
    get_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}'
    response_city = requests.get(get_city)

    if response_city.status_code == 200:
        data_city = json.loads(response_city.text)
        city_lat = data_city[0]["lat"]
        city_lon = data_city[0]["lon"]
    else:
        return f'Could not find city {city}'
    
    # get city weather
    get_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={city_lat}&lon={city_lon}&appid={api_key}"
    response_weather = requests.get(get_weather)

    if response_weather.status_code == 200:
        data_weather = json.loads(response_weather.text)
        weather = data_weather["weather"][0]["description"]
        temperature = data_weather["main"]["temp"]
    else:
        return f'Could not find weather for {city}'
    
    #convert temperature from Kelvin to Celsius
    temperature = round((temperature - 273.15),2)
    return f"The weather in {city} is {weather} with a temperature of {temperature} degrees Celsius."             #returning the weather of the city , here github copilot helped me to write the code and also parse the data from the api

# To run the script from the command line

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the current weather for a city.")
    parser.add_argument("--city", type=str, help="The name of the city to get the weather for.")
    args = parser.parse_args()

    sys.stdout.write(current_weather(args.city))

#thank you