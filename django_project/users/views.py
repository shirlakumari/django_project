from django.contrib.auth.models import User
from django.shortcuts import render
#redirect module after we created the accoutn
from django.shortcuts import redirect

#module whic check that somethig happed only iff user is login
from django.contrib.auth.decorators import login_required

#import from form to the view to interact
from .forms import UserRegisterForm
from .forms import ProfileUpdateForm
from .forms import UserUpdateForm

#this message is for displaying one time message to templets like accout created message only show one time
from django.contrib import messages
#there are these type of flash messages:
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error

#_______________________________________________________
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#________________________________________________________

# def register(request):
#     #if request method is POST then paas the detail in user form else create new form
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             #for saving our user in data if it is valid
#             form.save()
            
#             #if form is valid then we store the submitted username is cleaned_data dictonary
#             username = form.cleaned_data.get('username')
            
#             #flash message if succes
#             messages.success(request, f'Your account has been created! You are now able to log in')
            
#             #return to blog home templet
#             return redirect('login')
#     else:
#         # if anythig is wrond it create a empty form and does't redirect
#         form = UserRegisterForm()

#     return render(request, 'users/register.html', {'form': form})


# decorataor is used to add funcnality to a function 
@login_required
def profile(request):

    if request.method == 'POST':
        # we send the model in parameter so we can change or use that
        # request.user is current login user
        u_form = UserUpdateForm(request.POST, instance = request.user)
        # reques.POST and request.FILES is passing data in profile update and user update
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
    
        # saving data to database
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            #flash message if succes
            messages.success(request, f'Congratulations, Your profile is updated!')
            
            # if form save then it redirect to profile and save us from reloding
            # because after reloading we get another post request
            return redirect('profile')
    
    else:
        # if request is not POST then it create blanck
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)
