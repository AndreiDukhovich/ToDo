from datetime import datetime as dt, time as timeClass, date as dateClass, timedelta
from django.shortcuts import redirect, render
from typing import Union
from profileapp.models import Person
from .models import Action, Archive, PerTask
from django.http.response import HttpResponseRedirect
from json import dumps

def del_or_res_task(request, id: Union[int, list], model_type: Union[Action, Archive]) -> HttpResponseRedirect:
    '''Delete or change task.'''
    redirect_fun = redirect(request.META.get('HTTP_REFERER'))
    if model_type is Action:
        loc = 2
    elif model_type is Archive:
        loc = 1
    if isinstance(id, int):
        id = [id]
        if model_type is Action:
            redirect_fun = redirect('tasks_list')
        elif model_type is Archive:
            redirect_fun = redirect('task_list_with_param', filter_param='archive')
    if 'com' in request.POST:
        complete_task(id)
        return redirect_fun
    if 'del' in request.POST:
        delete_task(model_type, id)
        return redirect_fun
    if 'res' in request.POST:
        request.session['edit_list'] = id
        return redirect('edit', loc=loc, id=id[0])

def get_task_data_based_on_date(username, date: Union[dt, str], model=Action):
    if date == 'all_date':
        data = (model.objects.select_related('person')
                    .filter(person__username=username))
    else:
        data = (model.objects.select_related('person')
                        .filter(person__username=username)
                        .filter(date=date))
    if model == Archive:
        return data
    return data.order_by('-important')

def get_data_to_show_tasks(request, filter_param: str, date=None) -> dict:
    '''Return dictionary with data queryset about tasks and header for HTML page.
    If date not None, it must be date class.'''
    print(filter_param)
    if filter_param == 'today':
        h1 = 'Сегодня'
        today = dt.now()
        tasks = get_task_data_based_on_date(username=request.user.username, 
                                            date=today)
    elif filter_param == 'tomorrow':
        h1 = 'Завтра'
        today = dt.now()
        tomorrow = today + timedelta(days=1)
        tasks = get_task_data_based_on_date(username=request.user.username, 
                                            date=tomorrow)
    elif filter_param == 'important':
        h1 = 'Выжные'
        tasks = Action.objects.filter(person=request.user).filter(important=True)
    elif filter_param == 'archive':
        h1 = 'Архив'
        tasks = Archive.objects.filter(person=request.user).order_by('-date', '-time')
    elif date:
        h1 = '.'.join(reversed(date.split('-')))
        tasks = get_task_data_based_on_date(username=request.user.username, 
                                            date=date)
    else:
        h1 = 'Все задачи'
        tasks = Action.objects.filter(person=request.user).order_by('-date', '-time', '-important')
    return {'tasks': tasks, 'h1': h1}


def create_daily_periodic_task(time:timeClass, user_id: int):
    date = dt.now().date()
    if dt.now().time() > time:
        date += timedelta(days=1)
    
    PerTask.objects.update_or_create(name=f'{user_id}', period='ever',
                defaults={'action': 'telegram_daily_message',
                'time': time,
                'date': date,
                'kwargs': dumps({"user_id": f'{user_id}',
                            'time': f'{time}'})}
                )

   
def complete_task(id):
    tasks = Action.objects.select_related('person', 'topic').filter(id__in=id)
    for task in tasks:
        task.create_archive_task()
    PerTask.objects.filter(name__in=id).delete()
    tasks.delete()

def delete_task(model_type, id):
    tasks = model_type.objects.select_related('person', 'topic').filter(id__in=id).delete()
    if model_type is Action:
        PerTask.objects.filter(name__in=id).delete()