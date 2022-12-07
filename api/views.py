from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, WeatherSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.views import View
import requests
from .models import *


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# cities = ['Madison',
# 'Manchester',
# 'Marina',
# 'Marysville',
# 'McAllen',
# 'McHenry',
# 'Medford',
# 'Melbourne',
# 'Memphis',
# 'Merced',
# 'Mesa',
# 'Mesquite',
# 'Miami',
# 'Milwaukee',
# 'Minneapolis',
# 'Miramar',
# 'Mission Viejo',
# 'Mobile',
# 'Modesto',
# 'Monroe',
# 'Monterey',
# 'Montgomery',
# 'Moreno Valley',
# 'Murfreesboro',
# 'Murrieta',
# 'Muskegon',
# 'Myrtle Beach',
# 'Naperville',
# 'Naples',
# 'Nashua',
# 'Nashville',
# 'New Bedford',
# 'New Haven',
# 'New London']

cities=['Naples', 'New London']

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.shortcuts import render

def index(request):
    context = []
    for city in cities:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d71da0aca1d0c06fae26e1b1dc434022'

        city = city

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }

        context.append(weather)
    print(context)
    print(Test.objects.all())
    return render(request, 'index.html', {'context':context}) #returns the index.html template

class WeatherViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class IndexView(View):
    def get(self, request):
        context = []
        for city in cities:
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d71da0aca1d0c06fae26e1b1dc434022'

            city = city

            city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon'],
                'humidity': city_weather['main']['humidity'],
                'pressure': city_weather['main']['pressure'],
                'country': city_weather['sys']['country'],
                'sunrise': city_weather['sys']['sunrise'],
                'sunset': city_weather['sys']['sunset'],
                'windspeed': city_weather['wind']['speed']
            }
            context.append(weather)
        return render(request, 'index.html', {'context':context}) #returns the index.html template
