from django.contrib import admin
from django.urls import path, include
from mainApp     import views
from .views import detect_objects

urlpatterns = [
    path('detect_objects/', detect_objects, name='detect_objects'),
]
urlpatterns = [
    # http://127.0.0.1:8000/
    path("index"             , views.index, name="index"),
    path("joinForm/"    , views.joinForm),
    path("join/"        , views.join),
    path("login/"       , views.login),
    path("logout/"      , views.logout),
    path("main/"        , views.main),
    path("QNA/"         , views.QNA),
    path(""        , views.info),
    path('detect_objects/', detect_objects, name='detect_objects'),

]
