"""
Práctico Nº1 de la materia Programación en Python
Implementación de un inventario sencillo mediante el uso de listas de diccionarios y mostrando resultados con tabulate.

"""
from tabulate import tabulate as t
from IPython.display import clear_output
import sys
inventario = []

# Agrega productos al inventario con propósito de prueba
inventario.append({"nombre": "Laptop", "cantidad": 5, "precio": 1200})
inventario.append({"nombre": "Mouse", "cantidad": 10, "precio": 25})
inventario.append({"nombre": "Teclado", "cantidad": 8, "precio": 75})

def mostrar_menu():
    print("--GESTOR DE INVENTARIO--")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Modificar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")


def mostrar_inventario():
    """
    Muestra el inventario en formato de tabla.
    """
    if not inventario:  # Verifica si el inventario está vacío
        print("No hay productos en el inventario.")
    else:
        print(" -- Inventario: -- ")
        print(t(inventario, headers = "keys", tablefmt="github"))


def agregar_producto():
    while True:
        try: #Ingresar el nombre del producto, siempre que este no exista en el inventario
            nombre = input("Ingrese el nombre del producto: ").capitalize().strip() 
            if any(producto["nombre"] == nombre for producto in inventario):
                print("El producto ya existe en el inventario. Por favor ingrese un producto válido o Ctrl + D para no argegar ningún producto")
            else :
                break
        except EOFError:
            return

    
    while True:
        try: #Ingresar la cantidad de productos, 0 debe ser un valor posible x  ej para cuando un producto se queda sin stock 
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if (cantidad < 0):
                print("La cantidad debe ser un número positivo o 0. Por favor ingrese una cantidad válida o Ctrl + D para no argegar ningún producto")
            else:
                break
        except EOFError:
            return
        except ValueError:
            print("La cantidad debe ser un número válido. Por favor ingrese una cantidad válida o Ctrl + D para no argegar ningún producto")

    
    while True:
        try: #Ingresar el precio del producto, siempre que sea un número positivo
            precio = float(input("Ingrese el precio del producto: ")) 
            if precio <= 0:
                print("El precio debe ser un número positivo mayor que 0. Por favor ingrese un precio válido o Ctrl + D para no argegar ningún producto")
            else:
                break
        except ValueError:
            print("El precio debe ser un número válido. Por favor ingrese un precio válido o Ctrl + D para no argegar ningún producto")
        except EOFError:
            return

    # Agrego el nuevo producto al inventario
    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio":precio})
    print(f"El producto {nombre} ha sido agregado al inventario.")

def modificar_cantidad():
    """
    Modifica la cantidad de un producto existente en el inventario.
    """
    try:  # Pido al usuario que ingrese el producto al cual hay que modificarle la cantidad en el inventario, siemore que dicho producto exista
        while True:

            nombre = input("Ingrese el nombre del producto a modificar: ").capitalize().strip() 
            if any(producto["nombre"] == nombre for producto in inventario):
                break
            else:
                print("El producto no existe en el inventario. Por favor ingrese un producto válido o Ctrl + D para no modificar ningún producto")
    except EOFError:
        return

    try:  # Pido al usuario que ingrese la nueva cantidad del producto, siempre que sea un número positivo
        while True:
            cantidad = int(input("Ingrese la nueva cantidad del producto: ")) 
            if cantidad < 0:
                print("La cantidad debe ser un número positivo o 0. Por favor ingrese una cantidad válida o Ctrl + D para no modificar ningún producto")
            else:
                break
    except EOFError:
        return

    # Itero sobre la lista del inventario hasta dar con el producto a modificar y asigno la nueva cantidad al encontrarlo
    for producto in inventario:
        if producto["nombre"] == nombre:
            producto["cantidad"] = cantidad
            print(f"La cantidad del producto {nombre} ha sido modificada a {cantidad}.")
            return

def eliminar_producto():
    """
    Elimina un producto del inventario.
    """
    try:  # Pido al usuario que ingrese el producto a eliminar del inventario
        while True:
            nombre = input("Ingrese el nombre del producto a eliminar: ").capitalize().strip() 
            if any(producto["nombre"] == nombre for producto in inventario):
                break
            else:
                print("El producto no existe en el inventario. Por favor ingrese un producto válido o Ctrl + D para no eliminar ningún producto")
    except EOFError:
        return

    # Elimino del inventario el registro correspondiente al producto en cuestión
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print(f"El producto {nombre} ha sido eliminado del inventario.")

def main():
    """
    Función principal del programa.
    """
    while True:
        clear_output()
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            modificar_cantidad()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Gracias por usar el programa. ¡Hasta luego!")            
            break 
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")
        input("Presione Enter para continuar...")

if __name__ == "__main__":
  main()
