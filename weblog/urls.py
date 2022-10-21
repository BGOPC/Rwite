from django.urls import path
from django.contrib.auth.urls import urlpatterns
del urlpatterns[0]
from . import views
urlpatterns = [
    path("",views.mainView.as_view(), name="home"),
    path("",views.mainView.as_view(), name="home"),
    path("create",views.createView.as_view(), name="create"),
    path("register/",views.signUpView.as_view(), name="signUp"),
    path("login/",views.LoginView.as_view(), name="login"),

]
