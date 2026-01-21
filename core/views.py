
from django.http import HttpResponse
from django.shortcuts import render

# Postoji funkcija home koja prikazuje nekakvu poruku "Hello world"
# Gde se prikazuje ova funkcija?
def home(request):
    return render(request, 'index.html', status=200)

def about(request):
    return HttpResponse("An error happened while serving this page", status=404)

def product(request, name):
    return HttpResponse(f'This is {name}')

def user(request, userId):
    return HttpResponse(f'This is user {userId}')