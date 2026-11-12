
from django_password_eye.widgets import PasswordEyeWidget
from django.contrib.auth.forms import PasswordResetForm
from django import forms

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example of adding custom CSS classes or attributes to the email field
        # self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
        new_password1 = PasswordEye(
            widget=PasswordEyeWidget(attrs={'class': 'form-control', 'placeholder': 'Enter new password'})
        )

        new_password1 = PasswordEye(
            widget=PasswordEyeWidget(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
        )

