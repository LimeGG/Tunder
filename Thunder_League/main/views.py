from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return render(request, 'main/main.html')

def about_page(request):
    return render(request, 'main/about_us.html')