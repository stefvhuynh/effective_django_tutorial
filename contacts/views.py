from django.shortcuts import render
from contacts.models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts/contact_list.html', context)
