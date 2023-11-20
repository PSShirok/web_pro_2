from django.urls import path

from users.views import LogoutView, LoginView, RegisterView, UserUpdateView, generate_new_password, activate_user
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('activate/<str:verify_key>', activate_user, name='activate_user'),
  ]
