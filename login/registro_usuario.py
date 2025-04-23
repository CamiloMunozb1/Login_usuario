# Importación de librerías necesarias
import sqlite3 # Para interactuar con la base de datos SQLite
import bcrypt  # Para el cifrado de contraseñas
import re      # Para validaciones con expresiones regulares

# Clase para gestionar la conexión a la base de datos
class IngresoDB:
    def __init__(self, ruta_db):
        try:
            # Establecer la conexión a la base de datos
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()  # Crear un cursor para ejecutar consultas
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.") # Manejo de errores de base de datos
    
    def cierre_conexion(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()
        print("Cierre de la base de datos exitoso.")

# Clase para manejar el registro de nuevos usuarios
class RegistroUsuarios:
    def __init__(self,conexion):
        self.conexion = conexion # Conexión a la base de datos

    def ingreso_usuario(self):
        try:
            # Solicitar información al usuario para el registro
            self.Nombre_usuario = str(input("Ingresa el nombre de usuario: ")).strip()
            self.Apellido_usuario = str(input("Ingresa el apellido de tu usuario: ")).strip()
            self.Email_user = str(input("Ingresa tu correo electronico: ")).strip()
            self.Password_user = str(input("Ingresa una contraseña (6 caracteres max): ")).strip()
            
            # Expresiones regulares para validar el formato de correo y contraseña
            verificador_email = r"[a-zA-Z-0-9]+@[a-zA-Z]+\.[a-z-.]+$"
            verifcador_password =  r"^[a-zA-Z0-9@#$%^&+=]{6,}$"

            # Cifrar la contraseña con bcrypt
            cifrado = bcrypt.hashpw(self.Password_user.encode("utf-8"),bcrypt.gensalt())

            # Validar que todos los campos estén completos y sean correctos
            if not all ([self.Nombre_usuario, self.Apellido_usuario, self.Email_user, self.Password_user]):
                print("Todos los campos deben estar completos.")
            elif not re.fullmatch(verificador_email, self.Email_user):
                print("Ingresa un correo valido.")
                return
            elif not re.fullmatch(verifcador_password, self.Password_user):
                print("Ingresa una contraseña valida.")
                return

            # Insertar el nombre y apellido en la tabla de usuarios
            self.conexion.cursor.execute("INSERT INTO Nombre_usuarios(Nombre_usuario,Apellido_usuario) VALUES (?,?)",(self.Nombre_usuario,self.Apellido_usuario))
            self.conexion.conn.commit() # Confirmar la operación en la base de datos

            # Obtener el ID del usuario recién registrado
            self.conexion.cursor.execute("SELECT Usuario_ID FROM Nombre_usuarios WHERE Nombre_usuario = ?",(self.Nombre_usuario,))
            Usuario = self.conexion.cursor.fetchone()
            if Usuario:
                Usuario_ID = Usuario[0]
                # Insertar el correo electrónico y la contraseña cifrada en la tabla correspondiente
                self.conexion.cursor.execute("INSERT INTO Email_Contraseña(Email_user,Password_user,Usuario_ID) VALUES(?,?,?)",(self.Email_user,cifrado,Usuario_ID))
                self.conexion.conn.commit() # Confirmar la operación en la base de datos
            print("Datos registrados en la base de datos")

        except Exception as error:
            # Capturar cualquier error y mostrarlo
            print(f"Error en el programa: {error}.")


# Ruta a la base de datos
ruta_db = r"TU_RUTA_DB"
# Crear una conexión a la base de datos
conexion = IngresoDB(ruta_db)



