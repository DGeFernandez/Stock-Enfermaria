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
    
    print(colorama.Fore.CYAN +"1.-" + colorama.Fore.RED + "Para agregar un insumo ")
    print(colorama.Fore.CYAN +"2.-" + colorama.Fore.RED + "Para modificar un insumo ")
    print(colorama.Fore.CYAN +"3.-" + colorama.Fore.RED + "Para eliminar un insumo ")
    print(colorama.Fore.CYAN +"4.-" + colorama.Fore.RED + "Para buscar un insumo ")
    print(colorama.Fore.CYAN +"5.-" + colorama.Fore.RED + "Para solicitar un insumo ")
    print(colorama.Fore.CYAN +"6.-" + colorama.Fore.RED + "Para listar los insumo ")
    print(colorama.Fore.CYAN +"7.-" + colorama.Fore.RED + "Para salir presione 7.- ")
    
    opcion=input("Seleccione una opción: ")
    return opcion

# Leer inventario desde JSON
def leer_json():
    try:
        with open('inventario_dicc.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Guardar inventario en JSON
def escribir_json(data):
    with open('inventario_dicc.json', 'w') as file:
        json.dump(data, file, indent=4)

# Inicializar el inventario si el archivo JSON no existe
if not os.path.exists('inventario_dicc.json'):
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
    escribir_json(inventario_dicc)

def ingresar_insumo():
    """
    Author: Claudio Alejandro Ortega.
    Fecha: 2024
    Version: 1.0
    paramatros:
        no requiere
    """
    inventario = leer_json()
    nombre = input("Ingrese el nombre del insumo: ")
    descripcion = input("Ingrese la descripción del insumo: ")
    
    inventario[nombre] = descripcion
    
    escribir_json(inventario)
    print(f"Insumo '{nombre}' ingresado con éxito.")
   
def modificar():
    '''Recibe el diccionario donde modificar las cosas, el item a buscar(llave)
    y el nuevo valor a ser asignado(dato), muestra mensajes de confirmacion o de error
    y devuelve el diccionario modificado'''
    inventario = leer_json()
    llave = input("Ingrese el nombre del insumo a modificar: ")
    if llave in inventario:
        dato = input("Ingrese la nueva descripción del insumo: ")
        inventario[llave] = dato
        escribir_json(inventario)
        print (f"El nuevo valor de '{llave}' es '{dato}'")
    else:
        print (f"El item '{llave}' no se encuentra en la lista.")
    return inventario
        
def eliminar():
    '''Recibe el diccionario donde modificar las cosas, el item a eliminar(llave)
    muestra mensajes de confirmacion o de error y devuelve el diccionario modificado'''
    inventario = leer_json()
    llave = input("Ingrese el insumo a eliminar: ")
    
    if llave in inventario:
        del inventario[llave]
        escribir_json(inventario)
        print (f"Item '{llave}' eliminado.")
    else:
        print (f"El item '{llave}' no se encuentra en la lista.")
    return inventario
    
def buscar():
    '''Recibe el diccionario en donde buscar las cosas y el item a buscar(llave)
    y lo muestra en pantalla, no retorna nada'''
    inventario = leer_json()
    llave = input("Ingrese el insumo a buscar: ")
    if llave in inventario:
        print (f"{inventario[llave]}")
    else:
        print (f"El ítem '{llave}' no se encuentra en la lista.")

def solicitar_insumo():
    inventario = leer_json()
    nombre = input("Ingrese el nombre del insumo que desea solicitar: ")
    cantidad_solicitada = int(input("Ingrese la cantidad solicitada: "))
    
    if nombre in inventario:
        # Suponiendo que la descripción incluye la cantidad disponible
        descripcion = inventario[nombre]
        try:
            cantidad_disponible = int(descripcion.split()[-1])
            if cantidad_disponible >= cantidad_solicitada:
                nueva_cantidad = cantidad_disponible - cantidad_solicitada
                inventario[nombre] = f"{' '.join(descripcion.split()[:-1])} {nueva_cantidad}"
                escribir_json(inventario)
                print(f"Se ha solicitado {cantidad_solicitada} de {nombre}.")
            else:
                print(f"No hay suficiente cantidad de {nombre}.")
        except ValueError:
            print("La descripción del insumo no incluye una cantidad válida.")
    else:
        print("Insumo no encontrado.")

def listar_inventario():
    """
    Lista todo el inventario.
    """
    inventario = leer_json()
    if inventario:
        for categoria, items in inventario.items():
            print(f"{categoria}: {', '.join(items) if isinstance(items, list) else items}")
    else:
        print("El inventario está vacío.")

def main():
    '''
    Función main()
    Authors: Carolina Nazareno, 
             Alba Marlene Bareiro Servin, 
             Claudio Alejandro Ortega,
             Diana Ivón Geppi Fernández.
    Fecha: 2024
    Version: 1.0
    '''
    colorama.init()
    identificarProfesional()
    while True:
        opcion = menu()
        if opcion == '1':
            ingresar_insumo()
            enter_para_continuar()
        elif opcion == '2':
            modificar()
            enter_para_continuar()
        elif opcion == '3':
            eliminar()
            enter_para_continuar()
        elif opcion == '4':
            buscar()
            enter_para_continuar()
        elif opcion == '5':
            solicitar_insumo()
            enter_para_continuar()
        elif opcion == '6':
            listar_inventario()
            enter_para_continuar()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            enter_para_continuar()

if __name__ == "__main__":
    main()