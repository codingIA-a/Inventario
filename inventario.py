

"""
Crear un simulador de inventario para una tienda ficticia. 
El programa debe permitir agregar productos y mostrar el inventario .
Para resolver esto deberá:
1.-Crear  una función para agregar productos al inventario.
2.-Crear una función para mostrar TODO el inventario.
3.-Deberá integrar las funciones al menú_principal() para realizar la operación correspondiente tomando la entrada de usuario
"""


inventario = {
    'laptop' : {'precio': 1000, 'cantidad':10},
    'smartphone':{'precio' : 500, 'cantidad':20},
    'teclado': {'precio': 50, 'cantidad': 30}
}
#Crear una función que reciba 3 parámetros. El primer parámetro será el nombre del producto, 
# el segundo el precio y el tercero la cantidad
#La función deberá validar si el parametro que representa el nombre del producto existe dentro del inventario
#Si no existe deberá agregar el nuevo producto con su respectivo precio y cantidad
#Si el producto existe, deberá sumar el stock existente y actualizar el precio de ser necesario



#función agregar producto




#función mostrar inventario

def menu_principal():
    while True:
        print("\n----- Menú Principal -----")
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        
menu_principal()




