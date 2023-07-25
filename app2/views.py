from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_3(request):
    return render(request,'fifth.html')
def second_3(request):
    return render(request,'sixth.html')
def third_3(request):
    return HttpResponse('<h1><marquee>BJORN IRONSIDE</h1></marquee>')
