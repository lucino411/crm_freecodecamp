from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        }))
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }))
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs[
            'placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "First Name",
            "class": "form-control"
        }),
        label="")
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Last Name",
            "class": "form-control"
        }),
        label="")
    email = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Email",
            "class": "form-control"
        }),
        label="")
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Phone",
            "class": "form-control"
        }),
        label="")
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Address",
            "class": "form-control"
        }),
        label="")
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "City",
            "class": "form-control"
        }),
        label="")
    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "State",
            "class": "form-control"
        }),
        label="")
    zipcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Zipcode",
            "class": "form-control"
        }),
        label="")

    class Meta:
        model = Record
        exclude = ("user", )

# El atributo exclude en la clase Meta se utiliza para especificar los campos del modelo que no deben incluirse en el formulario. Estos campos excluidos son generalmente aquellos que se rellenarán automáticamente o cuyo valor no se espera que sea ingresado por el usuario a través del formulario.

# En el código que proporcionaste, exclude = ("user", ) significa que el campo user no estará incluido en el formulario. Esto puede ser útil en situaciones en las que el valor del campo user será proporcionado automáticamente por el sistema y no se espera que el usuario lo ingrese manualmente.

# Django generalmente proporciona funcionalidades para rastrear el usuario que realiza ciertas acciones, como agregar registros a la base de datos. Esto a menudo se realiza automáticamente mediante el uso de información de autenticación y autorización del usuario que está actualmente autenticado en el sistema. De esta manera, la aplicación puede registrar qué usuario realizó cierta acción, como agregar un registro en este caso.