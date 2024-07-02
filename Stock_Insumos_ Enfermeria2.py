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
import colorama # type: ignore # para instalar colorama ( pip install colorama / pip3 install colorama)
import json

def enter_para_continuar():
    input("Presione enter para continuar") # Se detiene el código un instante y se debe presionar enter para continuar
    

def limpiarPantalla():
    '''
    Función limpiarPantalla()
    Authors: Carolina Nazareno, 
             Alba Marlene Bareiro Servin, 
             Claudio Alejandro Ortega,
             Diana Ivón Geppi Fernández.
    Fecha: 2024
    Version: 1.0
    paramatros:
        no requiere
    retorno:
        retorna la opción seleccionada por el usuario
    '''
    os.system('cls' if os.name == 'nt' else 'clear') # Función que limpia la pantalla para sistemas operativos Windows y Linux
    return

def identificarProfesional():
    '''
    Función identificarProfesional()
    Author: Diana Ivón Geppi Fernández.
    Fecha: 2024
    Version: 1.0
    paramatros:
        no requiere
    '''
profesionalValido = input("Ingrese su usuario, por favor: ")
contraseniaValida = input("Ingrese su contraseña, por favor: ")
intentos = 1

while intentos <= 3:
    if profesionalValido == "stock" and contraseniaValida == "1234":
        print("Bienvenido. Ud. tiene acceso al programa.")
        break
    else:
        print(f"Usuario y contraseña incorrectos. Ingrese nuevamente su usuario y contraseña correcta. Le quedan {3 - intentos} intentos.")
        profesionalValido = input("Ingrese su usuario, por favor: ")
        contraseniaValida = input("Ingrese su contraseña, por favor: ")
        intentos += 1

if intentos > 3:
    print("Se han terminado los intentos. No accede al programa.")

def menu():
    '''
    Función menu()
    Authors: Carolina Nazareno, 
             Alba Marlene Bareiro Servin, 
             Claudio Alejandro Ortega,
             Diana Ivón Geppi Fernández.
    Fecha: 2024
    Version: 1.0
    paramatros:
        no requiere
    retorno:
        retorna la opción seleccionada por el usuario
    '''
    limpiarPantalla()
    print(colorama.Fore.LIGHTGREEN_EX +"-"*65 +colorama.Fore.RESET )
    print(colorama.Fore.LIGHTGREEN_EX +"Stock de Enfermería Pediatría en Centro de Atención Comunitaria".center(45))
    print(colorama.Fore.LIGHTGREEN_EX +"-"*65 + colorama.Fore.RESET)
    
    print(colorama.Fore.CYAN +"1.-" + colorama.Fore.RESET + "Para agregar un insumo ")
    print(colorama.Fore.CYAN +"2.-" + colorama.Fore.RESET + "Para modificar un insumo ")
    print(colorama.Fore.CYAN +"3.-" + colorama.Fore.RESET + "Para eliminar un insumo ")
    print(colorama.Fore.CYAN +"4.-" + colorama.Fore.RESET + "Para buscar un insumo ")
    print(colorama.Fore.CYAN +"5.-" + colorama.Fore.RESET + "Para solicitar un insumo ")
    print(colorama.Fore.CYAN +"6.-" + colorama.Fore.RESET + "Para listar los insumo ")
    print(colorama.Fore.CYAN +"7.-" + colorama.Fore.RESET + "Para salir presione 7.- ")
    
    opcion=input("Seleccione una opción: ")
    return opcion

def cargarInsumos():
    pass

def guardarInsumos():
    pass

def ingresar_insumo():
    """
     Author: Claudio Alejandro Ortega.
    Fecha: 2024
    Version: 1.0
    paramatros:
        no requiere
       """
    nombre = input("Ingrese el nombre del insumo: ")
    cantidad = int(input("Ingrese la cantidad del insumo: "))
    descripcion = input("Ingrese la descripción del insumo: ")
    
    conn = sqlite3.connect('centro_medico.db') # Esto llama a una base de datos que no existe por eso da error. Será así?
    c = conn.cursor()
    c.execute('INSERT INTO insumos (nombre, cantidad, descripcion) VALUES (?, ?, ?)', 
              (nombre, cantidad, descripcion))
    conn.commit()
    conn.close()
    print(f"Insumo '{nombre}' ingresado con éxito.")
   
