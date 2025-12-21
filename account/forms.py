from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import BlogUser

class BlogUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=BlogUser
        fields=UserCreationForm.Meta.fields("age","matricnumber")



class BlogUserUpdateForm(UserChangeForm):
    class Meta:
        model=BlogUser
        fields=UserCreationForm.Meta.fields