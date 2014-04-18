from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #email = forms.EmailField(max_length=100, required=False)
    class Meta:
        model = User
        #fields = ('username', 'email', 'password')
        ## I really don't need your email and you're safer not sharing it with me
        fields = ('username', 'password')
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post', css_class='btn-primary'))


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')



class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')