
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomePage),
    path('login/',views.LoginPage),
    path('',views.SignUpPage),
    path('logout/',views.Logout),
]
