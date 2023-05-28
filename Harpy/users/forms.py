# This class serves to create more fields in the custom form django provides us with.
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User  # Specify the model that this form will interact with
        # The 'name' attributes of the fields that we want to be shown in our form (in order), so that we may easily refer to them in future
        fields = ['username','email','password1','password2']
        
