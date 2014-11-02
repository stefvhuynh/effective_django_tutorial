from django import template
from contacts.forms import ContactForm

register = template.Library()

@register.inclusion_tag('contacts/_contact_fields.html')
def contact_fields(contact=None):
    contact_form = ContactForm(instance=contact)
    return {'contact_form': contact_form}