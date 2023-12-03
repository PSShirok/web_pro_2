import random

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from users.forms import UserRegisterForm, UserForm
from users.models import User


# Create your views her


class LogoutView(BaseLogoutView):
    pass


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class RegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    permission_required = 'users.add_user'
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_key = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        self.object.is_active = False
        send_mail(
            subject='Поздарвляем с успешной регистрацией, подтвердите адрес электронной почты',
            message=f'Добро пожаловать, подтвердите адрес перейдя по ссылке \n'
                    f'http://127.0.0.1:8000/users/activate/{self.object.user_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]

        )
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    permission_required = 'users.change_user'

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    send_mail(
        subject='Смена пароля',
        message=f'ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]

    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('products:home'))


def activate_user(request, user_key):
    # path = request.path[:8]
    user = User.objects.get(user_key=user_key)

    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
