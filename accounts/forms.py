from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password'
        ]

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        error_messages={
            'required': 'This field must not be empty',
        },
        min_length=4, max_length=150,
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Emali'}),
        error_messages={'required': 'E-mail is required'},
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        error_messages={'required': 'Please, repeat your password'},
        )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        error_messages={'required': 'Please, repeat your password'})

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = CustomUser.objects.filter(email=email)

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid'
                )  # noqa
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        exists = CustomUser.objects.filter(username=username)

        if exists:
            raise ValidationError(
                'Username is already in use', code='invalid'
                )  # noqa
        return username

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError('Password and Password2 must be equal', code='invalid')  # noqa   
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': password_confirmation_error,
            })
