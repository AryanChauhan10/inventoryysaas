from django.shortcuts import render
from .models import Contact

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'core/home.html')
