from django import forms
class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Юзернейм')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(label='Возраст', min_value=0)