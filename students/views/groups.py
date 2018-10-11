from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1,
        'full_name': u'Перевалова Анастасія',
        'group_name': u'ЗПІ-18'},
        {'id': 2,
        'full_name': u'Рудюк Максим',
        'group_name': u'АТ-22-1м'},
        {'id': 3,
        'full_name': u'Краснобокий Максим',
        'group_name': u'ЗПІ-15'},
        )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request):
    return HttpResponse('<h1>Delete Groups %s</h1>' % gid)

