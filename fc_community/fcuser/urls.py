from django.urls import path
from . import views

# 위에서 만든 view.py의 register라는 함수를 사용
urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
