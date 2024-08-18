from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from tours.models import Tour  # Assuming you have a Tour model in the tours app
from agents.models import Agent  # Assuming you have an Agent model in the agents app

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    if user.groups.filter(name='Administrators').exists():
        tours = Tour.objects.all()
        agents = Agent.objects.all()
    elif user.groups.filter(name='Managers').exists():
        tours = Tour.objects.filter(managed_by=user)
        agents = Agent.objects.all()  # Managers can see all agents
    else:  # Agents group
        tours = Tour.objects.filter(managed_by=user)
        agents = Agent.objects.filter(id=user.id)  # Agents only see their own info

    return render(request, 'accounts/profile.html', {'tours': tours, 'agents': agents})
