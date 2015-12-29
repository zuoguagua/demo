from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
#    return HttpResponse("Learn")
    return render(request,'index.html')


