# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
import json
from django.core import serializers
from main.forms import EnterText
from main.models import Chat
from django.contrib.auth.models import User
from datetime import datetime
import logging
import logging.handlers

# Create your views here.

def index(request):
    if request.POST and request.user.is_active:
        name = User.objects.get(username=request.user.username)
        chat = Chat()
        chat.name = name
        chat.text = request.POST['text']
        chat.date = datetime.now()
        chat.save()
        logging.basicConfig(filename='log.txt', level=logging.INFO)
        logging.info(' Date/Time: ' + chat.date.strftime("%Y-%m-%d %H:%M") + '    User: '
                     + chat.name.username + '    Message: ' + chat.text)
        return redirect('index')
    if request.is_ajax():
        date = []
        name = []
        text = []
        data = {'date': date, 'name': name, 'text': text}
        for i in Chat.objects.all()[:50]:
            date.append(i.date.strftime("%Y-%m-%d %H:%M"))
            name.append(i.name.username)
            text.append(i.text)
        return HttpResponse(json.dumps(data))
    return render(request, 'main/index.html', {'text': EnterText()})