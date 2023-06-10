from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'completed')

        def save(self, commit=True, user=None):
            instance = super().save(commit=False)
            instance.user = user
            if commit:
                instance.save()
            return instance
