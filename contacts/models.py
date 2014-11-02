from django.db import models

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255, default=None, help_text='First Name:'
    )
    last_name = models.CharField(
        max_length=255, default=None, help_text='Last Name:'
    )
    email = models.EmailField(
        max_length=255, default=None, help_text='Email:'
    )
    
    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])
