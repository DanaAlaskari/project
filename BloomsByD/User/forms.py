from django import forms
from .models import User

        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'Firstname' : forms.TextInput(attrs={'class': 'formcontrol'}),
            'Lastname' : forms.TextInput(attrs={'class': 'formcontrol'}),
            'Phone' : forms.TextInput(attrs={'class': 'formcontrol'}),
            'Email' : forms.TextInput(attrs={'class': 'formcontrol'}),
            'password': forms.PasswordInput(attrs={'class': 'formcontrol'}),
    
        }