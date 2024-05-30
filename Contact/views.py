# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm, send_email_task
import time

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            naam = form.cleaned_data['naam']
            email = form.cleaned_data['email']
            telefoonnummer = form.cleaned_data['telefoonnummer']
            adres = form.cleaned_data['adres']
            plaats = form.cleaned_data['plaats']
            postcode = form.cleaned_data['postcode']
            reacties = form.cleaned_data['reacties']

            html = render_to_string('emails/contactform.html', {
                'naam': naam,
                'email': email,
                'telefoonnummer': telefoonnummer,  
                'adres': adres,
                'plaats': plaats, 
                'postcode': postcode,
                'reacties': reacties
            })

            send_mail('The contact form subject', 'This is the message', 'Nc.vanderworp@gmail.com', ['Nc.vanderworp@gmail.com'], html_message=html)
            return redirect('contact') 
            
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })
