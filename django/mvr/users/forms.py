from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_password_eye.widgets import PasswordEyeWidget
from django_password_eye.fields import PasswordEye

# Customize the registration form
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="User name", # Custom label
        widget=forms.TextInput(attrs={
            # 'class': 'form-control',
            'class': 'form-signin',
            'placeholder': 'Username'
        })
    )

    email = forms.EmailField(
        label="Your Email Address", # Custom label
        widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
                'autocomplete': 'off'
        })
    )

    # Override the password field with PasswordEye
    password1 = PasswordEye(
        label="Password", # Custom label
        widget=PasswordEyeWidget(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    # Override the password field with PasswordEye
    password2 = PasswordEye(
        label="Confirm password", # Custom label
        widget=PasswordEyeWidget(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm'
        })
    )

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2', )


# Customize the login form with django eye
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-signin',
            'placeholder': 'Username'
        })
    )

    # Override the password field with PasswordEye
    password = PasswordEye(
        widget=PasswordEyeWidget(attrs={
            'class': 'form-control form-signin',
            'placeholder': 'Password'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages['required'] = 'A valid username is required.'
        self.fields['password'].error_messages['required'] = 'Your password is required.'
