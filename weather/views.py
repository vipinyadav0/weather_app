from django.shortcuts import render
from django.views import View
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def home(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=d71da0aca1d0c06fae26e1b1dc434022"
    city = "Las vegas"
    city_weather = requests.get(url.format(city)).json()
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    form = CityForm()
    
    cities = City.objects.all()
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

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
    