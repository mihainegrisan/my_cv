from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

from django.contrib.auth.decorators import login_required

from .models import Profile

from django.contrib import messages


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section' : 'dashboard'})
@login_required
def images(request):
    return render(request,
                  'account/images.html',
                  {'section' : 'images'})
@login_required
def people(request):
    return render(request,
                  'account/people.html',
                  {'section' : 'people'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            # Instead of saving the raw password entered by the user, we use the set_password() method of the user model that handles encryption to save for safety reasons.
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            # Create the user profile when they register for an account
            Profile.objects.create(user=new_user)

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form' : user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # authenticate() - checks user credentials and returns a User object
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    # sets the user in the current session.
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form' : form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error updating your profile.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
               'user_form' : user_form,
               'profile_form' : profile_form
    }
    return render(request, 'account/edit.html', context)
