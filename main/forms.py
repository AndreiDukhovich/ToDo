from django import forms
from .models import Action, Topic

choices = (
        ('', '---'),
        ('ever', 'Каждый день'),
        ('wd', 'По будням'),
        ('we', 'По выходным'))

class FormAction(forms.ModelForm):
    
    title = forms.CharField(label='', 
                            widget=forms.TextInput(attrs={'class': 'edit_form',
                                                         'placeholder': 'Название задачи'}))
    topic = forms.ModelChoiceField(Topic.objects, label='Тема задачи:', 
                                widget=forms.Select(attrs={'class': 'edit_form'}))
    discription = forms.CharField(label='', required=False, 
                                widget=forms.Textarea(attrs={'class': 'edit_form', 
                                                            'placeholder': 'Подробности'}))
    important = forms.BooleanField(label='', required=False, 
                                widget=forms.CheckboxInput(attrs={'class': 'formCheck'}))
    date = forms.DateField(label='', input_formats=['%d.%m.%Y'], required=False,
                            widget=forms.DateInput(attrs={'id': 'dateField', 
                                                        'class': 'flipForm', 
                                                        'placeholder': 'Дата', 
                                                        'readonly': ''}))
    time = forms.TimeField(label='', input_formats=['%H:%M'], required=False,
                            widget=forms.TimeInput(attrs={'id': 'timeField', 
                                                        'class': 'flipForm', 
                                                        'placeholder': 'Время', 
                                                        'readonly': ''}))
    
    period = forms.ChoiceField(label='', choices=choices, 
                                required=False, 
                                widget=forms.Select(attrs={'class': 'flipForm'}))

    class Meta:
        model = Action
        fields = ['title', 'topic', 'discription', 'important', 'date', 'time', 'period']


class EditForm(forms.ModelForm):
    date = forms.DateField(label='', input_formats=['%d.%m.%Y'], required=False,
                            widget=forms.DateInput(attrs={'id': 'dateField', 
                                                        'class': 'flipForm', 
                                                        'placeholder': 'Дата', 
                                                        'readonly': ''}))
    time = forms.TimeField(label='', input_formats=['%H:%M'], required=False,
                            widget=forms.TimeInput(attrs={'id': 'timeField', 
                                                        'class': 'flipForm', 
                                                        'placeholder': 'Время', 
                                                        'readonly': ''}))
    important = forms.BooleanField(label='', required=False, 
                                widget=forms.CheckboxInput(attrs={'class': 'formCheck'}))
    
    period = forms.ChoiceField(label='', choices=choices, 
                                required=False, 
                                widget=forms.Select(attrs={'class': 'flipForm'}))

    class Meta:
        model = Action
        fields = ['date', 'time', 'important', 'period']


class DateForm(forms.Form):
    date = forms.DateField(label='', input_formats=['%d.%m.%Y'], required=False, 
                            widget=forms.DateInput(attrs={'id': 'dateField', 
                                                        'class': 'edit_form', 
                                                        'placeholder': 'Дата', 
                                                        'readonly': ''}))