from django.shortcuts import render
from . models import Clients, Work, Services, Profile

def home(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def send_message(request):
    if request.method == 'POST':
        # Getting user input from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Creating the full email message body
        full_message = f"""A new message has been received from your website contact form.

        Name: {name}
        Email: {email}
        Phone: {phone}
        Message:
        {message}
        """

        # Sending the email using Django's send_mail function
        send_mail(
            subject='New Message from Website',
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Redirecting to a success page after sending
        return redirect('message_sent')

    return render(request, 'contact.html')


    
