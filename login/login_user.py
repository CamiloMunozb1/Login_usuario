import sqlite3
import bcrypt
import re

class IngresoDB:
    def __init__(self,ruta_db):
        try:
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
    
    def cierre_conexion(self):
        self.conn.close()
        print("Cierre de la base de datos exitoso.")

class LoginUsuario:
    def __init__(self,conexion):
        self.conexion = conexion

    def acceso_usuario(self):
        try:

            self.Email_user = str(input("Ingresa el email registrado: ")).strip()
            self.Password_user = str(input("Ingresa tu contraseña: ")).strip()

            verificador_email = r"[a-zA-Z-0-9]+@[a-zA-Z]+\.[a-z-.]+$"
            verifcador_password =  r"^[a-zA-Z0-9@#$%^&+=]{6,}$"

            if not self.Email_user or not self.Password_user:
                print("No se pueden dejar campos sin rellenar.")
                return
            elif not re.fullmatch(verificador_email,self.Email_user):
                print("Ingresa un correo valido al registro.")
                return
            elif not re.fullmatch(verifcador_password,self.Password_user):
                print("Ingresa una contraseña valida al del registro.")
                return
            
            self.conexion.cursor.execute("SELECT Password_user FROM Email_contraseña WHERE Email_user = ? ",(self.Email_user,))
            resultado= self.conexion.cursor.fetchone()
            if resultado:
                hash_password = resultado[0]

                if bcrypt.checkpw(self.Password_user.encode("utf-8"), hash_password):
                    print("Ingreso completo, sesion iniciada.")
                else:
                    print("Contraseña incorrecta.")
            else:
                print("Usuario no encontrado")
        
        except Exception as error:
            print(f"Error en la base de datos: {error}.")


ruta_db = r"C:\Users\POWER\registros_usuarios.db"
conexion = IngresoDB(ruta_db)