from django.urls import reverse # Used to generate URLs by reversing the URL patterns

from newsite.catalog import models


class user(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    symptoms = models.ManyToManyField(max_length=20)


    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author is a string rather than an object because it hasn't been declared yet in the file
    userName = models.CharField(max_length=20)
    password = models.TextField(max_length=30)
    phone = models.TextField(max_length=30, help_text='Enter your phone number')
    email = models.ForeignKey('email', unique=True,
                             help_text='Your email goes here.')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    symptoms = models.ManyToManyField(userName, help_text='Your symptoms appear here.')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def getSymptoms(self):
        return symptoms.split(' ,',symptoms)
    
