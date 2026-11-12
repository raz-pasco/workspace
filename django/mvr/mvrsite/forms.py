from django.contrib.auth.views import PasswordChangeView
from django_password_eye.fields import PasswordEye
from django_password_eye.widgets import PasswordEyeWidget
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django import forms

class CustomPasswordChangeForm(PasswordChangeForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].error_messages['required'] = 'Please enter your new password.'
        self.fields['new_password2'].error_messages['required'] = 'Please confirm your new password.'
        # Customize the 'password_mismatch' error message if needed
        self.error_messages['password_mismatch'] = 'The two password fields did not match. Please try again.'

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_reset_confirm.html' # Use a custom template
    # success_url = reverse_lazy('password_change_done')

