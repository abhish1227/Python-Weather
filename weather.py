import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


# def get_current_weather():
#     print('\n***Get Current Weather***\n')
#     city = input('\nEnter city name: ')
    
    
#     request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric"
    
#     # print(f"Request URL: {request_url}")
    
#     weather_data = requests.get(request_url).json()
    
#     # pprint(weather_data)
#     print(f"\nCurrent Weather for {city}: ")
#     print(f"\nTemperature: {weather_data['main']['temp']}°C")
#     print(f"\nHumidity: {weather_data['main']['humidity']}%")
#     print(f"\nFeels Like: {weather_data['main']['feels_like']}°C and {weather_data['weather'][0]['description']}.\n")
    
def get_current_weather(city):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n***Get Current Weather***\n')
    city = input('\nEnter city name: ')
    
    
    
    
    weather_data = get_current_weather(city)
    
    print(f"\nCurrent Weather for {city}: ")
    print(f"\nTemperature: {weather_data['main']['temp']}°C")
    print(f"\nHumidity: {weather_data['main']['humidity']}%")
    print(f"\nFeels Like: {weather_data['main']['feels_like']}°C.\n")