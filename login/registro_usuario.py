import sqlite3
import bcrypt
import re

class IngresoDB:
    def __init__(self, ruta_db):
        self.conn = sqlite3.connect(ruta_db)
        self.cursor = self.conn.cursor()
    
    def cierre_conexion(self):
        self.conn.close()
        print("Cierre de la base de datos exitoso.")

class RegistroUsuarios:
    def __init__(self,conexion):
        self.conexion = conexion

    def ingreso_usuario(self):
        try:
            self.Nombre_usuario = str(input("Ingresa el nombre de usuario: ")).strip()
            self.Apellido_usuario = str(input("Ingresa el apellido de tu usuario: ")).strip()
            self.Email_user = str(input("Ingresa tu correo electronico: ")).strip()
            self.Password_user = str(input("Ingresa una contraseña (6 caracteres): ")).strip()
            
            verificador_email = r"[a-zA-Z-0-9]+@[a-zA-Z]+\.[a-z-.]+$"
            verifcador_password =  r"^[a-zA-Z0-9@#$%^&+=]{6,}$"
            cifrado = bcrypt.hashpw(self.Password_user.encode("utf-8"),bcrypt.gensalt())

            if not all ([self.Nombre_usuario, self.Apellido_usuario, self.Email_user, self.Password_user]):
                print("Todos los campos deben estar completos.")
            elif not re.fullmatch(verificador_email, self.Email_user):
                print("Ingresa un correo valido.")
                return
            elif not re.fullmatch(verifcador_password, self.Password_user):
                print("Ingresa una contraseña valida.")
                return

            self.conexion.cursor.execute("INSERT INTO Nombre_usuarios(Nombre_usuario,Apellido_usuario) VALUES (?,?)",(self.Nombre_usuario,self.Apellido_usuario))
            self.conexion.conn.commit()

            self.conexion.cursor.execute("SELECT Usuario_ID FROM Nombre_usuarios WHERE Nombre_usuario = ?",(self.Nombre_usuario,))
            Usuario = self.conexion.cursor.fetchone()
            if Usuario:
                Usuario_ID = Usuario[0]
                self.conexion.cursor.execute("INSERT INTO Email_Contraseña(Email_user,Password_user,Usuario_ID) VALUES(?,?,?)",(self.Email_user,cifrado,Usuario_ID))
                self.conexion.conn.commit()
            print("Datos registrados en la base de datos")

        except Exception as error:
            print(f"Error en el programa: {error}.")


ruta_db = r"C:\Users\POWER\registros_usuarios.db"
conexion = IngresoDB(ruta_db)



