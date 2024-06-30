# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm, send_email_task
from django.contrib import messages
import time

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            naam = form.cleaned_data['naam']
            email = form.cleaned_data['email']
            telefoonnummer = form.cleaned_data['telefoonnummer']
            opmerkingen = form.cleaned_data['opmerkingen']

            html = render_to_string('emails/contactform.html', {
                'naam': naam,
                'email': email,
                'telefoonnummer': telefoonnummer,
                'opmerkingen': opmerkingen,
            })
            send_mail('The contact form subject', 'This is the message', 'rondirksbadkamers@gmail.com', ['rondirksbadkamers@gmail.com'], html_message=html)
            messages.success(request, "Formulier verzonden, hartelijk dank wij nemen zo snel mogelijk contact met u op!")
            return redirect('contact') 
            
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form
    })
