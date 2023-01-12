from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from account.models import Account

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')


            raw_password = form.cleaned_data.get('raw_password')
            account = authenticate(email=email, username=username, fname=fname, lname=lname, phone=phone, password=raw_password)
            # login(request, account)

            return redirect('logout')
        else:
            print(form.errors)
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        
    return render(request, 'account/registration.html', context)

def logout_view(request):
    logout(request)
    return redirect('authorization')

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('index')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')

    else:
        form = AccountAuthenticationForm(request.POST)
    
    context['login_form'] = form

    return render(request, 'account/authorization.html', context)