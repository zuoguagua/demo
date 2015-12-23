from django.shortcuts import render


import job_list
import systeminfo
# Create your views here.

def home(request):
    return render(request,'home.html')

def jobs(request):
    msg = job_list.job_list()
    #print msg
    return render(request,'jobs.html',{"msg":msg})

def system(request):
    msg = systeminfo.systeminfo()
    return render(request,'system.html',{"msg":msg})
