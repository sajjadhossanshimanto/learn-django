from django.urls import path
from users.views import sign_up, sign_in, home


urlpatterns = [
    path('sign-up/', sign_up),
    path('log-in/', sign_in),
    path('home/', home, name="home"),

]
