from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class JournalView(TemplateView):
    template_name = 'students/journal.html'
