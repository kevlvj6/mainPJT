from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def login(request) :
    print('debug >>>> mainApp /login')
    return render(request, 'main/login.html')