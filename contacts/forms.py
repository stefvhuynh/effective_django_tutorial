from django import forms
from contacts.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, help_text='First name')
    last_name = forms.CharField(max_length=128, help_text='Last name')
    email = forms.EmailField(max_length=128, help_text='Email')
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email',)