import requests
import json

def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]
        country = weather_data["sys"]["country"]

        print(f"Weather forecast for {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("Unable to fetch weather forecast.")

def main():
    api_key = "ee68513c98ad003a66771a5ec96123df"  # Replace with your OpenWeatherMap API key
    city = input("Enter the name of the city: ")
    get_weather_forecast(api_key, city)

if __name__ == '__main__':
    main()
