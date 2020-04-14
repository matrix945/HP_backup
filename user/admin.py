from django.contrib import admin

# Register your models here.
from django import forms

from .models import (
    Profile
)


class UserCreationForm(forms.ModelForm):
    # full_name = forms.CharField(label='用户名字', widget=forms.TextInput)
    # username = forms.CharField(label='登录帐户', widget=forms.TextInput)
    # phone = forms.CharField(label='联系电话', widget=forms.TextInput)
    description = forms.CharField(label='description', widget=forms.Textarea, required=False)
    # email = forms.CharField(label='电子邮箱', widget=forms.EmailInput)
    # is_teacher = forms.CharField(label='老师', widget=forms.CheckboxInput)
    # is_parent = forms.CharField(label='家长', widget=forms.CheckboxInput)
    # is_principal = forms.CharField(label='校长', widget=forms.CheckboxInput)
    class Meta:
        model = Profile
        fields = ('gender', 'age', 'occupation')


class WatchAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ('user', 'gender', 'age', 'occupation')


admin.site.register(Profile, WatchAdmin)
