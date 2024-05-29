from django import forms
from django.core.mail import send_mail
class ContactForm(forms.Form):
    naam = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefoonnummer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    adres = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plaats = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postcode = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    reacties = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

def send_email_task(subject, message, recipient_list, html_message=None):
    send_mail(subject, message, None, recipient_list, html_message=html_message)