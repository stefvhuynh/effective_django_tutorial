from django.test import TestCase
from django.db import IntegrityError
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
        
