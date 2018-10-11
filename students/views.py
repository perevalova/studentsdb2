from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    return render(request, 'students/students_list.html', {})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# def students_visiting(request, sid):
    # return HttpResponse('<h1>Students Visiting %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    return render(request, 'students/groups.html', {})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request):
    return HttpResponse('<h1>Delete Groups %s</h1>' % gid)

def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Анастасія',
        'last_name': u'Перевалова',
        'ticket': 341,
        'image': 'img/me.jpeg'},
        {'id': 2,
        'first_name': u'Максим',
        'last_name': u'Рудюк',
        'ticket': 156,
        'image': 'img/rud.jpg'},
        {'id': 3,
        'first_name': u'Максим',
        'last_name': u'Краснобокий',
        'ticket': 245,
        'image': 'img/kras.jpg'},
        )
    return render(request, 'students/students_list.html',
        {'students': students})

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
    return render(request, 'students/groups.html',
        {'groups': groups})
