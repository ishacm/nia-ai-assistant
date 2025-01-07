import requests

def get_weather(location, date):
    api_key = 'your-openweathermap-api-key'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
    response = requests.get(url).json()
    for forecast in response['list']:
        if forecast['dt_txt'].startswith(date):
            return forecast['weather'][0]['description']
    return None