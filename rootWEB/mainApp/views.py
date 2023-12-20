from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

from django.core.paginator import Paginator


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


def QNA(request):
    print('debug >>>> mainApp /QNA')
    return render(request, 'main/QNA.html')


def info(request):
    print('debug >>>> mainApp /info')
    return render(request, 'main/info.html')


