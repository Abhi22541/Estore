from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('dashboard/', Dashboard.as_view(), name='homepage'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name='login')
    # path('', Registrations.as_view(), name='register')
]