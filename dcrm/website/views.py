from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# cada vez que vas a una pagina web estas pidiendo (request) algo. Esa peticion (request) se devuelve de nuevo al backend, la pasamos en una vista y devuelve algo, en la primera vista estamos devolviendo el home.html

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authentication
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have been logged In')
            return redirect('home')
        else:
            messages.success(request, 'There was and Error Loggin In, Plesae try again')
            return redirect('home')
    else: 
        return render(request, 'home.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')