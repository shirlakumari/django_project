from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.fields import ImageField
from .models import Profile

class UserRegisterForm(UserCreationForm):
    #default parameter is required == true you can change parameter that email is required or not
    # create a email field
    email = forms.EmailField()

    # nOTE::vthis class and its method has predefind name so don't change
    class Meta:
        #model which we want to interact with this form whic is user
        # whenevern this form validate its create new user
        model = User

        #feilds which we want to be shown in our registration form with order
        fields = ['username', 'email', 'password1', 'password2']


# we are goona create model form which is allow us to create a form that 
# will work with specific database model
# here we want a update form whic user can use to update its info
class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()

    class Meta:
        model = User
        
        # we are not gonna do for password
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # we have to set our model here
        model = Profile
        fields = ['dp']