from django.shortcuts import render
from . models import Clients, Work, Services, Profile, MediaFile
import base64

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile})
    




def handle_upload(request):
    if request.method =='POST':
        uploaded_file = request.FILES['media-file']
        file_content = uploaded_file.read()
        encoded_string = base64.b64encode(file_content).decode('utf-8')


        from .models import MediaFile
        MediaFile.objects.create(
            filename=uploaded_file.name,
            file_data=encoded_string
        )
        return HttpResponse("Uploaded and saved successfully.")
    
