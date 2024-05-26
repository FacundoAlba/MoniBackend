from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.decorators import login_required
from .models import LoanRequest

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=20,
        help_text='20 caracteres como máximo. Únicamente letras, dígitos y @/./+/-/_'
    )

    password1 = forms.CharField(
        label='Contraseña',
        min_length=8,
        widget=forms.PasswordInput,
        help_text='Su contraseña debe contener al menos 8 caracteres.'
    )

    password2 = forms.CharField(
        label='Repetir contraseña',
        widget=forms.PasswordInput,
        help_text='Repita la contraseña'
    )

class CustomUserUptadeForm(UserCreationForm):
    username = forms.CharField(
        label='Nuevo nombre de usuario',
        max_length=20,
        help_text='20 caracteres como máximo. Únicamente letras, dígitos y @/./+/-/_'
    )

    password1 = forms.CharField(
        label=' Nueva contraseña',
        min_length=8,
        widget=forms.PasswordInput,
        help_text='Su contraseña debe contener al menos 8 caracteres.'
    )

    password2 = forms.CharField(
        label='Repetir nueva contraseña',
        widget=forms.PasswordInput,
        help_text='Repita la contraseña'
    )

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm()
        })  
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('loans')
            except:
                return render(request, 'signup.html', {'form': CustomUserCreationForm(), 'error': '* El Usuario ya existe'})
        else:
            return render(request, 'signup.html', {'form': CustomUserCreationForm(), 'error': '* Las contraseñas no coinciden'})


def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        }) 
    else:
        user = authenticate(request, username=request.POST['username'], 
        password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "* Usuario o Contraseña incorrecto"
            })
        else:
            login(request, user)
            return redirect ('home')
        
@login_required
def user_detail(request):
    user = request.user
    if request.method == 'GET':
        form = CustomUserUptadeForm()
    else:
        form = CustomUserUptadeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Los datos se han actualizado correctamente!')
            return redirect('home')
    
    return render(request, 'user_detail.html', {'form': form})
        
@login_required
def loans(request):
    loans = LoanRequest.objects.all()

    return render(request, 'loans.html', {
        'loans': loans
    })


