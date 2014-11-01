from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import View
from contacts.models import Contact
from contacts.forms import ContactForm

class ContactListView(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        context = {'contacts': contacts}
        return render(request, 'contacts/contact_list.html', context)


class ContactFormView(View):
    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        context = {'contact_form': contact_form}
        return render(request, 'contacts/contact_form.html', context)
        
    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('contacts:contact_list'))
        else:
            context = {'contact_form': contact_form}
            return render(
                request, 'contacts/contact_form.html', context, status=422
            )


class ContactDetailView(View):
    def get(self, request, *args, **kwargs):
        contact = get_object_or_404(Contact, pk=kwargs['contact_id'])
        context = {'contact': contact}
        return render(request, 'contacts/contact_detail.html', context)
            
            
            
