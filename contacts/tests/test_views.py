from django.test import TestCase
from django.core.urlresolvers import reverse
from contacts.models import Contact
from contacts.forms import ContactForm

class ContactListTests(TestCase):
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
        

class ContactNewTests(TestCase):
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


class ContactDetailTests(TestCase):
    """
    GET request
    """
    def test_get_with_valid_id(self):
        contact = add_contact('Charlie', 'Brown', 'charlie@peanuts.com')
        response = self.client.get(
            reverse('contacts:contact_detail', args=(contact.id,))
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['contact'], contact)
        
    def test_get_with_invalid_id(self):
        response = self.client.get(
            reverse('contacts:contact_detail', args=(1,))
        )
        
        self.assertEqual(response.status_code, 404)
        

class ContactEditTests(TestCase):
    """
    GET request
    """
    def test_get_with_valid_id(self):
        contact = add_contact('Charlie', 'Brown', 'charlie@peanuts.com')
        response = self.client.get(
            reverse('contacts:contact_edit', args=(contact.id,))
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['contact_form'], ContactForm)
        
    def test_get_with_invalid_id(self):
        response = self.client.get(
            reverse('contacts:contact_edit', args=(1,))
        )
        
        self.assertEqual(response.status_code, 404)
    """
    POST request
    """
    def test_post_with_valid_data(self):
        original_contact = add_contact(
            'Charlie', 'Brown', 'charlie@peanuts.com'
        )
        valid_data = {
            'first_name': 'Charlie',
            'last_name': 'Brown',
            'email': 'charliebrown@peanuts.com'
        }
        response = self.client.post(
            reverse('contacts:contact_edit', args=(original_contact.id,)),
            valid_data
        )
        updated_contact = Contact.objects.get(pk=original_contact.id)

        self.assertRedirects(
            response, 
            reverse('contacts:contact_detail', args=(updated_contact.id,)),
            status_code=302,
            target_status_code=200
        )
        self.assertEqual(updated_contact.email, 'charliebrown@peanuts.com')

    def test_post_with_invalid_data(self):
        original_contact = add_contact(
            'Charlie', 'Brown', 'charlie@peanuts.com'
        )
        invalid_data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        response = self.client.post(
            reverse('contacts:contact_edit', args=(original_contact.id,)),
            invalid_data
        )
        updated_contact = Contact.objects.get(pk=original_contact.id)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(original_contact, updated_contact)
    

"""
Helper methods
"""
def add_contact(first_name, last_name, email):
    contact = Contact.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )
    return contact[0]
    
    
    