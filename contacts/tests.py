from django.test import TestCase
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from contacts.models import Contact

class ContactModelTests(TestCase):
    def test_requires_a_first_name(self):
        contact = Contact(
            first_name=None, last_name='Brown', email='charlie@peanuts.com'
        )
        self.assertRaises(IntegrityError, contact.save)
        
    def test_requires_a_last_name(self):
        contact = Contact(
            first_name='Charlie', last_name=None, email='charlie@peanuts.com'
        )
        self.assertRaises(IntegrityError, contact.save)
        
    def test_requires_an_email(self):
        contact = Contact(
            first_name='Charlie', last_name='Brown', email=None
        )
        self.assertRaises(IntegrityError, contact.save)
    
    def test_unicode_representation(self):
        contact = Contact(
            first_name='Charlie', last_name='Brown', email='charlie@peanuts.com'
        )
        self.assertEqual(unicode(contact), 'Charlie Brown')
        
        
class ContactIndexViewTests(TestCase):
    def test_with_no_contacts(self):
        response = self.client.get(reverse('contacts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['contacts'], [])
    
    def test_with_contacts(self):
        add_contact('Charlie', 'Brown', 'charlie@peanuts.com')
        add_contact('Linus', 'van Pelt', 'linus@peanuts.com')
        response = self.client.get(reverse('contacts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['contacts']), 2)
        
    
def add_contact(first_name, last_name, email):
    contact = Contact.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )
    
    