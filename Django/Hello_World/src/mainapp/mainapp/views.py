
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    contacts = ['Kevin', 'Makenna', 'Bear', 'Bob', 'Nick']
    context = {
        'contacts':contacts,
    }
    return render(request, "home.html", context)