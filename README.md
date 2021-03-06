# Lecturabilidad
Proyecto elaborado en Django usando una base de datos `PostgreSQL`

## [Página Principal](https://lecturabilidad.herokuapp.com/)
### Configuración del entorno
> Es necesario tener instalado la version 3.7 de python o posterior

1. Crear el entorno virtual con el comando `python -m venv .env` ( `-m` indica que es un  modulo)
1. Habilitar el entorno virtual con `.env\Scripts\activate.bat` en Windows
1. Instalar las dependencias ubicadas en `requirements.txt` con el comando `pip install -r requirements.txt`

1. Ejecutar las migraciones para que se generen las tablas necesarias `python manage.py migrate`
1. Iniciar el servidor de desarrollo `python manage.py runserver`


## Estructura del proyecto
* `lectura/urls.py` es donde se declaran las rutas que puede resolver el servidor

* `templates` todo lo que son los html's para mostrar en las `views`.

* `users` es la aplicación encargar de manejar la autenticación de los usuarios
  
* `static` archivos estaticos utilizados en los html's

* `lecture/tablas_resultados` aquí se encuentrans las tablas `tabla_flesch` y `tabla_inflesz`


# Preparación para desplegar en Heroku [Ver tutorial](https://codigofacilito.com/articulos/deploy-django-heroku)

1. `pip install gunicorn` gunicorn es un servidor HTTP para Unix.
1. `pip install psycopg2==2.7.5` gestor de base de datos PostgreSQL
1. `pip install dj-database-url`  Para realizar la conexión entre el proyecto y el gestor de base de datos
1. `pip install python-decouple` Libreria facil de utilizar para acceder a las variables de entorno



