from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_2(request):
    return render(request,'third.html')
def second_2(request):
    return render(request,'fourth.html')
def third_2(request):
    return HttpResponse('<h1><marquee>LAGERTH LATHBROK</h1></marquee>')
