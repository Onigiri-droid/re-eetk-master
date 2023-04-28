from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import modelformset_factory, formset_factory, BaseFormSet
from core.models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин', 'name': 'login'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'name': 'pswd'}))


class CreateTableForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control datepicker',
            'autocomplete': 'off'
        })
    )
    number = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            'class': 'number'
        }),
        queryset=NumberLesson.objects.only('numberlesson_name')
    )
    theme = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            'class': 'theme'
        }),
        queryset=Theme.objects.all()
    )
    teacher = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            'class': 'teacher'
        }),
        queryset=Teacher.objects.all()
    )
    group = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            'class': 'group'
        }),
        queryset=Group.objects.all()
    )
    cabinet = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            'class': 'cabinet'
        }),
        queryset=Cabinet.objects.all()
    )
    subgroup = forms.ModelChoiceField(
        widget=forms.Select(attrs={
            'class': 'subgroup'
        }),
        queryset=Subgroups.objects.all()
    )

    class Meta:
        model = Lesson
        fields = ['date', 'number', 'theme', 'teacher', 'group', 'subgroup', 'cabinet']


LessonFormSet = modelformset_factory(
    Lesson,
    form=CreateTableForm,
    extra=1
)
