import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="db",               
        user="root",
        password="senha_secreta",
        database="sistema_login"
    )