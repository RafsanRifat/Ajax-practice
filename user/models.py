from django.db import models
from django.forms import ModelForm
# Create your models here.
from django.db import models
from django import forms


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'name',
            'email'
        ]

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not 'Raf' in name:
    #         raise forms.ValidationError("This is not a valid name")
    #     return name
