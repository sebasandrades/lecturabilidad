# Lecturabilidad
Proyecto elaborado en Django usando una base de datos `sqlite3`
### Configuración del entorno
> Es necesario tener instalado la version 3.7 de python o posterior

1. Crear el entorno virtual con el comando `python -m venv .env` ( `-m` indica que es un  modulo)
1. Habilitar el entorno virtual con `.env/Scripts/activate.bat` en Windows
1. Instalar las dependencias ubicadas en `requirements.txt` con el comando `pip install -r requirements.txt`

1. Ejecutar las migraciones para que se generen las tablas necesarias `python manage.py migrate`
1. Iniciar el servidor de desarrollo `python manage.py runserver`
