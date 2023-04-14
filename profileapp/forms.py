from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrationUser(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={"class":"myfield"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class":"myfield"}))
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs={"class":"myfield"}))
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={"class":"myfield"}))
    password1 = forms.CharField(label='Пароль:', required=True,
                                help_text=['Пароль не должен быть слишком похож на другую вашу личную информацию.',
                                'Ваш пароль должен содержать как минимум 8 символов.',
                                'Пароль не может состоять только из цифр.'],
                                widget=forms.PasswordInput(attrs={"class":"myfield"}))
    password2 = forms.CharField(label='Подтверждение пароля:', required=True,
                                widget=forms.PasswordInput(attrs={"class": "myfield"})
                                )
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']

class ProfileTimeForm(forms.Form):
    time = forms.TimeField(required=True, input_formats=['%H:%M'], 
                        widget=forms.TimeInput(
                        attrs={"class":"myfield", 
                                'placeholder': 'Установите время оповещения',
                                'id': 'timeField'}))

