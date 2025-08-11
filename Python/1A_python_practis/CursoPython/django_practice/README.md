# **Como iniciar un proyecto en django**

## Primero debes instalar django

### Para instalar Django, solo necesitas escribir el comando
```pip install Django```

### Para verificar que este se instalo correctamente
```py -m django --version```

## Segundo generar un entorno

### Para iniciar un proyecto con django se necesita generar un entorno, con el comando:
```py -m django startproject <Nombre de proyecto>```

Una vez creado el proyecto podras ver la siguiente estructura de carpertas

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
**Recuerda que esto solo es el entorno de nuesto proyecto, no es el proyecto aun.** 

## Tercero crea el proyecto

## Para crear un proyecto con django es tan facil como introducir una linea de comando en la terminal.
debes hubicarte desde tu terminal en el archivo que conteiene el entorno creado anterior mente.

```py manage.py startapp <Nombre>```

Luego de haber generado nuesto proyecto, nos quedara la siguiente estructura de archivos.
```
<Nombre>/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## Felicidades de esta forma se crea un proyecto django.
