from django.shortcuts import render
import datetime

def home(request):
    return render(request, "main.html", { "updated_time": datetime.datetime.now() })
