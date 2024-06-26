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
#Comente la linea 27 para que no imprima siempre toda la lista.
# print(inventario_dicc)

#progra  principal


#Aca tenes que definir la funcion, van solamente los parametros que necesites que ingresen,
#podes ponerle el nombre que quieras porque se pasan por referencia, es costumbre poner nombres
#simples y claros pero que definan bien lo que es.

def buscar(diccionario,busqueda):
    if busqueda in diccionario:
        return diccionario[busqueda]
    else:
        return f"El ítem '{busqueda}' no se encontró en el diccionario."
    
#Aca preguntamos que queres buscar, lo guardamos en la variable dato.
dato = input("Ingrese el item a buscar: ")
#y aca imprimimos lo que nos devuelva la funcion que hicimos antes, aca si tenemos que poner bien los nombres porque
#esto es lo que mandamos a la funcion.
print(buscar(inventario_dicc,dato))
  

'''
Aca voy a poner el codigo como estaba antes, asi lo tenes para diferenciar y ver los cambios:
def buscar(Guantes):
    if Guantes in inventario_dicc:
        return inventario_dicc[Guantes]
    else:
        return f"El ítem '{Guantes}' no se encontró en el diccionario."
  
'''