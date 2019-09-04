from .settings import PORTAL_URL


def students_proc(request):
    return {'PORTAL_URL': PORTAL_URL}


def site_creator(request):
    context = {'creator': 'https://perevalova.herokuapp.com'}

    return context