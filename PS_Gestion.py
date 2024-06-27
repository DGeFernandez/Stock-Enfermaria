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


# Diccionario

insumos_dicc = {
    "Guantes": ["tamaño S"],
    "Guantes": ["tamaño M"],
    "Guantes": ["tamaño G"],
    "Jeringas": ["10 cm³"],
    "Jeringas": ["20 cm³"],
    "Jeringas": ["5 cc"],
    "Jeringas": ["3 cc"],
    "Jeringas": ["1 ml"],
    "Agujas": ["25/8"],
    "Agujas": ["16/5"],
    "Agujas": ["40/8"],
    "Agujas": ["50/8"],
    "Algodón": "plegado 500gr",
    "Alcohol etílico o etanol":"70%",
    "Alcohol etílico o etanol":"90%",
    "Catéteres intravenosos": "venoso central",
    "Catéteres intravenosos": "corto",
    "Llave de 3 vías": "con conector luer",
    "Llave de 3 vías": "sin conector luer",
    "Butter flay": "Catéter para venoclisis MARIPOSA VENOFIX G-23 20 mm.",
    "Prolongadores": "B17",
    "Prolongadores": "B14",
    "Sondas vesicales para niños": ["10"],
    "Sondas vesicales para niños": ["12"],
    "Sondas vesicales para niños": ["14"],
    "Sondas naso-gástricas para niños": ["30"],
    "Sondas naso-gástricas para niños": ["31"],
    "Máscaras p/nbz":"Flexible PVC",
    "Máscaras de oxígeno": "Gafas Nasales",
    "Mascarilla de oxígeno":" Simple",
    "Mascarilla de oxígeno":"con Reservorio",
    "Mascarilla de oxígeno": "tipo Venturi",
    "Cánulas": "Cánulas intravenosas",
    "Cánulas": "Cánulas nasales",
    "Guías de bomba":"para desplazamiento positivo",
    "Guías de bomba":"para lineares peristálticas",
    "Guías de bomba":"para peristálticas rotativas.",
    "Agua oxigenada": "peróxido de hidrógeno 30%",
    "Agua oxigenada": "peróxido de hidrógeno 50%",
    "Agua oxigenada": "peróxido de hidrógeno 9%",
    "Pervinox solución":"Povidona-Iodo",
    "Pervinox solución jabonosa": "Betadine Povidona-Iodo ",
    "Gasas": "Gasa estéril",
    "Gasas": "Gasa no estéril",
    "Gasas": "Gasa hidrófila",
    "Gasas": "Gasa adhesiva",
    "Gasas": "Gasa de malla",
    "Apósitos":  "Apósitos Hidrocoloides",
    "Apósitos":  "Apósitos de Silicona.",
    "Baja lenguas de madera": "Depresor lingual de madera"
}

print(insumos_dicc)


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
            # Implementar funcionalidad de solicitud de insumo
        elif opcion == "6":
            print("Ud. puede listar los insumos.")
            listarInsumos()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("La opción no es válida! Presione enter para continuar.")
        input("Presione enter para continuar.")
