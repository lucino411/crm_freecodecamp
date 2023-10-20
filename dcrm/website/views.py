from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

# cada vez que vas a una pagina web estas pidiendo (request) algo. Esa peticion (request) se devuelve de nuevo al backend, la pasamos en una vista y devuelve algo, en la primera vista estamos devolviendo el home.html

def home(request):
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records':records})
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else: 
        messages.success(request, "You must be logged In to view that page")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record have been deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged In to do that")
        return redirect('home')
