from random import randint

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import UserRegisterForm, UserLoginForm
from .models import MyUser, InviteCode


# Create your views here.
def hello(request):
    if request.user.is_authenticated():
        return render(request, 'hello.html')
    return render(request, 'hello.html')


@login_required
def user_index(request):
    if request.user.is_authenticated():
        user = request.user
        total_load = user.ss_up_throught + user.ss_down_throught
        percent = float(total_load)/float(user.ss_max_throught)*100.0
        return render(request, 'index.html', {'current_user': request.user,
                                              'total_load': total_load, 'percent': percent})
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = email[:email.find('@')]
            last_user_port = get_last_user_port()
            ss_port = last_user_port + randint(2, 7)
            ss_password = randint(10000, 99999)
            user = MyUser.objects.create_user(username=username,
                                              email=email,
                                              password=form.cleaned_data['password'],
                                              ss_port=ss_port,
                                              ss_password=ss_password)
            # Shadowsocks.objects.create(ss_port=ss_port, ss_password=ss_password, user=user)
            InviteCode.objects.filter(code=form.cleaned_data['invite_code']).delete()
            return redirect(reverse(user_index))
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = email[:email.find('@')]
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse(user_index))
                else:
                    print 'user not active!'
            else:
                return render(request, 'login.html', {'form': form, 'password_is_wrong': True})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'password_is_wrong': False})


def user_logout(request):
    logout(request)
    return redirect(reverse(hello))


def get_last_user_port():
    if MyUser.objects.count() == 0:
        return 10000
    else:
        return MyUser.objects.order_by('-id').first().ss_port
