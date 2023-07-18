from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from .models import Query
class SignUpForm(UserCreationForm):
    # class Meta:
    #     model = User
    #     fields = ['username', 'password1', 'password2']
    pass

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['query',]