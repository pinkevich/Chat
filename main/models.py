# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    text = models.CharField(max_length=300, verbose_name='Сообщение')
    date = models.DateTimeField()
    name = models.ForeignKey(User)
    def __unicode__(self):
        return self.name
