# PASOS A SEGUIR

## PASO 1: Creación y vinculo del Repositorio en GitHUb

Primero crearemos un repositorio en GitHub con nuestro nombre, un README.md por defecto, lenguaje Python y lo último None.
Creamos una carpeta en local para guardar ese repositorio.
Sin estar en ninguna carpeta abierta ir a Source Control y clonar el repositorio guardado en tu GitHub sin antes escribir tu contraseña y dar permisos.
Y así tendriamos ya nuestro proyecto listo para hacer commits de nuestros cambios desde Visual Studio.

## PASO 2: Instalar VirtualEnvwrapper y crear nuestro Entorno Virtual

Entrar a la página de VirtualEnvwrapper "https://virtualenvwrapper.readthedocs.io/en/latest/" y seguir los pasos para instalarlo:

```bash
$ pip install virtualenvwrapper (Para instalarlo)
$ export WORKON_HOME=~/Envs 
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh (Esta línea la ponemos al final del archivo que ejecuta para no tener que ponerlo cada vez que entramos)
                                             (Ponemos cd y despues nano .bashrc, y dentro del archivo lo añadimos al final)

$ mkvirtualenv nombreEntorno (Para crear el entorno)
$ deactivate (Para salir del entorno)
$ workon (Para ver los entornos creados)
$ workon nombreEntorno (Para entrar al entorno)```
