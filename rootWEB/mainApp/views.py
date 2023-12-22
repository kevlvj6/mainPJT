
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

# Create your views here.

def login(request):
    print('debug >>>> mainApp /login')
    return render(request, 'main/login.html')


def main(request):
    print('debug >>>> mainApp /main')
    return render(request, 'main/main.html')


def CCTV(request):
    print('debug >>>> mainApp /CCTV')
    return render(request, 'main/CCTV.html')


def QNA(request):
    print('debug >>>> mainApp /QNA')
    return render(request, 'main/QNA.html')

def N_chart(request):
    print('debug >>>> mainApp /N_chart')
    return render(request, 'main/N_chart.html')

def chart(request):
    print('debug >>>> mainApp /chart')
    return render(request, 'main/chart.html')


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()

        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

