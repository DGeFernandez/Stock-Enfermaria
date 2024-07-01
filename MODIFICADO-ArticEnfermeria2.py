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
#progra  principal

def buscar(diccionario,llave):
    if llave in diccionario:
        return diccionario[llave]
    else:
        return f"El ítem '{llave}' no se encuentra en la lista."

    
def modificar(diccionario,llave,dato):
    if llave in diccionario:
        diccionario[llave] = dato
        return f"El nuevo valor de '{llave}' es '{dato}'"
    else:
        return f"El item '{llave}' no se encuentra en la lista."
    
def eliminar(diccionario,llave):
    if llave in diccionario:
        del(diccionario[llave])
        return f"Item '{llave}' eliminado."
    else:
        return f"El item '{llave}' no se encuentra en la lista."


def main():
        while True:
            eleccion = int(input("Ingrese 1 para buscar, 2 para modificar, 3 para eliminar y 4 para salir: "))
            if eleccion == 1:
                llave = input("Ingrese el ítem a buscar: ")
                print(buscar(inventario_dicc, llave))
            elif eleccion == 2:
                llave = input("Ingrese el ítem a modificar: ")
                dato = input("Ingrese el nuevo valor: ")
                print(modificar(inventario_dicc, llave, dato))
            elif eleccion == 3:
                llave = input("Ingrese el ítem a eliminar: ")
                print(eliminar(inventario_dicc, llave))
            elif eleccion == 4:
                break
            else:
                print("Opción no válida.")

            eleccion = int(input("Ingrese 5 para imprimir toda la lista, 0 para volver al menú inicial, cualquier otro número para salir: "))
            if eleccion == 5:
                print("\nLista:")
                for key, value in inventario_dicc.items():
                    if isinstance(value, list):
                        value_str = ", ".join(value)
                    else:
                        value_str = value
                    print(f"{key}: {value_str}")
            elif eleccion == 0:
                continue
            else:
                break

    
if __name__ =="__main__":
    main()