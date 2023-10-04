from django.db import models
from django.urls import reverse
import uuid # Required for unique book instances

class wellness(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    patientID = models.IntegerField('ID', help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('w', 'Waiting'),
        ('U', 'Up'),
        ('D', 'Done'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Status in queue',
    )

    class Meta:
        queue_status = ['waiting']
        
        def waiting(self):
            return

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
