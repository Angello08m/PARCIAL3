class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Libro '{self.titulo}' prestado con éxito."
        return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"Libro '{self.titulo}' devuelto con éxito."
        return f"El libro '{self.titulo}' ya estaba disponible."

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {estado}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        resultado = libro.prestar()
        if "éxito" in resultado:
            self.libros_prestados.append(libro)
        return resultado

    def devolver_libro(self, libro):
        resultado = libro.devolver()
        if "éxito" in resultado and libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        return resultado

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado a la biblioteca."

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        return f"Usuario '{usuario.nombre}' agregado a la biblioteca."

    def mostrar_libros(self):
        return "\n".join(str(libro) for libro in self.libros)

    def mostrar_usuarios(self):
        return "\n".join(str(usuario) for usuario in self.usuarios)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de la biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "12345")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "67890")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Crear usuario
    usuario1 = Usuario("Ana Pérez", "U001")
    biblioteca.agregar_usuario(usuario1)

    # Simular préstamo y devolución
    print(biblioteca.mostrar_libros())
    print(usuario1.tomar_prestado(libro1))
    print(biblioteca.mostrar_libros())
    print(usuario1.devolver_libro(libro1))
    print(biblioteca.mostrar_libros())