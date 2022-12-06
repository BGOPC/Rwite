from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
    first_name = forms.CharField(label="", error_messages={
        'required': 'Please Enter your FirstName'
    }, max_length=255, widget=forms.TextInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "FirstName",
    }))
    last_name = forms.CharField(label="", error_messages={
        'required': 'Please Enter your LastName'
    }, max_length=255, widget=forms.TextInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "LastName"
    }))

    username = forms.CharField(label="", error_messages={
        'required': 'Please Enter your nickname'
    }, max_length=255, widget=forms.TextInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "NickName"
    }))
    email = forms.EmailField(label="", error_messages={
        'required': 'Please Enter your Email'
    }, max_length=255, widget=forms.EmailInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "Email"
    }))
    password1 = forms.CharField(label="", error_messages={
        'required': 'Please Enter your password'
    }, max_length=255, widget=forms.PasswordInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(label="", error_messages={
        'required': 'Please ReEnter your password'
    }, max_length=255, widget=forms.PasswordInput(attrs={
        "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
        "placeholder": "Password"
    }))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "last_name", "first_name"]


class LoginForm(AuthenticationForm):
    username = UsernameField(label="", error_messages={
        'required': 'Please enter your nickname'
    }, widget=forms.TextInput(attrs={'autofocus': True, "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                                     "placeholder": "NickName"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', "class": "appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                                          "placeholder": "NickName"
                                          }),
    )
