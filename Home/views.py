from django.shortcuts import render
from . models import Clients, Work, Services, Profile

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile})
    

    
