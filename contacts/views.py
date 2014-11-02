from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View
from contacts.models import Contact
from contacts.forms import ContactForm

class ContactList(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        context = {'contacts': contacts}
        return render(request, 'contacts/contact_list.html', context)


class ContactNew(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/contact_new.html')
        
    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('contacts:contact_list'))
        else:
            return render(request, 'contacts/contact_new.html', status=422)


class ContactDetail(View):
    def get(self, request, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=kwargs['contact_id'])
        context = {'contact': contact}
        return render(request, 'contacts/contact_detail.html', context)
        

class ContactEdit(View):
    def get(self, request, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=kwargs['contact_id'])
        context = {'contact': contact}
        return render(request, 'contacts/contact_edit.html', context)
        
    def post(self, request, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=kwargs['contact_id'])
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return redirect(
                reverse('contacts:contact_detail', args=(contact.id,))
            )
        else:
            context = {'contact': contact}
            return render(
                request, 'contacts/contact_edit.html', context, status=422
            )
    
            
