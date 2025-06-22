from django.shortcuts import render
from . models import Clients, Work, Services, Profile

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile})


from django .contrib.auth.models import User
from django.http import HttpResponse

def create_superuser(request):
    if not User.objects.filter(username="kawsar").exists():
        User.objects.create_superuser('kawsar', 'kawsar@gmail.com', '1234.com')
        return HttpResponse("Superuser created.")
    else:
        return HttpResponse("Superuser already exists.")
