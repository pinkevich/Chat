from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': PasswordInput,
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': PasswordInput,
        }