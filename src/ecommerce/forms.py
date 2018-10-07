from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class=': 'form-control',
            'placeholder': 'Your Username'
        }
    ))
    email= forms.EmailField(widget=forms.TextInput(
        attrs={
            'class=':'form-control',
            'placeholder':'Your Email'
        }
    ))
    password=forms.CharField(widget=forms.PasswordInput(
            attrs={
                'placeholder':'Your Password'
            }
        )
    )

    def clean_email(self):
        email= self.cleaned_data.get('email')
        if 'snapp.cab' not in email:
            raise forms.ValidationError('Email has to be snapp.cab')
        return email
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class=': 'form-control',
            'placeholder': 'Your Username'
        }
    ))
    email= forms.EmailField(widget=forms.TextInput(
        attrs={
            'class=':'form-control',
            'placeholder':'Your Email'
        }
    ))
    password=forms.CharField(widget=forms.PasswordInput(
            attrs={
                'placeholder':'Your Password'
            }
        )
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Please re-enter Password'
        }
    ),label='Confirm Password'
    )

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Duplicate Username')
        else:
            return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Duplicate Email')
        else:
            return email

    def clean(self):
        data=self.cleaned_data
        pass1=data.get('password')
        pass2 = data.get('password2')
        if pass1 != pass2:
            raise forms.ValidationError('Passwords must match')
        else:
            return data
