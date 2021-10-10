from django.urls import path

from . import views

urlpatterns = [
    path('', views.reg, name='reg'),
    path('user/<str:username>', views.index, name='index'),
    path('user/chat=<str:room_name>/username=<str:username>', views.room, name='room'),
]
