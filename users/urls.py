from django.urls import path

from users.views import LogoutView, LoginView, RegisterView, UserUpdateView, generate_new_password
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
#     path('', HomeListView.as_view(), name='home'),
#     path('create/', ProductCreateView.as_view(), name='create_product'),
#     path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
#
  ]
