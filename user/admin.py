from django.contrib import admin

# Register your models here.
from django import forms

from .models import (
    Profile
)


class UserCreationForm(forms.ModelForm):
    description = forms.CharField(label='description', widget=forms.Textarea, required=False)
    class Meta:
        model = Profile
        fields = ('gender', 'age', 'occupation')


class WatchAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ('user', 'gender', 'age', 'occupation')


admin.site.register(Profile, WatchAdmin)
