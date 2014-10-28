from django.test import TestCase
from django.core.urlresolvers import reverse
from contacts.models import Contact

class ContactListViewTests(TestCase):
    def test_with_no_contacts(self):
        response = self.client.get(reverse('contacts:contact_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['contacts'], [])
    
    def test_with_contacts(self):
        add_contact('Charlie', 'Brown', 'charlie@peanuts.com')
        add_contact('Linus', 'van Pelt', 'linus@peanuts.com')
        response = self.client.get(reverse('contacts:contact_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['contacts']), 2)
        self.assertContains(response, 'Charlie Brown')
        

class ContactCreateViewTests(TestCase):
    def test_with_a_get_request(self):
        
    def test_with_a_post_request(self):


def add_contact(first_name, last_name, email):
    contact = Contact.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )