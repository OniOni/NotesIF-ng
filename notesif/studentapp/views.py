from django.shortcuts import render
import datetime

def home(request):
    return render(request, "all.html", { "updated_time": datetime.datetime.now(), "profile": request.user.get_profile() })
