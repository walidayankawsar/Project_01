from django.shortcuts import render, redirect
from . models import Clients, Work, Services, Profile, Social
from django.contrib import messages
from django.core.mail import send_mail
from . forms import ContactForm
from django.conf import settings

def mainpage(request):
    client = Clients.objects.all()
    work = Work.objects.all()
    services = Services.objects.all()
    profile = Profile.objects.first()
    links = Social.objects.first()
    return render(request, 'index.html', {'clients':client,'works':work,'service':services, 'profile':profile, 'link':links})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            subject = "New Contact Message"
            message = [
                f"Name: {contact.name}",
                f"Email: {contact.email}",
                f"Phone: {contact.phone}",
                "Message:",
                contact.message  # user লিখা message
            ]

            # সব lines একসাথে যোগ করতে চাইলে
            message = "\n".join(message)




            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )


            messages.success(request, "Your message sent successfully.")
            return redirect('mainpage')
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = ContactForm()
    return redirect('contact')


    



