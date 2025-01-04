import requests

def get_weather(location):
    api_key = ('e6cb67306dee4fbfbce32041243011')
    base_url = 'http://api.weatherapi.com/v1/current.json'
    complete_url = f"{base_url}?key={api_key}&q={location}"
    response = requests.get(complete_url)
    data = response.json()
    if 'error' in data:
        return f"Error: {data['error']['message']}"
    current = data['current']
    location = data['location']
    weather_info = {
        'Location': f"{location['name']}, {location['region']}, {location['country']}",
        'Temperature': f"{current['temp_c']}°C",
        'Condition': current['condition']['text'],
        'Humidity': f"{current['humidity']}%",
        'Wind': f"{current['wind_kph']} kph"
    }
    return weather_info
if __name__ == "__main__":
    location = input("Enter your location: ")
    weather_info = get_weather(location)
    for key, value in weather_info.items():
        print(f"{key}: {value}")
