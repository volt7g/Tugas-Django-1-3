from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def check_for_special(value):
    if value[0].isnumeric():
        raise forms.ValidationError("Names cannot start with a number.")

class FormName(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5),check_for_special])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        
        if email != vemail:
            raise forms.ValidationError("Make sure emails match!")