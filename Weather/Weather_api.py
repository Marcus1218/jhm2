import os
import requests
from typing import Dict, Union
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_weather(location: str, date: str = None, hour: int = None) -> Union[Dict[str, str], str]:
    api_key = os.getenv('f2300b3f7eef4feabd2142219251601', 'f2300b3f7eef4feabd2142219251601')
    base_url = 'http://api.weatherapi.com/v1'
    if date:
        complete_url = f"{base_url}/history.json?key={api_key}&q={location}&dt={date}"
    else:
        complete_url = f"{base_url}/current.json?key={api_key}&q={location}"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return f"Network error: {e}"

    if 'error' in data:
        return f"Error: {data['error']['message']}"

    if date:
        for hour_data in data['forecast']['forecastday'][0]['hour']:
            if hour_data['time'].endswith(f"{hour:02d}:00"):
                current = hour_data
                break
    else:
        current = data['current']
    location_info = data['location']
    weather_info = {
        'Location': f"{location_info['name']}, {location_info['region']}, {location_info['country']}",
        'Temperature': f"{current['temp_c']}°C",
        'Condition': current['condition']['text'],
        'Humidity': f"{current['humidity']}%",
        'Wind': f"{current['wind_kph']} kph"
    }
    return weather_info

def format_weather_info(weather_info: Dict[str, str]) -> str:
    return '\n'.join(f"{key}: {value}" for key, value in weather_info.items())

def plot_weather_data(weather_data: Dict[str, Dict[str, float]], location: str) -> None:
    labels = list(weather_data.keys())
    wind_speeds = [data['Wind'] for data in weather_data.values()]
    temperatures = [data['Temperature'] for data in weather_data.values()]

    plt.figure(figsize=(10, 5))
    plt.plot(labels, wind_speeds, marker='o', linestyle='-', color='b', label='Wind Speed (kph)')
    plt.plot(labels, temperatures, marker='o', linestyle='-', color='r', label='Temperature (°C)')
    plt.xlabel('Hour')
    plt.ylabel('Value')
    plt.title(f"Weather Data Comparison for {location}")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_minute_wind_speed(weather_data: Dict[str, float], location: str) -> None:
    labels = list(weather_data.keys())
    wind_speeds = list(weather_data.values())

    plt.figure(figsize=(10, 5))
    plt.plot(labels, wind_speeds, marker='o', linestyle='-', color='b', label='Wind Speed (kph)')
    plt.xlabel('Minute')
    plt.ylabel('Wind Speed (kph)')
    plt.title(f"Wind Speed for the Last 2 Hours in {location}")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    location = input("Enter your location: ")
    weather_info = get_weather(location)
    if isinstance(weather_info, str):
        print(weather_info)
    else:
        print(format_weather_info(weather_info))
        weather_data = {}
        for i in range(6):
            date = (datetime.now() - timedelta(hours=i + 1)).strftime('%Y-%m-%d')
            hour = (datetime.now() - timedelta(hours=i + 1)).hour
            previous_weather_info = get_weather(location, date, hour)
            if isinstance(previous_weather_info, str):
                print(previous_weather_info)
            else:
                weather_data[f"{hour}:00"] = {
                    'Wind': float(previous_weather_info['Wind'].split()[0]),
                    'Temperature': float(previous_weather_info['Temperature'].split('°')[0])
                }
        current_wind = float(weather_info['Wind'].split()[0])
        current_temp = float(weather_info['Temperature'].split('°')[0])
        weather_data['Current Hour'] = {'Wind': current_wind, 'Temperature': current_temp}

        # Check for wind shear
        wind_speeds = [data['Wind'] for data in weather_data.values()]
        for i in range(1, len(wind_speeds)):
            if abs(wind_speeds[i] - wind_speeds[i - 1]) > 3:
                print("wind shear is high BE CAREFUL!!!")

        plot_weather_data(weather_data, weather_info['Location'])

        # Fetch and plot wind speed for the last 2 hours in 20-minute intervals
        minute_weather_data = {}
        for i in range(6):
            time_point = datetime.now() - timedelta(minutes=(i + 1) * 20)
            date = time_point.strftime('%Y-%m-%d')
            hour = time_point.hour
            minute = time_point.minute
            previous_weather_info = get_weather(location, date, hour)
            if isinstance(previous_weather_info, str):
                print(previous_weather_info)
            else:
                minute_weather_data[f"{hour:02d}:{minute:02d}"] = float(previous_weather_info['Wind'].split()[0])
        plot_minute_wind_speed(minute_weather_data, weather_info['Location'])

if __name__ == "__main__":
    main()