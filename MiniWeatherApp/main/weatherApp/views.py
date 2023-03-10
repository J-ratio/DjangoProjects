import urllib.request

from django.shortcuts import render
import json
from urllib import request

# Create your views here.

def index(request):

    if request.method == "POST":
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

        list_of_data = json.loads(source)

        data = {
            'country_code': str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)

    else:
        data = {}

    return render(request, "weatherApp/index.html", data)
