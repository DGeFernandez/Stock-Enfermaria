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
# import sqlite3 
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
    insumos = leer_json()
    nombre = input("Ingrese el nombre del insumo: ")
    cantidad = int(input("Ingrese la cantidad del insumo: "))
    descripcion = input("Ingrese la descripción del insumo: ")
    
    insumo = {
        "id": len(insumos) + 1,
        "nombre": nombre,
        "cantidad": cantidad,
        "descripcion": descripcion
    }
    
    insumos.append(insumo)
    escribir_json(insumos)
    print(f"Insumo '{nombre}' ingresado con éxito.")
   
def modificar():
    '''Recibe el diccionario donde modificar las cosas, el item a buscar(llave)
    y el nuevo valor a ser asignado(dato), muestra mensajes de confirmacion o de error
    ydevuelve el diccionario modificado'''
    if "llave" in inventario_dicc:
        inventario_dicc["llave"] = "dato"
        print (f"El nuevo valor de '{"llave"}' es '{"dato"}'")
    else:
        print (f"El item '{"llave"}' no se encuentra en la lista.")
    return inventario_dicc
        
def eliminar(inventario_dicc,llave):
    '''Recibe el diccionario donde modificar las cosas, el item a eliminar(llave)
    muestra mensajes de confirmacion o de error y devuelve el diccionario modificado'''
    llave=input("Ingrese el insumo a eliminar: ")
    
    if llave in inventario_dicc:
        del(inventario_dicc[llave])
        print (f"Item '{llave}' eliminado.")
    else:
        print (f"El item '{llave}' no se encuentra en la lista.")
    return inventario_dicc
    
def buscar(inventario_dicc,llave):
    '''Recibe el diccionario en donde buscar las cosas y el item a buscar(llave)
    y lo muestra en pantalla, no retorna nada'''
    if llave in inventario_dicc:
        print (f"{inventario_dicc[llave]}")
    else:
        print (f"El ítem '{llave}' no se encuentra en la lista.")
def solicitar_insumo():
    insumos = leer_json()
    try:
        id_insumo = int(input("Ingrese el ID del insumo que desea solicitar: "))
        cantidad_solicitada = int(input("Ingrese la cantidad solicitada: "))
        
        for insumo in insumos:
            if insumo['id'] == id_insumo:
                if insumo['cantidad'] >= cantidad_solicitada:
                    insumo['cantidad'] -= cantidad_solicitada
                    escribir_json(insumos)
                    print(f"Solicitud realizada con éxito. Nueva cantidad de {insumo['nombre']}: {insumo['cantidad']}")
                else:
                    print("No hay suficiente cantidad disponible para esta solicitud.")
                break
        else:
            print("El insumo con el ID proporcionado no existe.")
    except ValueError:
        print("Ingrese un valor numérico válido.")

def listar(inventario_dicc):
    '''Recibe el diccionario, lo muestra, no retorna nada'''
    print("\nLista:")
    for key, value in inventario_dicc.items():
        if isinstance(value, list):
            value_str = ", ".join(value)
        else:
            value_str = value
        print(f"{key}: {value_str}")

def main():
    inventario_dicc = cargar_inv('inventario_dicc.json')


# Diccionario

inventario_dicc = {
    "sGuante": ["tamaño S", "tamaño M", "tamaño G"],
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

menuOpciones=menu() #esta linea es la que llama a la función menu() y guarda el valor de retorno en la variable menuOpciones
limpiarPantalla()

while menuOpciones != "0":
    if menuOpciones == "1":
        print("Ud. puede agregar un insumo.-")
        input("Presione enter para continuar.-") 
        # ingresar_insumo()
        pass
    elif menuOpciones =="2":
        print("Ud. puede modificar un insumo.-")
        input("Presione enter para continuar.-") 
        modificar()
        
    elif menuOpciones == "3":
        print("Ud. puede eliminar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
        eliminar(inventario_dicc,llave)
    elif menuOpciones == "4":
        insumo=input("Ud. puede buscar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
        buscar(inventario_dicc,llave)
    elif menuOpciones == "5":
        print("Ud. puede solicitar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    elif menuOpciones == "6":
        print("Ud. puede listar los insumo.-")
        input("Presione enter para continuar.-")
        listar(inventario_dicc)
    elif menuOpciones == "7":
        print("Gracias por utilizar el programa.-")
        input("Presione enter para salir.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    else: # Termina con else porque no inicie con True el bucle while, sino debo colocar break antes del else.-
        print("La opción no es válida!")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    #muestro nuevamente el menú para que el usuario pueda seleccionar otra opción
    #esta linea es la que llama a la función menu() y guarda el valor de retorno en la variable menuOpcionesstock