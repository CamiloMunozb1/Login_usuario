## Proyecto de Login y Registro de Usuarios

Este es un proyecto que implementa un sistema de registro y login de usuarios utilizando SQLite para la base de datos y bcrypt para la gestión segura de contraseñas.

## Descripción

Este proyecto permite a los usuarios:
1. Crear una cuenta, proporcionando un nombre de usuario, apellido, correo electrónico y una contraseña.
2. Iniciar sesión proporcionando su correo electrónico y contraseña.
3. Utiliza hashing de contraseñas (con bcrypt) para almacenar las contraseñas de manera segura.
4. La base de datos se guarda en un archivo SQLite.

## Tecnologías

- Python: El lenguaje de programación utilizado para la implementación del sistema.
- SQLite: Base de datos ligera para almacenar la información de los usuarios.
- bcrypt: Para el cifrado de contraseñas y asegurar que las contraseñas no se almacenen en texto claro.
- Expresiones regulares (regex): Para la validación del correo electrónico y la contraseña.

## Instalación

Para comenzar con el proyecto, sigue estos pasos:
1. Clonar el repositorio:

       git clone https://github.com/tu-usuario/nombre-del-repositorio.git

2. Crear un entorno virtual (opcional pero recomendado):

       python -m venv venv

3. Activar el entorno virtual.
4. Instalar las dependencias: Asegúrate de tener bcrypt y sqlite3 instalados:

       pip install bcrypt

## USO

1. Configura la base de datos: Asegúrate de que el archivo de base de datos registros_usuarios.db esté en la ruta correcta o crea uno nuevo utilizando SQLite.
2. Ejecuta el programa: Ejecuta el archivo principal index.py para iniciar el sistema de login y registro.
3. El programa te permitirá elegir entre las siguientes opciones:
     -Crear una cuenta: Se te pedirá que ingreses el nombre de usuario, apellido, correo electrónico y una contraseña.
     -Iniciar sesión: Ingresarás tu correo electrónico y contraseña para acceder a tu cuenta.
     -Salir: Para terminar el programa.

## Notas

  -Asegúrate de tener la base de datos SQLite correctamente configurada antes de ejecutar el programa.
  
  -Este proyecto es un ejemplo básico y está diseñado para ser usado en un entorno de pruebas o local. No es adecuado para      producción sin realizar ajustes adicionales en la seguridad y escalabilidad.

## AUTOR

  Desarrollado por Juan camilo Muñoz.

## Licencia

  Este proyecto está bajo la Licencia MIT.


