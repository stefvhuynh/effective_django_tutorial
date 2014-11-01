from django.shortcuts import render
from django.views.generic import View
from contacts.models import Contact

class ContactList(View):
    def get(self, request):
        contacts = Contact.objects.all()
        context = {'contacts': contacts}
        return render(request, 'contacts/contact_list.html', context)
