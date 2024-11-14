from django import forms
from subscribe_app.models import Customer

class OldSubscriberForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = "__all__"
