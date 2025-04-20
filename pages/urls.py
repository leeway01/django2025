"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'   # ← 네임스페이스 선언

urlpatterns = [
    # 메인 페이지
    path('', views.mainpage, name='main'),
    path('company/', views.company, name='company'),
    path('product/', views.product, name='product'),
    path('guide/', views.guide, name='guide'),
    path('news/', views.news, name='news'),
    path('event/', views.event, name='event'),
    path('support/', views.support, name='support'),
]
