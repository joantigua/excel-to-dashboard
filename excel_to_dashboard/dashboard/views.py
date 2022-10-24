from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def home (request):
    agents = Agent.objects.all()
    context = {'agents' : agents}
    return render(request, 'dashboard/agents.html', context)

def dashboard(request, id):
  agents = Agent.objects.filter(id = id)
  
  context = {
      'agents' : agents,
      }
  return render(request, 'dashboard/dashboard.html', context )

def deleteAgents(request):
  agents = Agent.objects.all()
  agents.delete()
  return redirect('/home')