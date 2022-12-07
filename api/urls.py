from django.urls import path, include
from rest_framework import routers
from .views import *
from .serializers import *



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'weather', WeatherViewSet, basename='weather')


# router.register(r'example', ExampleView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('index/',IndexView.as_view())
]

