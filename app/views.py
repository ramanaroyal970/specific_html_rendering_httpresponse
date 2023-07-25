from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_1(request):
    return render(request,'first.html')
def second_1(request):
    return render(request,'second.html')
def third_1(request):
    return HttpResponse('<h1><marquee>RAGNOR LATHBROK</h1></marquee>')
