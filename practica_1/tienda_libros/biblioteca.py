class Libro:
    def __init__(self, numero_libro, genero, autor, titulo, año_publicacion, tarifa_diaria_alquiler):
        self.numero_libro = numero_libro
        self.genero = genero
        self.autor = autor
        self.titulo = titulo
        self. año_publicacion=año_publicacion
        self.tarifa_diaria_alquiler = tarifa_diaria_alquiler
        self.disponible = True 

    def __str__(self):
      return f"Número: {self.numero_libro}, Género: {self.genero}, Autor: {self.autor}, Título: {self.titulo}, Año de publicación: {self.año_publicacion}, Tarifa diaria: {self.tarifa_diaria_alquiler}, Disponible: {'Sí' if self.disponible else 'No'}"

class Nodo:
    def __init__(self, libro=None):
        self.libro = libro
        self.siguiente = None
        self.anterior = None

class DoubleLinkedList:
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.longitud = 0

    def __iter__(self):
        nodo_actual=self.cabeza
        while nodo_actual is not None:
            yield nodo_actual
            nodo_actual=nodo_actual.siguiente

    
    def __str__(self):
        resultado = [str(x.libro) for x in self]
        return '  '.join(resultado)
    

    def agregar_libro_al_final_de_la_lista(self, libro):
        nuevo_nodo =Nodo(libro)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.longitud +=1

    def agregar_libro_al_principio_de_la_lista(self, libro):
        nuevo_nodo = Nodo(libro)
        if self.cabeza== None :
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            return nuevo_nodo
        else:
            self.cabeza.anterior =nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.longitud +=1


    def eliminar_libro(self, numero_libro):
        if self.longitud == 0:
            return print("No hay libros en la lista para eliminar ")
        
        # Buscar el nodo con el número de libro especificado
        nodo_actual = self.cabeza
        for nodo_actual in self:
            if nodo_actual.libro.numero_libro == numero_libro:
                if nodo_actual == self.cabeza:
                    self.cabeza = nodo_actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                # Si es el último nodo de la lista
                if nodo_actual == self.cola:
                    self.cola = nodo_actual.anterior
                    if self.cola:
                        self.cola.siguiente = None
                # Si está en medio de la lista
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                self.longitud -= 1
                return print(f"El libro con número {numero_libro} ha sido eliminado.")
            nodo_actual = nodo_actual.siguiente

        print(f"No se encontró ningún libro con el número {numero_libro} en la lista.")


    def buscar_libro_por_genero(self, genero):
        lista_libros = DoubleLinkedList()
        cantidad_libros = 0
        for nodo_actual in self:
            if nodo_actual.libro.genero == genero:
                cantidad_libros += 1
                libro = nodo_actual.libro
                informacion_del_libro = f"Número: {libro.numero_libro}, Género: {libro.genero}, Autor: {libro.autor}, Título: {libro.titulo}, Año de publicación: {libro.año_publicacion}, Tarifa diaria: {libro.tarifa_diaria_alquiler}, Disponible: {'Sí' if libro.disponible else 'No'}"
                lista_libros.agregar_libro_al_final_de_la_lista(informacion_del_libro)

        return lista_libros, cantidad_libros
    
    def buscar_libro_por_titulo(self, titulo):
        for nodo_actual in self:
            if nodo_actual.libro.titulo == titulo:
                disponible = "Sí" if nodo_actual.libro.disponible else "No"
                return f"El libro {titulo} está en la biblioteca y {'está disponible' if nodo_actual.libro.disponible else 'no está disponible'} para alquiler."
        return f"El libro {titulo} no se encuentra en la biblioteca."
    
    def buscar_libro_por_autor(self, autor):
        for nodo_actual in self:
            if nodo_actual.libro.autor == autor:
                disponible = "Sí" if nodo_actual.libro.disponible else "No"
                return f"El libro de {autor}, con el titulo {nodo_actual.libro.titulo}, ,está en la biblioteca y {'está disponible' if nodo_actual.libro.disponible else 'no está disponible'} para alquiler."
        return f"El libro de {autor} no se encuentra en la biblioteca."
    
    def buscar_libro_por_año_de_publicacion(self, año_publicacion):
        for nodo_actual in self:
            if nodo_actual.libro.año_publicacion == año_publicacion:
                disponible = "Sí" if nodo_actual.libro.disponible else "No"
                return f"El libro de {año_publicacion}, con el titulo {nodo_actual.libro.titulo}, ,está en la biblioteca y {'está disponible' if nodo_actual.libro.disponible else 'no está disponible'} para alquiler."
        return f"El libro de {año_publicacion} no se encuentra en la biblioteca."

    def lista_libros_disponibles(self):
        libros_disponibles = DoubleLinkedList()
        for nodo_actual in self:
            if nodo_actual.libro.disponible:
                libros_disponibles.agregar_libro_al_final_de_la_lista(nodo_actual.libro)

        print("Libros disponibles para alquilar:")
        for nodo_libro in libros_disponibles:
            print(nodo_libro.libro)

    def lista_libros_no_disponibles(self):
        libros_no_disponibles = DoubleLinkedList()
        for nodo_actual in self:
            if not nodo_actual.libro.disponible:
                libros_no_disponibles.agregar_libro_al_final_de_la_lista(nodo_actual.libro)        

        if libros_no_disponibles.longitud == 0:
            print("Todos los libros están disponibles para alquilar.")
        else:
            print("Libros no disponibles para alquilar:")
            for nodo_libro in libros_no_disponibles:
                print(nodo_libro.libro)

    def lista_libros_disponibles_por_genero(self, genero):
        libros_disponibles = DoubleLinkedList()
        for nodo_actual in self:
            if nodo_actual.libro.genero == genero:
                if nodo_actual.libro.disponible:
                    libros_disponibles.agregar_libro_al_final_de_la_lista(nodo_actual.libro)

        print("Libros disponibles para alquilar por genero son:")
        for nodo_libro in libros_disponibles:
            print(nodo_libro.libro)


   

print ("Hola")
libro1 = Libro(1, "Ficción", "J.R.R. Tolkien", "El Señor de los Anillos", 1954, 2.50)
libro2 = Libro(2, "Ficción", "George Orwell", "1984", 1949, 1.75)
libro3 = Libro(3, "Ficción", "George", "1984", 1949, 1.75)
lista =DoubleLinkedList()
lista.agregar_libro_al_final_de_la_lista(libro1)
lista.agregar_libro_al_principio_de_la_lista(libro2)
lista.agregar_libro_al_principio_de_la_lista(libro3)
print (lista)

libros_encontrados, cantidad = lista.buscar_libro_por_genero("Ficción")
print(f"Se encontraron {cantidad} libros de Ficción:")
print(libros_encontrados)
print(lista.buscar_libro_por_titulo("El Señor de los Anillos"))

print(lista.buscar_libro_por_titulo("El Señor de los Anillos"))
print(lista.buscar_libro_por_autor("vale"))
print(lista.buscar_libro_por_año_de_publicacion(1954))
lista.lista_libros_disponibles()
lista.lista_libros_no_disponibles()
print("La nueva lista es:, ", lista)
lista.lista_libros_disponibles_por_genero("Ficción")