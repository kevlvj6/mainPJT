from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

def login(request) :
    print('debug >>>> mainApp /login')
    return render(request, 'main/login.html')

def main(request) :
    print('debug >>>> mainApp /main')
    return render(request, 'main/main.html')

def QNA(request) :
    print('debug >>>> mainApp /QNA')
    return render(request, 'main/QNA.html')