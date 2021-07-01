from django.urls import path
from . import views


# app_name = 'polls'
urlpatterns = [
    path("", views.home, name='index'),
    path('result/<int:question_id>/', views.result, name='result'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('vote/<int:question_id>', views.vote, name='vote')
]
