from django.shortcuts import render
import datetime
import plop

def home(request):
    example = plop.tab()
    print example
    plop.pprint_tab(example)

    return render(request, "all.html", { "updated_time": datetime.datetime.now(), "laniere_dict": example})
