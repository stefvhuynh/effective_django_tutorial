from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    
    def __unicode__(self):
        return ' '.join([self.first_name, self.last_name])
