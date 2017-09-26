from django import forms

from django.contrib.auth.models import User

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    
    class Meta:
    
        model = User
        fields = ('username', 'first_name', 'email')
        
    def clean_password_confirm(self):
        cd = self.cleaned_data
        
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Passwords don\'t match.')
        
        return cd['password_confirm']


class UserEditForm(forms.ModelForm):
    
    class Meta:
    
        model = User
        fields = ('first_name', 'last_name', 'email')
        

class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        
        model = Profile
        fields = ('birth', 'photo')
