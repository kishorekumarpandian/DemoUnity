#Phase1-Unity CMR Software

from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("signup",views.signup, name="signup"),
    path("signin",views.signin, name="signin"),
    path("insert_user",views.insert_user, name="insert_user"),
    path("signout",views.signout, name="signout"),
]