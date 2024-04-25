from  biblioteca import Libro, Nodo, DoubleLinkedList

def menu():
    print("Bienvenido a la biblioteca:")
    print("1. Agregar un libro al final de la lista")
    print("2. Agregar un libro al principio de la lista")
    print("3. Numero del libro a eliminar")
    print("4. Buscar libros por género")
    print("5. Buscar libro por título")
    print("6. Buscar libro por autor")
    print("7. Buscar libro por año de publicación")
    print("8. Mostrar lista de libros disponibles")
    print("9. Mostrar lista de libros no disponibles")
    print("10. Mostrar libros disponibles, por genero")
    print("11. Mostrar libros NO disponibles, por genero")
    print("12. Alquilar libro por género")
    print("13. Alquilar libro por número")
    print("14. Devolver libro")
    print("15. Ingrese el identificador del usuario para verificar el descuento por alquiler múltiple:")
    print("16. Calcular ingreso total")
    print("17. Intercambiar libros deteriorados")
    print("0. Salir")


lista = DoubleLinkedList()


while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero_libro = int(input("Ingrese el número del libro: "))
        genero = input("Ingrese el género del libro: ")
        autor = input("Ingrese el autor del libro: ")
        titulo = input("Ingrese el título del libro: ")
        año_publicacion = int(input("Ingrese el año de publicación del libro: "))
        tarifa_diaria_alquiler = float(input("Ingrese la tarifa diaria de alquiler del libro: "))

        libro = Libro(numero_libro, genero, autor, titulo, año_publicacion, tarifa_diaria_alquiler)
        lista.agregar_libro_al_final_de_la_lista(libro)
        

    if opcion == "2":
        numero_libro = int(input("Ingrese el número del libro: "))
        genero = input("Ingrese el género del libro: ")
        autor = input("Ingrese el autor del libro: ")
        titulo = input("Ingrese el título del libro: ")
        año_publicacion = int(input("Ingrese el año de publicación del libro: "))
        tarifa_diaria_alquiler = float(input("Ingrese la tarifa diaria de alquiler del libro: "))

        libro = Libro(numero_libro, genero, autor, titulo, año_publicacion, tarifa_diaria_alquiler)
        lista.agregar_libro_al_final_de_la_lista(libro)
        

    elif opcion == "3":
        numero_libro = int(input("Ingrese el número del libro a eliminar: "))  # Convertir a entero
        print(lista.eliminar_libro(numero_libro))


    elif opcion == "4":
        genero = input("Ingrese el género a buscar: ")
        libros_encontrados, cantidad = lista.buscar_libro_por_genero(genero)
        print(f"Se encontraron {cantidad} libros de {genero}:")
        print(libros_encontrados)

    elif opcion == "5":
        titulo = input("Ingrese el título del libro a buscar: ")
        print(lista.buscar_libro_por_titulo(titulo))

    elif opcion == "6":
        autor = input("Ingrese el nombre del autor del libro a buscar: ")
        print(lista.buscar_libro_por_autor(autor))

    elif opcion == "7":
        año = int(input("Ingrese el año de publicación del libro a buscar: "))
        print(lista.buscar_libro_por_año_de_publicacion(año))

    elif opcion == "8":
        lista.lista_libros_disponibles()

    elif opcion == "9":
        lista.lista_libros_no_disponibles()

    elif opcion == "10":
        genero = input("Ingrese el género para mostrar libros disponibles: ")
        print(lista.lista_libros_disponibles_por_genero(genero))

    elif opcion == "11":
        genero = input("Ingrese el género para mostrar libros NO disponibles: ")
        print(lista.lista_libros_no_disponibles_por_genero(genero))

    elif opcion == "12":
        genero = input("Ingrese el género del libro a alquilar: ")
        numero_libro =int( input("Ingrese el número del libro a alquilar: "))
        print(lista.alquilar_libro_por_genero(genero, numero_libro))

    elif opcion == "13":
        numero_libro = int(input("Ingrese el número del libro a alquilar: "))  
        print(lista.alquilar_libro(numero_libro))

    elif opcion == "14":
        numero_libro = int(input("Ingrese el número del libro a devolver: "))  
        print(lista.devolver_libro(numero_libro))

    elif opcion == "15":
        usuario = input("Ingrese el identificador del usuario para verificar el descuento por alquiler múltiple: ")
        print(lista.aplicar_descuento_por_alquiler_multiple(usuario))