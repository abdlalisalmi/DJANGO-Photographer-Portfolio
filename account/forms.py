from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Account



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user', 'avatar', 'full_name', 'boi',
                  'date_of_birth', 'facebook', 'instagram', 'twitter']
