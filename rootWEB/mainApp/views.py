
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

from django.core.paginator import Paginator

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

# Create your views here.

def index(request) :
    print('debug >>> mainApp/index')
    # 로그인 세션 유무에 따라서 서로 다른 화면을 렌더할 수 있어야 함
    if request.session.get('session_user_id') :
        print('debug >>> session exits')
        return render(request, 'main/main.html')

    return render(request, 'main/index.html')

def joinForm(request) :
    print('debug >>> mainApp/joinForm')
    return render(request, 'main/join.html')

def join(request) :
    print('debug >>> mainApp/join')
    id   = request.POST.get('id')
    pwd  = request.POST.get('pwd')
    name = request.POST.get('name')
    print('debug params >>>> ',id, pwd, name)

    # SQL : INSERT INTO User_tbl values(?, ?, ?, ?, ?)
    # ORM : class == table, save()
    user = User_tbl(user_id   = id,
                    user_pwd  = pwd,
                    user_name = name,
                    user_img  = 'boy.jpg')
    user.save()
    return redirect('index')

def login(request) :
    print('debug >>> mainApp/login')
    id   = request.POST.get('id')
    pwd  = request.POST.get('pwd')
    print('debug params >>>>' , id, pwd)
    # SQL : select user_id, select user_pwd, user_name from usr_rbl where
    # OMR : class(instance) == table
    instance = User_tbl.objects.get(user_id = id, user_pwd = pwd)
    print('debug ResultSet >>>' , instance)

    # context 에 심는 일반 데이터는 렌더링되는 페이지에서만 사용이 가능
    # context 에 세션(session)을 심으면 모든 Templates 페이지에서 사용이 가능
    # 근데 django 는 세션에 객체를 못 심어서 따로 작업해야 함
    request.session['session_name']    = instance.user_name
    request.session['session_img']     = instance.user_img
    request.session['session_user_id'] = instance.user_id
    # context 에 세션을 담는 작업
    context = {}
    # context['name']    = request.session['session_name']
    # context['img']     = request.session['session_img']
    # context['user_id'] = request.session['session_user_id']
    # context = {'userInfo': instance }
    return render(request, 'main/main.html', context)

def logout(request):
    print('debug >>> mainApp/logout, redirect index')
    # 명시적인 로그아웃으로 서버가 관리하는 세션을 clear 작업 필요
    # 그 후 렌더가 아닌 리다이렉트를 통해 첫 페이지로 이동
    request.session['session_name']    = {}
    request.session['session_img']     = {}
    request.session['session_user_id'] = {}
    request.session.flush()
    return redirect('index')

def main(request):
    print('debug >>>> mainApp /main')
    return render(request, 'main/main.html')


def CCTV(request):
    print('debug >>>> mainApp /CCTV')
    return render(request, 'main/CCTV.html')


def QNA(request):
    print('debug >>>> mainApp /QNA')
    return render(request, 'main/QNA.html')


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

@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()  # VideoCamera 인스턴스 생성
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        print("에러입니다")
        pass