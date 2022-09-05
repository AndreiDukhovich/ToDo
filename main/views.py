from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .forms import Form_action, Form_change, RegistrationUser
from .models import Action
import datetime
from django.contrib.auth import authenticate, login

# Create your views here.
def main(request):
    return render(request, 'main/main.html')


def add_action(request):
    error = ''
    if request.method == 'POST':
        form = Form_action(request.POST)
        new_action = form.save(commit=False)
        new_action.person = request.user.username
        new_action.save()
        if form.is_valid():
            form.save()
            return redirect('add_action')
        else:
            error = 'Ой, что-то не так.'
    form = Form_action()
    info_list = Action.objects.filter(person=request.user.username).order_by('-date')
    data = {'form': form, 'error': error, 'actions': info_list}
    return render(request, 'main/create.html', data)

def chenge_complete(request):
    if request.method == 'POST':
        form = Form_change(request.POST)
        new_action = form.save(commit=False)
        new_action.save()
        if form.is_valid():
            form.save()
            return redirect('add_action')
    form = Form_action()
    info_list = Action.objects.filter(person=request.user.username).order_by('-date')
    data = {'form': form, 'actions': info_list}
    return render(request, 'main/create.html', data)

def hui(request):
    return render(request, 'main/hui.html')

def info_task(request, title):
    try:
        info = Action.objects.get(title=title)
        if request.method == 'POST':
            info.complete = True
            info.save()
        form = Form_action()
        data = {'info': info}
        return render(request, 'main/info.html', data)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        return render(request, 'main/dontexiststask.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            u_pass = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username=u_name,
                                password=u_pass)
            login(request, user)
            return redirect('main')
    form = RegistrationUser()
    data = {'form': form}
    return render(request, 'registration/createUser.html', data)    

def today(request):
    h1 = 'Сегодня'
    now = datetime.datetime.now()
    tasks = Action.objects.filter(person=request.user.username).filter(date=now).order_by('-important')
    return render(request, 'main/taskList.html', {'tasks': tasks, 'h1': h1})

def tomorrow(request):
    h1 = 'Завтра'
    now = datetime.datetime.now()
    tomorrow = now.replace(day=1+now.day)
    tasks = Action.objects.filter(person=request.user.username).filter(date=tomorrow).order_by('-important')
    return render(request, 'main/taskList.html', {'tasks': tasks, 'h1': h1})

def important(request):
    h1 = 'Выжное'
    tasks = Action.objects.filter(person=request.user.username).filter(important=True)
    return render(request, 'main/taskList.html', {'tasks': tasks, 'h1': h1})

def tasks_list(request):
    h1 = 'Все твои задачи'
    tasks = Action.objects.filter(person=request.user.username).order_by('-date').order_by('-time').order_by('-important').order_by('complete')
    return render(request, 'main/taskList.html', {'tasks': tasks, 'h1': h1})
