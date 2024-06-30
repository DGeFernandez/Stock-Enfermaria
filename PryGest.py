"""
Stock de Insumos de Enfermería Pediátrica 
en un Centro de Atención Comunitaria.-
Authors: Carolina Nazareno, 
        Alba Marlene Bareiro Servin,
        Claudio Alejandro Ortega,
        Diana Ivón Geppi Fernández.
Fecha: 2024
Version: 1.0
"""

import sqlite3
import os
import colorama

def limpiarPantalla():
    '''
    Función limpiarPantalla()
    Authors: Carolina Nazareno, 
             Alba Marlene Bareiro Servin, 
             Claudio Alejandro Ortega,
             Diana Ivón Geppi Fernández.
    Fecha: 2024
    Version: 1.0
    parametros:
        no requiere
    retorno:
        no retorna
    '''
    os.system('cls' if os.name == 'nt' else 'clear') # Función que limpia la pantalla para sistemas operativos Windows y Linux
    return

def identificarProfesional():
    '''
    Función identificarProfesional - Author: Diana Ivón Geppi Fernández - Fecha: 2024 - Version: 1.0 - parametros: no requiere
    '''
    profesionalValido = input("Ingrese su usuario, por favor: ")
    contraseniaValida = input("Ingrese su contraseña, por favor: ")
    intentos = 1

    while intentos <= 3:
        if profesionalValido == "stock" and contraseniaValida == "123":
            print("Bienvenido. Ud. tiene acceso al programa.")
            break
        else:
            intentos_restantes = 3 - intentos
            print(f"Usuario y contraseña incorrectos. Ingrese nuevamente su usuario y contraseña correcta. Le quedan {intentos_restantes} intentos.")
            profesionalValido = input("Ingrese su usuario, por favor: ")
            contraseniaValida = input("Ingrese su contraseña, por favor: ")
            intentos += 1

    if intentos > 3:
        print("Se han terminado los intentos. No accede al programa.")
        return False
    
    return True

def menu():
    limpiarPantalla()
    print(colorama.Fore.LIGHTGREEN_EX + "Stock de Enfermería Pediátrica en Centro de Atención Comunitaria".center(65))
    print("-" * 65)
    print(colorama.Fore.CYAN + "1.-" + colorama.Fore.RED + " Para agregar un insumo ")
    print(colorama.Fore.CYAN + "2.-" + colorama.Fore.RED + " Para modificar un insumo ")
    print(colorama.Fore.CYAN + "3.-" + colorama.Fore.RED + " Para eliminar un insumo ")
    print(colorama.Fore.CYAN + "4.-" + colorama.Fore.RED + " Para buscar un insumo ")
    print(colorama.Fore.CYAN + "5.-" + colorama.Fore.RED + " Para solicitar un insumo ")
    print(colorama.Fore.CYAN + "6.-" + colorama.Fore.RED + " Para listar los insumos ")
    print(colorama.Fore.CYAN + "7.-" + colorama.Fore.RED + " Para salir")
    op = input("Seleccione una opción: ")
    return op

# Función para ingresar un nuevo insumo
def ingresar_insumo():
    nombre = input("Ingrese el nombre del insumo: ")
    cantidad = int(input("Ingrese la cantidad del insumo: "))
    descripcion = input("Ingrese la descripción del insumo: ")
    
    conn = sqlite3.connect('centro_medico.db')
    c = conn.cursor()
    c.execute('INSERT INTO insumos (nombre, cantidad, descripcion) VALUES (?, ?, ?)', 
              (nombre, cantidad, descripcion))
    conn.commit()
    conn.close()
    print(f"Insumo '{nombre}' ingresado con éxito.")

def buscarInsumo():
    # Implementar funcionalidad de búsqueda
    pass

def modificarInsumo():
    # Implementar funcionalidad de modificación
    pass

def eliminarInsumo():
    # Implementar funcionalidad de eliminación
    pass

def listarInsumos():
    conn = sqlite3.connect('centro_medico.db')
    c = conn.cursor()
    c.execute('SELECT * FROM insumos')
    insumos = c.fetchall()
    conn.close()
    
    if insumos:
        print("Lista de insumos:")
        for insumo in insumos:
            print(f"ID: {insumo[0]}, Nombre: {insumo[1]}, Cantidad: {insumo[2]}, Descripción: {insumo[3]}")
    else:
        print("No hay insumos en el inventario.")

def solicitar_insumo():
    try:
        id_insumo = int(input("Ingrese el ID del insumo que desea solicitar: "))
        cantidad_solicitada = int(input("Ingrese la cantidad solicitada: "))
        
        conn = sqlite3.connect('centro_medico.db')
        c = conn.cursor()
        
        # Verificar si el insumo existe y obtener la cantidad actual
        c.execute('SELECT cantidad FROM insumos WHERE id = ?', (id_insumo,))
        resultado = c.fetchone()
        
        if resultado:
            cantidad_actual = resultado[0]
            if cantidad_actual >= cantidad_solicitada:
                nueva_cantidad = cantidad_actual - cantidad_solicitada
                c.execute('UPDATE insumos SET cantidad = ? WHERE id = ?', (nueva_cantidad, id_insumo))
                conn.commit()
                print(f"Solicitud realizada con éxito. Nueva cantidad de {id_insumo}: {nueva_cantidad}")
            else:
                print("No hay suficiente cantidad disponible para esta solicitud.")
        else:
            print("El insumo con el ID proporcionado no existe.")
        
        conn.close()
    except ValueError:
        print("Ingrese un valor numérico válido.")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")

# Programa Principal
colorama.init(convert=True)
if identificarProfesional():
    while True:
        opcion = menu()
        if opcion == "1":
            print("Ud. puede agregar un insumo.")
            ingresar_insumo()
        elif opcion == "2":
            print("Ud. puede modificar un insumo.")
            modificarInsumo()
        elif opcion == "3":
            print("Ud. puede eliminar un insumo.")
            eliminarInsumo()
        elif opcion == "4":
            print("Ud. puede buscar un insumo.")
            buscarInsumo()
        elif opcion == "5":
            print("Ud. puede solicitar un insumo.")
            solicitar_insumo()
        elif opcion == "6":
            print("Ud. puede listar los insumos.")
            listarInsumos()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("La opción no es válida! Presione enter para continuar.")
        input("Presione enter para continuar.")