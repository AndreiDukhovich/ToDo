from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .forms import *
from .models import Action, Archive, get_next_valid_date
from .services import *
from profileapp.models import Person
'''
from django.db import connection, reset_queries
import time
import functools

def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        
        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(connection.queries)
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func'''

def main(request):
    return render(request, 'main/main.html')


def add_action(request):
    error = ''
    main_form = FormAction()
    if request.method == 'POST':
        main_form = FormAction(request.POST)
        if main_form.is_valid():
            print(main_form.cleaned_data)
            new_action = main_form.save(commit=False)
            new_action.person = request.user
            if not new_action.date:
                date = dt.now().date()
                now_time = dt.now().time()
                if now_time > new_action.time:
                    date += timedelta(days=1)
                new_action.date = get_next_valid_date(date, new_action.period)
            new_action.save()
            return redirect('add_action')
    data = {'main_form': main_form, 'error': error}
    return render(request, 'main/create.html', data)

def info_task(request, id):
    try:
        info = Action.objects.get(id=id)
        if request.method == 'POST':
            return del_or_res_task(request=request, id=id, model_type=Action)
        data = {'info': info}
        return render(request, 'main/info.html', data)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        return render(request, 'main/dontexiststask.html')


def tasks_list(request, filter_param=None, date=None):
    model_type = Action
    html_file = 'taskList.html'
    if filter_param == 'archive':
        model_type = Archive
        html_file = 'archiveList.html'
    data = get_data_to_show_tasks(request=request, filter_param=filter_param, date=date)
    if request.method == 'POST':
        task_id_list = [int(id) for id in list(request.POST)[2:]]
        return del_or_res_task(request=request, id=task_id_list, model_type=model_type) 
    return render(request, f'main/{html_file}', data)


def info_archive_task(request, id):
    try:
        info = Archive.objects.get(id=id)
        if request.method == 'POST':
            return del_or_res_task(request=request, id=id, model_type=Archive)
        data = {'info': info}
        return render(request, 'main/archive_info.html', data)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        return render(request, 'main/dontexiststask.html')


def edit(request, id, loc):
    if loc == 1:
        task = Archive.objects.get(id=id)
        amount_edit_taks = len(request.session.get('edit_list', ''))
    elif loc == 2:
        task = Action.objects.get(id=id)
        amount_edit_taks = len(request.session.get('edit_list', ''))
    error = ''
    if request.method == 'POST':
        if 'edit' in request.POST:
            form = EditForm(request.POST)
            if form.is_valid():
                form_data = form.cleaned_data
                Action.objects.update_or_create(person=task.person, title=task.title,
                defaults={'topic': task.topic, 'discription': task.discription, 'date': form_data.get('date'),
                'time': form_data.get('time'), 'important': form_data.get('important')})
                if loc == 1:
                    task.delete()
                edit_list = request.session.get('edit_list', '')
                if edit_list:
                    request.session['edit_list'] = edit_list[1:]
                    if len(edit_list) > 1:
                        return redirect('edit', loc=loc, id=edit_list[1])
                    else:
                        del request.session['edit_list']
                        return redirect('tasks_list')
                return redirect('tasks_list')
            else:
                error = 'Проверьте веденные данные'
        if 'end' in request.POST:
            del request.session['edit_list']
            return redirect('tasks_list')
    form = EditForm()
    data = {'form': form, 'error': error, 'task': task, 'amount_edit_taks': amount_edit_taks}
    return render(request, 'main/edit.html', data)


def task_for_date(request):
    form = DateForm()
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            return redirect('task_list_with_date', date=form.cleaned_data.get('date'))
    data = {'form': form}
    return render(request, 'main/task_for_date.html', data)

