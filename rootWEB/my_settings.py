DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE 명',
        'USER': 'DB접속 계정명',
        'PASSWORD': 'DB접속용 비밀번호',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SECRET_KEY = "django-insecure-0as*)&ksny73!lwp$-beve1ww**9&a=lr8jlzj6x=+=l$onfcn"  # setting.py 내 SECRET_KEY 사용