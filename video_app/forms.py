from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class userRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,required=True,widget = forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder' : 'Enter email' }))
    first_name = forms.CharField(required=True,widget = forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder' : 'Firstname' }))
    last_name = forms.CharField(max_length=100,required=True,widget = forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder' : 'Lastname' }))
    password1 = forms.CharField(required=True,widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder' : 'Enter password' }))
    password2 = forms.CharField(required=True,widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirm password' }))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']

    def save(self,commit=True):
        user = super(userRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.firstname = self.cleaned_data['first_name']
        user.lastname = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user