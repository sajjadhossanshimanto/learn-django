from django.urls import path
from users.views import sign_up, sign_in, home, sign_out, activate_user, admin_dashboard, assign_rule, group_list


urlpatterns = [
    path('sign-up/', sign_up),
    path('log-in/', sign_in, name='login'),
    path('home/', home, name="home"),
    path('logout/', sign_out, name="logout"),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/', admin_dashboard, name="admin-dashboard"),
    path('admin/<int:user_id>/assign-role/', assign_rule),
    path('admin/group-list/', group_list),
]
