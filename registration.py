from django.db import models
from django.urls import reverse

class LoginSystem(models.User):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    userName = models.CharField(max_length=20, help_text='Enter your Username')
    passCode = models.TextField(max_length=30, help_text='Enter your password.')
    # …

    # Metadata
    class Meta:
        ordering = ['-userName']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

    def sendInfo(self):
        return

    def enterInfo(self):
        record = user(userName, passCode)
        record.save()
        
    