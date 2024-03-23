import os
import requests
from notion_client import Client

# OpenWeather API Settings
openweather_api_key = "05b875973e88059b36fc847c2e0d74f4" 
city = "College Station"  
state = "Texas" 
country = "US"  
base_url = "https://api.openweathermap.org/data/2.5/weather?"

notion = Client(auth="secret_uiMuV0x2ugBWB6j4g8mqZ55DiuF3SklSmUCneRf1mTo") 
# Notion Authentication
#notion = Client(auth=os.environ["587e2098d85142aab90e5b6e25cb3ce6"]) 
database_id = "587e2098d85142aab90e5b6e25cb3ce6" 

def fetch_weather_data():
    weather_url = f"{base_url}q={city},{state},{country}&appid={openweather_api_key}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("Error fetching weather data") 

def update_notion_weather(weather_data):
    notion.pages.create(parent={"database_id": database_id}, properties={
        "City": {"title": [{"type": "text", "text": {"content": city}}]}, 
        "Temperature": {"number": weather_data["main"]["temp"]}, 
        "Wind Speed": {"number": weather_data["wind"]["speed"]},
        "Humidity": {"number": weather_data["main"]["humidity"]},
        "Description": {"rich_text": [{"type": "text", "text": {"content": weather_data["weather"][0]["description"]}}]}
    })

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    update_notion_weather(weather_data) 
