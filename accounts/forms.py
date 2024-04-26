from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class':"form-control", 'id':"user_name"})
        self.fields['password1'].widget.attrs.update({'class':"form-control", 'id':"pass1"})
        self.fields['password2'].widget.attrs.update({'class':"form-control", 'id':"pass2"})


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         if commit:
#             user.save()
#         return user