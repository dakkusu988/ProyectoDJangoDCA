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

```bash
http://127.0.0.1:8000/
```