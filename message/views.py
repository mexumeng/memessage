from django.shortcuts import render
from message.models import Message

# Create your views here.


def index(request):
    return render(request, 'index.html', {
    })


def submessage(request):
    msgs = Message.objects.all()[:2]
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone_num = request.POST.get('address', '')
    mess = request.POST.get('message', '')
    if name != '':
        msg = Message()
        msg.name = name
        msg.email = email
        msg.phone_num = phone_num
        msg.messages = mess
        msg.save()
    return render(request, 'show.html', {
        'msgs': msgs,

    })