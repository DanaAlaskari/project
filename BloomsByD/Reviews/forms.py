from django import forms
from .models import Review

        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = '__all__'

        widgets = {
            'Flower' : forms.TextInput(attrs={'class': 'formcontrol'}),
            'username' : forms.TextInput(attrs={'class': 'formcontrol'}),
            'opinion ' : forms.TextInput(attrs={'class': 'formcontrol'}),
        }