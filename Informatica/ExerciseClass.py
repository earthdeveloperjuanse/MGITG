# Exercise class 11/08/2023
# Juan Sebastián Hernández Santana
# Maestría en Gestión de la Información y Tecnologías Geoespaciales

import mysql.connector

conexion = mysql.connector.connect(host = 'localhost', user = 'root', password = '')
sql = conexion.cursor()

# Funciones del Sistema Gestor de Bases de datos

def show_dataBases(sql):
    sql.execute('SHOW DATABASES')
    for db in sql:
        print(db)

def create_dataBase(bd):
    try:
        sql.execute('CREATE DATABASE IF NOT EXISTS {}'.format(bd))
        print('Base de datos "{}" creada satisfactoriamente.'.format(bd))
    except mysql.connector.Error as err:
        print('Error al crear la base de datos {}'.format(err))

def list_tablesDB(bd):
    try:
        sql.execute('USE {}'.format(bd))
        sql.execute('SHOW TABLES')
        for table in sql:
            print(table)

        input_describe = input('¿Desea saber la estructura de una tabla? 1. Si, 0: No')
        if input_describe == '1':
            table = input('Ingrese nombre de la tabla: ')
            sql.execute('DESCRIBE {}'.format(table))
            for field in sql:
                print(field)

    except mysql.connector.Error as err:
        print('Error al listar las tablas {}'.format(err))

def create_table(bd, table):
    try:
        sql.execute('CREATE TABLE IF NOT EXISTS {}.{}(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, value FLOAT(10), dateData DATETIME(2), latitude FLOAT(10), longitude FLOAT(10))'.format(bd, table))
        print('Tabla "{}" creada satisfactoriamente.'.format(table))
    except mysql.connector.Error as err:
        print('Error al crear la tabla {}'.format(err))

def addData(sql, bd, table):
    x, y = input_coordinates()
    value = input_measure()
    dateData = input('Fecha de medición: ')
    try:
        sqlinsert = 'INSERT INTO {}.{} (value, dateData, latitude, longitude) VALUES ({}, {}, {}, {})'.format(bd, table, value, dateData, x, y)
        sql.execute(sqlinsert)
        conexion.commit()
        print('Datos adicionados correctamente.')
    except mysql.connector.Error as err:
        print('Error al adicionar los datos {}'.format(err))

def displayData(bd):
    sql.execute('USE {}'.format(bd))
    

# Funciones de la herramienta creada

def input_coordinates():
    while True:
        try:
            x = float(input('Ingrese latitud: '))
            y = float(input('Ingrese longitud: '))

            if (-90 <= x <= 90) and (-180 <= y <= 180):
                return x, y
            else:
                print('Las coordenadas ingresadas están fuera de los límites.')
        except ValueError:
            print('Ingrese un valor de coordenadas válido.')

def input_measure():
    while True:
        try:
            value = float(input('Ingrese medición: '))

            if value > 0:
                return value
            else:
                print('La medición está fuera de los límites.')
        except ValueError:
            print('Ingrese un valor de medición válido.')

def display_menu():
    print('INFORMÁTICA APLICADA A LA INFORMACIÓN GEOGRÁFICA \nMENÚ PRINCIPAL \n1. Mostrar bases de datos de una conexión \n2. Crear bases de datos \n3. Crear tabla \n4. Agregar datos a tabla \n5. Listar tablas de base de datos \n6. Salir')

def input_option():
    while True:
        try:
            option = int(input('Seleccione una opción: '))
            if 1 <= option <= 6:
                return option
            else:
                print('Opción invalida. Intente nuevamente.')
        except ValueError:
            print('Opción invalida. Intente nuevamente.')

def select_option(option):
    if option == 1:
        show_dataBases(sql)
    elif option == 2:
        bd = input('Nombre de la base de datos a agregar: ')
        create_dataBase(bd)
    elif option == 3:
        bd = input('Nombre de la base de datos a agregar: ')
        table = input('Nombre de la tabla a agregar: ')
        create_table(bd, table)
    elif option == 4:
        bd = input('Nombre de la base de datos a agregar: ')
        table = input('Nombre de la tabla a agregar: ')
        addData(sql, bd, table)
    elif option == 5:
        bd = input('Nombre de la base de datos a agregar: ')
        list_tablesDB(bd)

def main():
    display_menu()
    while True:
        option = input_option()
        if option == 6:
            print('Vuelva pronto.')
            break
        else:
            select_option(option)

if __name__ == '__main__':
    main()