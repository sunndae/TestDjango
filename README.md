## Certamen numero 2 

Ciencias de la ingenieria 2: Lenguaje de programación

Para este proyecto en Django utilicé mi sistema operativo ubuntu, en caso de querer clonar mi repositorio, favor hacer lo siguiente para crear un entorno virtual

## Requisitos previos

- Python 3.10 o superior
- pip (el instalador de paquetes de Python)
- virtualenv (para crear entornos virtuales)

### 1. Crear y activar el entorno virtual

1. **Crear un directorio para el proyecto** (si aún no lo has hecho):
   ```
   mkdir Certamen2LP
   cd Certamen2LP
2. **Crear el entorno virtual**:

Con el entorno virtual activado, instala Django y otras dependencias necesarias:

    python3.10 -m venv venv

3. **Activar el entorno virtual**:

Es importante que activemos el entorno virtual creado para evitar problemas a la hora de empezar a programar.

    source venv/bin/activate

Una vez creamos y activamos nuestro entorno virtual, debemos instalar Django en nuestra carpeta del proyecto

4. **Instalación de Django usando pip**:

Cuando activamos el entorno virtual, debemos instalar el framework de Django para poder hacer nuestro proyecto despues
    
    pip install django

5. **Creación de un txt para tener las mismas dependencias**:

Esto nos va a ser bastante util cuando queramos subir nuestro proyecto a Docker.

    pip freeze > requirements.txt

6. **Creación del proyecto**:

  Una vez hagamos el archivo requirements.txt, vamos a crear finalmente nuestro proyecto de Django.

    django-admin startproject nombreDeTuProyecto

7. **Ejecución de nuestro proyecto**:
  Una vez que creemos nuestro proyecto en Django, debemos ubicar un archivo llamado **manage.py** el cual nos va a servir para ejecutar nuestro proyecto
      
     ```bash
     cd nombreDeTuProyecto

8. **Cuando entres a esta carpeta y te encuentres en el directorio donde está **manage.py** vas a ejecutar el siguiente comando**.

    python manage.py runserver
   

  Te aparecerá un mensaje en la consola de este estilo 

    June 15, 2024 - 00:17:03
    Django version 5.0.6, using settings 'Certamen2LDP.settings'
    Starting development server at http://IP:NumeroDePuerto/
    Quit the server with CONTROL-C.

y si haces 
**CTRL + Click* en la dirección **https://IP:NumeroDePuerto** 
se abrirá una ventana en el navegador con un mensaje en inglés que la instalación se ha realizado correctamente.

<br>
