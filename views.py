from django.shortcuts import render

# Create your views here.
from .models import User, Symptom, Illness, Hospital

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_patients = User.objects.all().count()
    #num_registered = LoginSystem.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = User.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_diseases = Illness.objects.count()

    context = {
        'num_patients': num_patients,
        'num_instances': num_instances_available,
        'num_diseases': num_diseases,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'signup.html', context=context)

