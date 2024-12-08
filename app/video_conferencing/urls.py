from django.urls import path
from . import views

urlpatterns = [
    path('video_conference/<str:class_name>/', views.video_conference, name='video_conference'),
]
