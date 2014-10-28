from django.test import TestCase
from django.db import IntegrityError
from contacts.models import Contact

class ContactModelTests(TestCase):
    def test_requires_a_first_name(self):
        contact = Contact(first_name=None, last_name='Brown')
        self.assertRaises(IntegrityError, contact.save)
        
    def test_requires_a_last_name(self):
        contact = Contact(first_name='Charlie', last_name=None)
        self.assertRaises(IntegrityError, contact.save)
