"""
URL configuration for fc_community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from fcuser import views
from fcuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcuser/', include('fcuser.urls')),
    # path('', views.home),
    # 그냥 직방으로 홈으로 갈때는 ''이고, 어디 들렀다가 홈으로 가는거는 '/'
    path('', home),
    path('board/', include('board.urls')),
]
