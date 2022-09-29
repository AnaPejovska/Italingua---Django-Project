"""Domasna_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Italingua.views import home, test, lectures, profile, practice, congratulations, forum, choose, quiz, addQuestion, reply, replies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('test/', test, name='test'),
    path('lectures/', lectures, name='lectures'),
    path('profile/', profile, name='profile'),
    path('practice/', practice, name='practice'),
    path('congratulations/', congratulations, name='congratulations'),
    path('forum', forum, name='forum'),
    path('choose', choose, name='choose'),
    path('quiz', quiz, name='quiz'),
    path('addQuestion', addQuestion, name='addQuestion'),
    path('reply', reply, name='reply'),
    path('replies', replies, name='replies'),
]
