from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    '''
        name of class is very clear and if we want to add new user django use this form class
        to create it with User model that we added before
    '''
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm_password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email','phone_number','fullname')

    
    #this method checks passwords that match or not!!
    def clean_password2(self):
        'we check password 2 because it fill after password1 and always password 1 is not empty in checking'
        
        cd=self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1']!=cd['password2']:
            raise ValidationError('passwords don\'t match!! try again')
        return cd['password2']

    def save(self,commit=True):
        'for set password we must override save method to set then save user ;) '

        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        
        if commit:
            user.save()

        return user
    
class UserChangeForm(forms.ModelForm):
    '''
        this class uses for updating user object like email,fullname and ...
        but for passwords it does not work and must add another for password
    '''
    
    password=ReadOnlyPasswordHashField(help_text='you can change your password with using <a href=\'../password/\'>this form</a>')
    # password=ReadOnlyPasswordHashField(help_text='you can change your password with using <a href="../password/">this form</a>')

    class Meta:
        model=User
        fields=('email','phone_number','fullname','password','is_active','is_admin','last_login')

class UserRegisterForm(forms.Form):
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }),max_length=11)

    fullname=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))

class VerifycodeForm(forms.Form):
    code=forms.IntegerField(widget = forms.TextInput(attrs={
        'class':'form-control'
    }))