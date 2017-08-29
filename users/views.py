from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import UserProfile
from .forms import LoginForm, RegisterForm

# Create your views here.


# 登陆逻辑
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"msg": "用户名或密码不可为空"})


# 注册逻辑
class RegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            username = request.POST.get("username", "")
            mobile = request.POST.get("mobile", "")
            if UserProfile.objects.filter(Q(email=email) | Q(username=username) | Q(mobile=mobile)):
                return render(request, "register.html", {"msg": "用户名/邮箱/手机已被注册", "register_form": register_form})
            else:
                password_1 = request.POST.get("password_1", "")
                password_2 = request.POST.get("password_2", "")
                if password_1 != password_2:
                    return render(request, "register.html", {"msg": "两次输入密码不相同", "register_form": register_form})
                else:
                    user_profile = UserProfile()
                    user_profile.username = username
                    user_profile.email = email
                    user_profile.mobile = mobile
                    user_profile.set_password(password_1)
                    user_profile.save()
                    return HttpResponseRedirect("/login/")
        else:
            return render(request, "register.html", {"register_form": register_form})


# 登出逻辑
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
