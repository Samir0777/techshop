from django.shortcuts import render
from .models import CardSection

def home(request):
    cards = CardSection.objects.all()
    return render(request, 'home.html', {'cards': cards})
