from django.shortcuts import render
from django.http import HttpResponse

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
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# def students_visiting(request, sid):
	# return HttpResponse('<h1>Students Visiting %s</h1>' % sid)

