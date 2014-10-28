import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'addressbook.settings')

import django
django.setup()

from contacts.models import Contact

def populate():
    add_contact(
        first_name='Charlie', last_name='Brown', email='charlie@peanuts.com'
    )
    
    add_contact(
        first_name='Linus', last_name='van Pelt', email='linus@peanuts.com'
    )
    
    add_contact(
        first_name='Sally', last_name='Brown', email='sally@peanuts.com'
    )


def add_contact(first_name, last_name, email):
    return Contact.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )[0]


if __name__ == '__main__':
    print 'Excecuting %s' % __file__
    populate()
    
