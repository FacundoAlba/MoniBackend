# Proyecto Django con Docker

Este es un proyecto Django configurado para ejecutarse en contenedores Docker utilizando Docker Compose.

## Prerrequisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalación

Sigue los pasos a continuación para configurar y ejecutar el proyecto:

1. Crea las migraciones de la base de datos:
    ```sh
    docker compose run web python manage.py makemigrations
    ```

2. Ejecuta las migraciones de la base de datos:
    ```sh
    docker compose run web python manage.py migrate
    ```
3. Levanta los contenedores Docker:
    ```sh
    docker compose up
    ```

4. (Opcional) Crea un superusuario:
    ```sh
    docker compose run web python manage.py createsuperuser
    ```

5. Accede a la aplicación en tu navegador web en `http://localhost:8000`.

## Comandos útiles

- Para levantar los contenedores en segundo plano:
    ```sh
    docker compose up -d
    ```

- Para detener los contenedores:
    ```sh
    docker compose down
    ```

- Para reconstruir los contenedores después de realizar cambios en el Dockerfile o en `requirements.txt`:
    ```sh
    docker compose up --build
    ```

- Para ver los logs de los contenedores:
    ```sh
    docker compose logs
    ```
- Para ejecutar comandos de Django en el contenedor `web`:
    ```sh
    docker compose run web <comando_django>
    ```

## Notas adicionales

- Asegúrate de que tu archivo `requirements.txt` esté actualizado con todas las dependencias necesarias para tu proyecto.
- Puedes personalizar las configuraciones de Docker y Django según tus necesidades específicas.

---

¡Gracias por usar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactar al mantenedor del proyecto.
