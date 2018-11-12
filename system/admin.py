from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from system.models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileAdmin(admin.ModelAdmin):
    form = UserForm

admin.site.register(Profile, ProfileAdmin)
