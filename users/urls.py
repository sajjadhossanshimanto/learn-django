from django.urls import path
from users.views import sign_up, sign_in, home, sign_out


urlpatterns = [
    path('sign-up/', sign_up),
    path('log-in/', sign_in, name='login'),
    path('home/', home, name="home"),
    path('logout/', sign_out, name="logout"),


]