def modificar(diccionario, llave, dato):
    """
     Author:Carolina Nazareno.
    Fecha: 2024
    Version: 1.0
    paramatros:
        requiere parámetros
       """
    llave= input("Ingrese insumo a modificar: ")
    dato= input("Ingrese la descripción a modificar: ")
    if diccionario.update({llave}) == dato:
        print(f"El nuevo valor de '{llave}' es '{dato}'")
    else:
        return (f"El item '{llave}' no se encuentra en la lista.")
        
def eliminar(diccionario,llave):
         
    if llave in diccionario:
        del(diccionario[llave])
        return f"Item '{llave}' eliminado."
    else:
        return f"El item '{llave}' no se encuentra en la lista."
    
def buscar(diccionario,llave):
    llave=input("Ingrese el insumo a buscar: ")
    if llave in diccionario:
       diccionario[llave]= llave
    else:
        return f"El insumo '{llave}' no se encuentra en la lista."
def solicitar_insumo():
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

inventario_dicc = {
    "Guantes": ["tamaño S", "tamaño M", "tamaño G"],
    "Jeringas": ["10 cm³", "20 cm³", "5 cc", "3 cc", "1 ml"],
    "Agujas": ["25/8", "16/5", "40/8", "50/8"],
    "Algodón": "plegado 500gr",
    "Alcohol etílico o etanol": ["70%", "90%"],
    "Catéteres intravenosos": ["venoso central", "corto"],
    "Llave de 3 vías": ["con conector luer", "sin conector luer"],
    "Butter flay": "Catéter para venoclisis MARIPOSA VENOFIX G-23 20 mm.",
    "Prolongadores": ["B17", "B14"],
    "Sondas vesicales para niños": ["10", "12", "14"],
    "Sondas naso-gástricas para niños": ["30", "31"],
    "Máscaras p/nbz": "Flexible PVC",
    "Máscaras de oxígeno": ["Gafas Nasales", "Simple", "con Reservorio", "tipo Venturi"],
    "Cánulas": ["Cánulas intravenosas", "Cánulas nasales"],
    "Guías de bomba": ["para desplazamiento positivo", "para lineares peristálticas", "para peristálticas rotativas"],
    "Agua oxigenada": ["peróxido de hidrógeno 30%", "peróxido de hidrógeno 50%", "peróxido de hidrógeno 9%"],
    "Pervinox solución": "Povidona-Iodo",
    "Pervinox solución jabonosa": "Betadine Povidona-Iodo",
    "Gasas": ["Gasa estéril", "Gasa no estéril", "Gasa hidrófila", "Gasa adhesiva", "Gasa de malla"],
    "Apósitos": ["Apósitos Hidrocoloides", "Apósitos de Silicona"],
    "Baja lenguas de madera": "Depresor lingual de madera"
}



# Programa Principal

identificarProfesional()
diccionario = cargarInsumos()
menuOpciones=menu() #esta linea es la que llama a la función menu() y guarda el valor de retorno en la variable menuOpciones
limpiarPantalla()

while menuOpciones != "0":
    if menuOpciones == "1":
        print("Ud. puede agregar un insumo.-")
        input("Presione enter para continuar.-") 
        ingresar_insumo()
    elif menuOpciones =="2":
        print("Ud. puede modificar un insumo.-")
        input("Presione enter para continuar.-") 
        modificar(diccionario)
        
    elif menuOpciones == "3":
        print("Ud. puede eliminar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
        eliminar(diccionario)
    elif menuOpciones == "4":
        insumo=input("Ud. puede buscar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
        buscar(diccionario,insumo)
    elif menuOpciones == "5":
        print("Ud. puede solicitar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    elif menuOpciones == "6":
        print("Ud. puede listar los insumo.-")
        input("Presione enter para continuar.-")
        listarInsumos()
    elif menuOpciones == "7":
        print("Gracias por utilizar el programa.-")
        input("Presione enter para salir.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    else: # Termina con else porque no inicie con True el bucle while, sino debo colocar break antes del else.-
        print("La opción no es válida!")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    #muestro nuevamente el menú para que el usuario pueda seleccionar otra opción
    #esta linea es la que llama a la función menu() y guarda el valor de retorno en la variable menuOpcionesstock