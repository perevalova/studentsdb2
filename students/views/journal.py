from django.shortcuts import render
from django.http import HttpResponse

def students_visiting(request):
    visitings = (
        {'id': 1,
        'full_name': u'Перевалова Анастасія',},
        {'id': 2,
        'full_name': u'Рудюк Максим',},
        {'id': 3,
        'full_name': u'Краснобокий Максим',},
        )
    return render(request, 'students/journal.html', {'visitings': visitings})

def students_edit(request, vid):
    return HttpResponse('<h1>Edit Student Visiting %s</h1>' % vid)
