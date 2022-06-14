from django.shortcuts import render
from .models import Opportunity

def home(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'home.html', {'opportunities':opportunities})