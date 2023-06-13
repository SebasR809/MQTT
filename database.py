import pyodbc

def connection():
    server = "192.168.10.30\MSSQLSERVER01"
    database = "Pruebas"
    username = "soporte"
    password = "12345"
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +server+';DATABASE='+database+';UID='+username+';PWD=' + password)
        return conexion
    except Exception as e:
        print("Error connect to database sql: " + e)
