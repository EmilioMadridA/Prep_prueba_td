# Proyecto Django: test_prueba_td

## Descripción del Proyecto

El proyecto `test_prueba_td` es una aplicación web construida con el framework Django que permite a los usuarios registrarse, iniciar sesión, gestionar perfiles y publicar productos. Este proyecto incluye un sistema de autenticación personalizado y permite a los usuarios agregar y listar productos.

## Configuración del Proyecto

### Requisitos

- Python 3.8+
- Django 4.2.11
- PostgreSQL

### Instalación

1. Clonar el repositorio:

   ```sh
   git clone https://github.com/tu_usuario/test_prueba_td.git
   cd test_prueba_td

2. Crear y activar un entorno virtual:

    python -m venv env
    # En Linux / WSL usar
    source env/bin/activate  
    # En Windows usar 
    `env\Scripts\activate`

3. Instalar las dependencias:

    pip install -r requirements.txt

4. Configurar la base de datos PostgreSQL en settings.py:

        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'prueba_td',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': 'tupuerto',
        }
    }

### ** Recuerda crear la base de datos en tu equipo o nube.

## Funcionalidades

- Registro de Usuario: Los usuarios pueden registrarse proporcionando un nombre de usuario, correo electrónico, dirección, teléfono y tipo de usuario (comprador o vendedor).
- Inicio de Sesión: Los usuarios pueden iniciar sesión usando su correo electrónico o nombre de usuario.
- Perfil de Usuario: Los usuarios autenticados pueden ver su perfil.
- Gestión de Productos: Los usuarios autenticados pueden agregar nuevos productos y ver una lista de productos disponibles.

## Autor ✒️

- **Emilio Madrid** - [EmilioMadridA](https://github.com/EmilioMadridA)

## Agradecimientos 🎁

- A todo el equipo de Desafio Latam y Talento Digital por la oportunidad de aprender y crecer en el campo del desarrollo web con Python y Django.
- A Brayan y Gustavo, por todo lo enseñado.
- A **Judith Vera** - [JudVera](https://github.com/JudVera) por ser la mejor partner en los trabajos en equipo!