from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('insta_login/', views.insta_login, name='insta_login'),
    # path('snap_login/', views.snap_login, name='snap_login'),
    path('login_api/', views.login_api, name='login_api'),
    path('hdfc_survey/', views.survey, name='survey'),
]
