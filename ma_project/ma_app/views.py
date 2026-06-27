from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError  

# Create your views here.


def home(request):
    return render(request, 'home.html')

def selection(request):
    return render(request, 'selection.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('signup')
            elif ' ' in username:
                messages.info(request, 'username cannot contain spaces')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('signup')
            elif password is None:
                messages.info(request, 'Please enter password')
                return redirect('signup')
            elif ' ' in password:
                messages.info(request, 'Password cannot contain spaces')
                return redirect('signup')
            elif len(password) < 4 or len(password) > 15:
                messages.info(request, 'password must be more than 4 charcters and less than 15 characters')
                return redirect('signup')
            else:
               
               try:
                validate_email(email)
               except ValidationError:
                messages.error(request, 'Invalid email used, try again...')
                return redirect('signup')

               user = User.objects.create_user(username=username, email=email, password=password)
               user.save()
               messages.info(request, 'user created successfully. Check in your django admin dashboard.')
               return redirect('signup')
        else:
            messages.info(request, 'Invalid password')  
            return redirect('signup')
    return render(request, 'signup.html')
            
            
