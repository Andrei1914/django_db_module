from django import forms
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Юзернейм')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')