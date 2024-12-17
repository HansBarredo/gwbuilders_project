from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contacts(request):
    return render(request, 'contacts/contact.html')

def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')  
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        contact.save()

   
        messages.success(request, 'Your message has been submitted. We will get back to you soon.')
        return redirect('contacts') 

    return render(request, 'contacts/contact.html')
