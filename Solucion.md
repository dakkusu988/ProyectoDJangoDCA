# PASOS A SEGUIR

## PASO 1: Creación y vinculo del Repositorio en GitHUb

Primero crearemos un repositorio en GitHub con nuestro nombre, un README.md por defecto, lenguaje Python y lo último None.
Creamos una carpeta en local para guardar ese repositorio.
Sin estar en ninguna carpeta abierta ir a Source Control y clonar el repositorio guardado en tu GitHub sin antes escribir tu contraseña y dar permisos.
Y así tendriamos ya nuestro proyecto listo para hacer commits de nuestros cambios desde Visual Studio.

## PASO 2: Instalar VirtualEnvwrapper y crear nuestro Entorno Virtual

Para Linux entrar a "https://virtualenvwrapper.readthedocs.io/en/latest/" y seguir los pasos para instalarlo:

### Linux
```bash
$ pip install virtualenvwrapper (Para instalarlo)
$ export WORKON_HOME=~/Envs 
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh (Esta línea la ponemos al final del archivo que ejecuta para no tener que ponerlo cada vez que entramos)
                                             (Ponemos cd y despues nano .bashrc, y dentro del archivo lo añadimos al final)

$ mkvirtualenv nombreEntorno (Para crear el entorno)
$ deactivate (Para salir del entorno)
$ workon (Para ver los entornos creados)
$ workon nombreEntorno (Para entrar al entorno)
```

Para Windows entrar a https://pypi.org/project/virtualenvwrapper-win/ y seguir los pasos para instalarlo:

### Windows
```bash
# using pip
pip install virtualenvwrapper-win

# using easy_install
easy_install virtualenvwrapper-win

# from source
git clone git://github.com/davidmarble/virtualenvwrapper-win.git
cd virtualenvwrapper-win
python setup.py install   # or pip install .
```

## PASO 3: Instalar los paquetes necesarios y requirements.txt

Creamos en el repositorio un archivo "requirements.txt" que contenga esto "Django~=4.2.7" (Ultima versión).
Escribir estos 2 comandos correspondientes dentro de nuestro entorno virtual:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
## PASO 4: Crear el proyecto de Django

Crear el proyecto en tu carpeta desde el entorno virtual con este comando:

```bash
django-admin startproject mysite .
```
## PASO 5: Cambios en settings.py, migrate y arrancar el servidor

Modificamos el archivo settings.py reemplazando cada línea por la correspondiente:

```python
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Berlin'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```

Luego ejecutamos este comando en nuestro proyecto de Django:

```bash
python manage.py migrate
```
Ya por último escribimos el comando dentro del entorno para arrancar el servidor:

```bash
python manage.py runserver
```

Una vez arrancado vemos la dirección correspondiente para saber si todo funciono correctamente:

```text
http://127.0.0.1:8000/
```

## PASO 6: Creación de Task, modificación en settings.py, models.py, makemigrations y migrate

Para crear nuestro task en nuestro proyecto escribir este comando:

```bash
python manage.py startapp task
```

Modificamos el archivo settings.py de esta manera:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]
```

Borrar todo lo que hay en task/models.py y poner esto:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

Escribir en la línea de comandos estos 2 comandos y debería darnos un OK:

```bash
python manage.py makemigrations task
python manage.py migrate task
```

## PASO 7: Modificación admin.py y creación superusuario Admin

Reemplazar el contenido de admin.py con esto:

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

Si tienes el servidor arrancado deberías ver una pestaña de inicio aquí:

```text
http://127.0.0.1:8000/admin/
```

Creamos un superusuario para poder iniciar sesión y administrar nuestro sitio:

```bash
python manage.py createsuperuser

Username: ola
Email address: ola@example.com
Password:
Password (again):
Superuser created successfully.
```

Ahora ya podrás iniciar sesión al escribir tu usuario.

## Paso 8: Modificar urls.py y creación de otro urls.py en Task

Modificar el archivo urls.py para que quede así:

```python
# Archivo urls.py de mysite

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('task.urls')),
]
```

Creamos otro urls.py en task y que quede tal que así:

```python
# Archivo urls.py de task

from django.urls import path
from . import views

urlpatterns = [
  path('', views.task_list, name='task_list'),
]
```

Después de hacer todo esto, no funcionara ni la pagina de admin, ni la de Django, ya que el servidor ha dejado de funcionar.
Luego lo arreglaremos.

## Paso 9: Modificación archivo views.py de Task

Modificar el archivo views.py de task para que quede así:

```python
from django.shortcuts import render
from .models import Task

def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'tasks/task_list.html', {'tasks': task})
```

Debería salir un TemplateError.

## Paso 10: Creación de directorios y archivo templates/task/task_list.html en Task, reinicio de servidor y modificación de task_list.html

Crea un directorio dentro de Task para que quede tal que así:

```text
task
└───templates
    └───task
```

Ahora crea un archivo task_list.html dentro de esa ruta que has creado y mira la página:

```text
http://127.0.0.1:8000/
```

Si te sigue dando error reinicia el servidor con "Ctrl+C" y "python manage.py runserver".
Se debería ver una pantalla en Blanco.

Ahora completamos el archivo task_list.html con este contenido:

```python
<html>
        <head>
            <title>Task List</title>
        </head>
        <body>
            <h1>Lista de Tareas</h1>
            <ul>
                {% for task in tasks %}
                <li>
                    <h2>{{ task.title }}</h2>
                    <p>{{ task.description }} - {% if task.completed %} Sí {% else %} No {% endif %}</p>
                </li>
                {% empty %}
                <p>No hay tareas disponibles.</p>
                {% endfor %}
            </ul>
        </body>
    </html>
```
Se deberían notar los cambios hechos en la pagina.

## Paso 11: Coming soon...
