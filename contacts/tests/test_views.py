from django.test import TestCase
from django.core.urlresolvers import reverse
from contacts.models import Contact

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
            reverse('contacts:contact_list'), valid_data
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Contact.objects.all()), 1)
    
    def test_post_with_invalid_data(self):
        invalid_data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        
        response = self.client.post(
            reverse('contacts:contact_list'), invalid_data
        )
        
        self.assertEqual(response.status_code, 422)
        self.assertEqual(len(Contact.objects.all()), 0)


def add_contact(first_name, last_name, email):
    contact = Contact.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )
    
    
    