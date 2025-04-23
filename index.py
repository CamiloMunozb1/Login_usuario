# Importación de clases necesarias para manejar el registro de usuarios y login
from login.registro_usuario import IngresoDB, RegistroUsuarios
from login.login_user import IngresoDB, LoginUsuario

# Definir la ruta de la base de datos
ruta_db = r"TU_RUTA_DB"
# Crear una conexión con la base de datos
conexion = IngresoDB(ruta_db)

# Bucle principal del programa que permitirá al usuario interactuar
while True:
    # Imprimir el menú de opciones para el usuario
    print(
        """
            Login de usuario:
            1. Crea una cuenta.
            2. Ingresa a tu cuenta.
            3. Salir.
        """
    )

    try:
        # Solicitar al usuario que elija una opción
        usuario = str(input("Ingresa una opcion: "))
        
        # Si el usuario elige la opción 1, se procede al registro de un nuevo usuario
        if usuario == "1":
            ingreso = RegistroUsuarios(conexion)  # Crear instancia de RegistroUsuarios
            ingreso.ingreso_usuario()  # Llamar al método para registrar usuario
            
        # Si el usuario elige la opción 2, se procede al login del usuario existente
        elif usuario == "2":
            login = LoginUsuario(conexion)  # Crear instancia de LoginUsuario
            login.acceso_usuario()  # Llamar al método para verificar acceso
            
        # Si el usuario elige la opción 3, se termina el programa
        elif usuario == "3":
            print("Final de la sesion...")  # Mensaje de despedida
            break  # Salir del bucle, terminando el programa
        
        # Si el usuario ingresa una opción no válida
        else:
            print("Por favor, ingresar una opcion valida del 1 al 3.")

        # Pausar la ejecución hasta que el usuario presione Enter para continuar
        input("\nPresiona enter para continuar...")

    # Excepciones para capturar errores específicos de tipo ValueError
    except ValueError:
        print("Ingresa un valor correcto")
    # Excepciones generales para capturar cualquier error inesperado
    except Exception as error:
        print(f"Error en el programa: {error}.")
