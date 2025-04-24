from django import forms
from .models import User,Task

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['user_name', 'nama', 'last_nama', 'email', 'number', 'gender']

class TaskForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%Y-%m-%d', '%d/%m/%Y'])
    class Meta:
        model=Task
        fields = ['task_name', 'task_desc','clock']
        
