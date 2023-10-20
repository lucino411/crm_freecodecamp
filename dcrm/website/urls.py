from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home' ),
    # path('login/', views.login_user, name = 'login' ),
    path('logout', views.logout_user, name = 'logout' ),
    path('register', views.register_user, name = 'register' ),
    path('record/<int:pk>', views.customer_record, name = 'record' ),
    path('delete_record/<int:pk>', views.delete_record, name = 'delete_record' ),
    path('update_record/<int:pk>', views.update_record, name = 'update_record' ),
    path('add_record/', views.add_record, name = 'add_record' ),
]

'''
El parámetro name en la función path en las URLs de Django se utiliza para identificar de manera única una URL particular en el proyecto. Proporcionar un nombre a una URL puede ser útil en varias situaciones:

Referencia en plantillas: Puedes usar el nombre proporcionado para referenciar la URL desde las plantillas de Django. Esto es particularmente útil para construir enlaces de forma dinámica en las plantillas.

Reverse URL matching: Puedes utilizar el nombre de la URL para realizar coincidencias inversas (reverse URL matching) en tu código de Django. Esto te permite evitar codificar manualmente las URL en tu aplicación y en su lugar utilizar los nombres de las URLs definidas en las configuraciones de las vistas.

Por ejemplo, si tienes un enlace en tu plantilla que apunta a la vista 'home', podrías usar algo como:

<a href="{% url 'home' %}">Home</a>
Esto generaría un enlace que apunta a la URL correspondiente a la vista con el nombre 'home' definida en tus archivos de URL.

Además, en tu código de Django, puedes usar el nombre de la URL para realizar coincidencias inversas, lo que te permite generar dinámicamente la URL asociada a un nombre particular:

from django.urls import reverse

url = reverse('home')
El parámetro name proporciona una forma de referenciar las URLs de manera legible y lógica en tu aplicación de Django, lo que facilita la gestión y el mantenimiento del código a lo largo del tiempo.

'''