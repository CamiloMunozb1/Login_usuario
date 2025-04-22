from login.registro_usuario import IngresoDB, RegistroUsuarios
from login.login_user import IngresoDB, LoginUsuario

ruta_db = r"C:\Users\POWER\registros_usuarios.db"
conexion = IngresoDB(ruta_db)

while True:
    print(
        """
            Login de usuario:
            1. Crea una cuenta.
            2. Ingresa a tu cuenta.
            3. Salir.
        """
    )

    try:

        usuario = str(input("Ingresa una opcion: "))
        if usuario == "1":
            ingreso = RegistroUsuarios(conexion)
            ingreso.ingreso_usuario()
        elif usuario == "2":
            login = LoginUsuario(conexion)
            login.acceso_usuario()
        elif usuario == "3":
            print("Final de la sesion...")
            break
        else:
            print("Por favor, ingresar una opcion valida del 1 al 3.")

        input("\nPresiona enter para continuar...")
    
    except ValueError:
        print("Ingresa un valor correcto")
    except Exception as error:
        print(f"Error en el programa: {error}.")

