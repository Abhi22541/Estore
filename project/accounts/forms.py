from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Userform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=('username', 'email', 'password', 'password2')

    def save(self, commit=True):
                user = super(Userform, self).save(commit=False)
                user.email = self.cleaned_data['email']
                if commit:
                       user.save()
                return user
