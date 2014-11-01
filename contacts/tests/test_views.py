from django.test import TestCase
from django.core.urlresolvers import reverse
from contacts.models import Contact
from contacts.forms import ContactForm

class ContactListViewTests(TestCase):
    """
    GET requests
    """
    def test_get_with_no_contacts(self):
        response = self.client.get(reverse('contacts:contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['contacts'], [])
    
    def test_get_with_contacts(self):
        add_contact('Charlie', 'Brown', 'charlie@peanuts.com')
        add_contact('Linus', 'van Pelt', 'linus@peanuts.com')
        response = self.client.get(reverse('contacts:contact_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['contacts']), 2)
        self.assertContains(response, 'Charlie Brown')
        self.assertContains(response, 'Linus van Pelt')
        

class ContactNewViewTests(TestCase):
    """
    GET requests
    """
    def test_get(self):
        response = self.client.get(reverse('contacts:contact_new'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['contact_form'], ContactForm)
        self.assertContains(response, 'Add Contact')
    """
    POST requests
    """
    def test_post_with_valid_data(self):
        valid_data = {
            'first_name': 'Charlie', 
            'last_name': 'Brown', 
            'email': 'charlie@peanuts.com'
        }
        
        response = self.client.post(
            reverse('contacts:contact_new'), valid_data
        )
        
        self.assertRedirects(
            response, 
            reverse('contacts:contact_list'), 
            status_code=302, 
            target_status_code=200
        )
        self.assertEqual(len(Contact.objects.all()), 1)
    
    def test_post_with_invalid_data(self):
        invalid_data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        
        response = self.client.post(
            reverse('contacts:contact_new'), invalid_data
        )
        
        self.assertEqual(response.status_code, 422)
        self.assertIsInstance(response.context['contact_form'], ContactForm)
        self.assertEqual(len(Contact.objects.all()), 0)


"""
Helper methods
"""
def add_contact(first_name, last_name, email):
    contact = Contact.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )
    
    
    