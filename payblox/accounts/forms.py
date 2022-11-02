from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User


# user=get_user_model()
# print('##############################')
# print(user)
# print('##############################')

class RegisterUser(UserCreationForm):
    email = forms.EmailField(required=True, max_length=105)
    dob=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'email', 'dob', 'username', 'password1', 'password2', 'security_question',
                  'security_answer', 'business_name', 'business_type', 'dba', 'monthly_volume']
        # widgets = {'email': forms.EmailInput(attrs={'placeholder':'Enter Email'}), 'username': forms.TextInput(attrs={'placeholder':'Enter Username'}),
        #            'first_name': forms.TextInput(attrs={'placeholder':'Enter First Name'}),
        #            'last_name': forms.TextInput(attrs={'placeholder':'Enter Last Name'}),
        #            'password1': forms.PasswordInput(attrs={'placeholder':'Enter Password'}),
        #            'password2': forms.PasswordInput(attrs={'placeholder':'Retype Password'})}
