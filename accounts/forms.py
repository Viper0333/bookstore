from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Senha",
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar Senha",
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']  # <-- inclua password aqui

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
