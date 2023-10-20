from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# cada vez que vas a una pagina web estas pidiendo (request) algo. Esa peticion (request) se devuelve de nuevo al backend, la pasamos en una vista y devuelve algo, en la primera vista estamos devolviendo el home.html


def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have been logged In')
            return redirect('home')
        else:
            messages.success(
                request, 'There was and Error Loggin In, Plesae try again')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,
                             "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


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


# Si usas form = AddRecordForm(request.POST or None), básicamente estás creando un formulario en blanco o un formulario no vinculado a una instancia específica de un modelo. Esto es útil cuando deseas crear una nueva instancia de un modelo con los datos proporcionados en el formulario. Sin embargo, cuando se usa de esta manera, deberás llamar explícitamente al método save() en el formulario para guardar los datos ingresados en la base de datos.

# Si usas form = AddRecordForm(request.POST or None, instance=current_record), Cuando se utiliza instance=current_record en el formulario AddRecordForm, estás enlazando el formulario a una instancia específica del modelo Record, lo que te permite editar los campos de esa instancia a través del formulario. Sin embargo, para que los cambios se guarden en la base de datos, es necesario llamar explícitamente al método save() en el formulario, es decir, form.save(). Si no se llama a este método, los cambios no se guardarán en la base de datos.



def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added")
                return redirect('home')

        return render(request, 'add_record.html', {'form': form})

    else:
        messages.success(request, "You must be logged In to do that")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(pk=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged In to do that")
        return redirect('home')
