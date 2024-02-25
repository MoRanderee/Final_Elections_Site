from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
   
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')

def save(self, commit=True):
    user = super(SignUpForm, self).save(commit=False)
    user.username = self.cleaned_data['username']
    if commit:
        user.save()
    return user
    

# class NewUserForm(UserCreationForm):
# 	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user