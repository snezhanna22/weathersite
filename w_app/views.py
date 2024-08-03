import requests
from datetime import datetime
from django.utils import dateformat
from django.shortcuts import render

from weathersite.apikey import API_TOKEN



def search(request):

    if request.method == "POST":
        form = request.POST['city']
        url = (f"https://api.openweathermap.org/data/2.5/weather?q={form}&units=metric&lang=ru&appid="+ API_TOKEN)
        response = requests.get(url, params=form, timeout=40)
        res = response.json()

        DATE_FORMAT = "d E Y H:i"
        time = dateformat.format(datetime.now(), DATE_FORMAT)

        # pres = res["main"]["pressure"]
        # pressure = pres * 0.75006156

        city_info = {
            "city": res['name'],
            "dt": time,
            "temp": res['main']['temp'],
            "description": res["weather"][0]["description"],
            "wind": res["wind"]["speed"],
            "humidity": res["main"]["humidity"],
            "pressure": res["main"]["pressure"] * 0.75006156,
            "icon": res["weather"][0]["icon"],
        }

        context = {
            "search_city": city_info,
        }

        return render(request, 'w_app/index.html', context)
    return render(request, 'w_app/index.html')
    