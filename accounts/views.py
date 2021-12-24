
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Registration


def register(request):
    if request.method == 'POST':
        # Register User
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number', '')
        # dob = request.POST.get('dob')
        gender = request.POST.get('gender')

        # check passwor match
        if password == password2:
            # check username
            if Registration.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('accounts:register')
            elif Registration.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return redirect('accounts:register')
            else:
                user = Registration(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    address=address,
                    contact_number=contact_number,
                    gender=gender
                )
                # auth.login(request, user)
                # messages.success(request, 'register successful')
                # return redirect('pages:index')
                user.set_password(password)
                user.save()
                messages.success(
                    request, 'You are now registered and can log in')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts:register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            username=username,
            password=password,
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('pages:index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logout.')
        return redirect('pages:index')
