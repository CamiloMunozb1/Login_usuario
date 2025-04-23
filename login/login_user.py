# Importación de las librerías necesarias
import sqlite3 # Para interactuar con la base de datos SQLite
import bcrypt  # Para manejar el cifrado de contraseñas
import re      # Para usar expresiones regulares en las validaciones


# Clase para gestionar la conexión a la base de datos
class IngresoDB:
    def __init__(self,ruta_db):
        try:
            # Intentar establecer la conexión con la base de datos SQLite
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor() # Crear un cursor para ejecutar consultas
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.") # Manejo de errores de base de datos
    
    def cierre_conexion(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()
        print("Cierre de la base de datos exitoso.")


# Clase para manejar el login de un usuario
class LoginUsuario:
    def __init__(self,conexion):
        self.conexion = conexion  # Conexión a la base de datos

    def acceso_usuario(self):
        try:
            # Solicitar al usuario que ingrese su correo y contraseña
            self.Email_user = str(input("Ingresa el email registrado: ")).strip()
            self.Password_user = str(input("Ingresa tu contraseña: ")).strip()

            # Expresiones regulares para validar el formato del correo y la contraseña
            verificador_email = r"[a-zA-Z-0-9]+@[a-zA-Z]+\.[a-z-.]+$"
            verifcador_password =  r"^[a-zA-Z0-9@#$%^&+=]{6,}$"

            # Validar que los campos no estén vacíos
            if not self.Email_user or not self.Password_user:
                print("No se pueden dejar campos sin rellenar.")
                return
            # Validar que el correo tenga un formato válido
            elif not re.fullmatch(verificador_email,self.Email_user):
                print("Ingresa un correo valido al registro.")
                return
            # Validar que la contraseña tenga el formato correcto
            elif not re.fullmatch(verifcador_password,self.Password_user):
                print("Ingresa una contraseña valida al del registro.")
                return
            
            # Consultar la base de datos para obtener la contraseña cifrada del usuario
            self.conexion.cursor.execute("SELECT Password_user FROM Email_contraseña WHERE Email_user = ? ",(self.Email_user,))
            resultado= self.conexion.cursor.fetchone() # Recuperar el resultado de la consulta

            if resultado:
                # Si existe un usuario, obtener su contraseña cifrada
                hash_password = resultado[0]
                # Verificar si la contraseña ingresada corresponde al hash almacenado
                if bcrypt.checkpw(self.Password_user.encode("utf-8"), hash_password):
                    print("Ingreso completo, sesion iniciada.") # Si la contraseña es correcta
                else:
                    print("Contraseña incorrecta.") # Si la contraseña es incorrecta
            else:
                print("Usuario no encontrado") # Si no se encuentra el usuario en la base de datos
        
        except Exception as error:
            # Capturar cualquier error y mostrarlo
            print(f"Error en la base de datos: {error}.")


# Ruta a la base de datos
ruta_db = r"TU_RUTA_DB"
# Crear una conexión a la base de datos
conexion = IngresoDB(ruta_db)