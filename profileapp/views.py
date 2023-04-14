from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from main.models import PerTask
from main.services import create_daily_periodic_task
from .forms import RegistrationUser, ProfileTimeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from datetime import time as tm
from .services import *

def registration(request, id=False):
    er = ''
    form = RegistrationUser()
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            u_pass = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username=u_name,
                                password=u_pass)
            login(request, user)
            if id:
                bind_acc_with_telegram(request, id)
            return redirect('main')
    data = {'form': form, 'er': er}
    return render(request, 'registration/createUser.html', data)

def telgramconferm(request, id):
    return bind_acc_with_telegram(request, id)  

def login_with_tele_id(request, id):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return bind_acc_with_telegram(request, id)
    form = AuthenticationForm()
    return render(request,'registration/login.html', {'form':form})


def profile_settings(request):
    error = ''
    try:
        instance_time = (PerTask.objects.get(name=request.user.id, action='telegram_daily_message')
                                            .time.isoformat('minutes'))
    except PerTask.DoesNotExist:
        instance_time = ''
    person_info = request.user
    if person_info.email:
        person_email = person_info.email.split('@')
        person_email = person_email[0][:3]+'*'*(len(person_email[0])-3)+'@'+person_email[1]
    else:
        person_email = 'Ваш email не установлен'
    form = ProfileTimeForm({'time': instance_time})
    if request.method == 'POST':
        form = ProfileTimeForm(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data
            if 'dailyAlertTime' in request.POST:
                if not Person.objects.filter(user=request.user).exists():
                    error = 'Ваш телеграм не привязан к аккаунту'
                else:
                    time = post_data.get('time')
                    create_daily_periodic_task(time=time, user_id=request.user.id)
    data = {'form': form, 'error': error, 'person_info': person_info, 'person_email': person_email}
    return render(request, 'registration/profileSettings.html', data)


