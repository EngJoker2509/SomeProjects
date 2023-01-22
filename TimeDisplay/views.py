from django.shortcuts import render
from time import strftime,gmtime

def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time1": strftime("%b %d, %Y",gmtime()),
        "clock":strftime("%H:%M %p",gmtime())
    }
    return render(request,'time_display.html', context)