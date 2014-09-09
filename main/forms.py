from django.forms import ModelForm
from main.models import Chat

class EnterText(ModelForm):
    class Meta:
        model = Chat
        fields = ['text']