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

import os
import colorama # type: ignore # para instalar colorama ( pip install colorama / pip3 install colorama)

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
    print(colorama.Fore.LIGHTGREEN_EX +"Stock de Enfermería Pediatría en Centro de Atención Comunitaria".center(45))
    print("-"*65)
    print(colorama.Fore.CYAN +"1.-" + colorama.Fore.RESET + "Para agregar un insumo ")
    print(colorama.Fore.CYAN +"2.-" + colorama.Fore.RESET + "Para buscar un insumo ")
    print(colorama.Fore.CYAN +"3.-" + colorama.Fore.RESET + "Para modificar un insumo ")
    print(colorama.Fore.CYAN +"4.-" + colorama.Fore.RESET + "Para eliminar un insumo ")
    print(colorama.Fore.CYAN +"5.-" + colorama.Fore.RESET + "Para solicitar un insumo ")
    print(colorama.Fore.CYAN +"6.-" + colorama.Fore.RESET + "Para listar los insumo ")
    op=input("Seleccione una opción: ")#le quito el int() porque no necesito que sea un número, sino un string
    return op

def agregarInsumo():
   print(""" Asegurese de colocar:
         > La medida del insumo a agregar
         > El tamaño del insumo a agregar
         > El cero (0) en caso de no tener tamaño o medida         
         """)

   nuevo_insumo= {
      "Nombre": input("Ingrese el insumo: "),
      "Tamaño": input("Ingrese el tamaño: "),
      "Medida": input("Ingrese la medida: "),
    }
   insumos.append(nuevo_insumo) # Con esto cargamos los datos
   
   enter_para_continuar()

def buscarInsuno():
    pass

def modificarInsumo():
    pass

#Variable
insumos= [
    {
      "Alcohol": "90°",
      "Guantes":[" s, m, g"],
      "Jeringas": ["10 cm³, 20 cm³, 5 cc, 3cc, 1 ml"],
      "Agujas":  ["25/8, 16/5, 40/8, 50/8"],
      "Algodón": "90",
      "Catéteres": "intravenosos",
      "Llave": "3 vías",
      "Butter": "flay",
      "Prolongadores": ["B14 y B17"],
      "Sondas vesicales":[ "10, 12, 14"],
      "Sondas naso-gástricas": ["30, 31"],
      "Máscaras": "p/nbz",
      "Máscaras de oxígeno": "niño",
      "Cánulas": "0",
      "Guías": "bomba",
      "Guías": "N.E",
      "Agua": "oxigenada"
    }
]

# Programa Principal

identificarProfesional()
menuOpciones=menu() #esta linea es la que llama a la función menu() y guarda el valor de retorno en la variable menuOpciones

while menuOpciones != "0":
    if menuOpciones == "1":
        print("Ud. puede agregar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú 
        agregarInsumo()
    elif menuOpciones =="2":
        print("Ud. puede modificar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    elif menuOpciones == "3":
        print("Ud. puede eliminar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    elif menuOpciones == "4":
        print("Ud. puede buscar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    elif menuOpciones == "5":
        print("Ud. puede listar un insumo.-")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    elif menuOpciones == "0":
        print("Gracias por utilizar el programa.-")
        input("Presione enter para salir.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    else: # Termina con else porque no inicie con True el bucle while, sino debo colocar break antes del else.-
        print("La opción no es válida! Presione enter para continuar.- ")
        input("Presione enter para continuar.-") #para poder leer el mensaje anterior antes de volver a mostrar el menú
    #muestro nuevamente el menú para que el usuario pueda seleccionar otra opción
    menuOpciones=menu() #esta linea es la que llama a la función menu() y guarda el valor de retorno en la variable menuOpcionesstock