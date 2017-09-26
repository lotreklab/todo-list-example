# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):

    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
                  
                  
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            
            profile = Profile.objects.create(user=new_user)
            
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        
    else:
        form = UserRegistrationForm(request.POST)
        
    return render(request,
                  'account/register.html',
                  {'form': form})
                      
                      
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
            
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
