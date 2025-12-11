import os
import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')
        
        api_key = os.environ.get('WEATHER_API_KEY')
        
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

        try:
            response = requests.get(url)
            data = response.json()

            if 'error' not in data:
                weather_data = {
                    'city': data['location']['name'],
                    'country': data['location']['country'],
                    'temperature': data['current']['temp_c'],
                    'description': data['current']['condition']['text'],
                    'icon': 'https:' + data['current']['condition']['icon'],
                }
            else:
                error_message = data['error']['message']
        
        except Exception as e:
             error_message = "Error connecting to Weather API"

    return render(request, 'weather/index.html', {
        'weather_data': weather_data, 
        'error_message': error_message
    })