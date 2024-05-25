from django.shortcuts import render, redirect
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
        label='Repetir Contraseña',
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
    if request.method == 'GET':
        user = request.user
        form = CustomUserCreationForm(instance=user)
        return render(request, 'user_detail.html', {
            'user': user, 'form': form
        })
    else:
        user = request.user
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            return render(request, 'user_detail.html', {
                'user': user, 'form': form
            })
@login_required
def loans(request):
    loans = LoanRequest.objects.all()

    return render(request, 'loans.html', {
        'loans': loans
    })


