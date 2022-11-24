from django.forms import ModelForm, CharField, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Reseni, Ucebnice

class ReseniForm(ModelForm):
    def __init__(self, *args, priklad, **kwargs):
            super(ReseniForm, self).__init__(*args, **kwargs)
            self.fields["reseni"] = CharField(max_length=200, required=False)

    class Meta:
        model = Reseni
        fields = ('reseni',)

class UcebniceForm(ModelForm):

    class Meta:
        model = Ucebnice
        fields = ('nazev',)

class RegistraceForm(UserCreationForm):
    email = EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistraceForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user