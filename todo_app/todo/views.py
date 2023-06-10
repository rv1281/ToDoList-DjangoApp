from django.shortcuts import render, redirect
from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, ToDoForm
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
# Views for user creation

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                messages.success(request, 'Account created successfully! You are now logged in.')
                return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    todos = ToDo.objects.filter(user=request.user).order_by('completed', '-id')
    form = ToDoForm(request.POST or None)  # Create an instance of the form
    if request.method == 'POST':
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Set the user attribute
            todo.save()
            return redirect('dashboard')
    return render(request, 'dashboard.html', {'todos': todos, 'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def todo_list(request):
    todos = ToDo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = False if request.POST.get('completed') != 'on' else True
        ToDo.objects.create(user=request.user, title=title, completed=completed)
        return redirect('todo_list')
    return render(request, 'create_todo.html')

@login_required
def update_todo(request, pk):
    todo = ToDo.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user  # Set the user attribute
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'update_todo.html', {'todo': todo, 'form': form})


@login_required
def delete_todo(request, pk):
    todo = ToDo.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('dashboard')  # Redirect to the dashboard page
    return render(request, 'delete_todo.html', {'todo': todo})


# For Fast API calls

class ToDoListCreateAPIView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ToDoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
