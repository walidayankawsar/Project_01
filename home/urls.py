from django.urls import path
from . import views
from .views import send_message
from django.http import HttpResponse


urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('send-message/', send_message, name='send_message'),
    path('message-sent/', lambda r: HttpResponse("Message sent successfully!"), name='message_sent'),
]


