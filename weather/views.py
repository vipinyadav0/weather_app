from django.shortcuts import render
from django.views import View
import requests
from .models import City
from .forms import CityForm
from decouple import config
# Create your views here.


def home(request):
    API= config('API_KEY')

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    cities = City.objects.all()
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city, API)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) 

    


    context = {
        'weather_data' : weather_data,
        'form': form
}
    return render(request, 'weather/index.html', context)
