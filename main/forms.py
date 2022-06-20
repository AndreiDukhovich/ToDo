from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Action, Topic, User

class Form_action(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'formText', 'placeholder': 'Введи название'}))
    topic = forms.ModelChoiceField(Topic.objects, label='', widget=forms.Select(attrs={'class': 'formText', 'placeholder': 'Введи тему'}))
    discription = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={'class': 'formText', 'placeholder': 'Опиши задачу (необязательно)'}))
    date = forms.DateField(label='', input_formats=['%d.%m.%Y'], required=False, 
                            widget=forms.DateInput(attrs={'id': 'dateField', 'class': 'formDateTime', 'placeholder': 'Дата (тоже не обязательно))', 'readonly': ''}))
    time = forms.TimeField(label='', input_formats=['%H:%M'], required=False, widget=forms.TimeInput(attrs={'id': 'timeField', 'class': 'formDateTime', 'placeholder': 'Время (и это не обязательно))', 'readonly': ''}))
    important = forms.BooleanField(label='', required=False, widget=forms.CheckboxInput(attrs={'class': 'formCheck'}))

    class Meta:
        model = Action
        fields = ['topic', 'title', 'discription', 'date', 'time', 'important']

class Form_change(forms.ModelForm):
    complete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'formCheck'}))

    class Meta:
        model = Action
        fields = ['complete']


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