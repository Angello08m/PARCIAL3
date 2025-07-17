
# Listas para almacenar libros y usuarios
libros = []
usuarios = []

def agregar_libro(titulo, autor, isbn):
    if any(l['isbn'] == isbn for l in libros):
        return f"Error: ISBN {isbn} ya existe."
    libros.append({'titulo': titulo, 'autor': autor, 'isbn': isbn, 'disponible': True})
    return f"Libro '{titulo}' agregado con éxito."

def agregar_usuario(nombre, id_usuario):
    if any(u['id'] == id_usuario for u in usuarios):
        return f"Error: Usuario con ID {id_usuario} ya existe."
    usuarios.append({'nombre': nombre, 'id': id_usuario, 'libros_prestados': []})
    return f"Usuario '{nombre}' agregado con éxito."

def mostrar_libros():
    if not libros:
        return "No hay libros en la biblioteca."
    return "\n".join(
        f"{l['titulo']} por {l['autor']} (ISBN: {l['isbn']}) - "
        f"{'Disponible' if l['disponible'] else 'Prestado'}"
        for l in libros
    )

def mostrar_usuarios():
    if not usuarios:
        return "No hay usuarios registrados."
    return "\n".join(
        f"Usuario: {u['nombre']} (ID: {u['id']}) - Libros prestados: {len(u['libros_prestados'])}"
        for u in usuarios
    )

def prestar_libro(id_usuario, isbn):
    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)
    if not usuario:
        return f"Error: Usuario con ID {id_usuario} no encontrado."
    libro = next((l for l in libros if l['isbn'] == isbn), None)
    if not libro:
        return f"Error: Libro con ISBN {isbn} no encontrado."
    if not libro['disponible']:
        return f"El libro '{libro['titulo']}' no está disponible."
    libro['disponible'] = False
    usuario['libros_prestados'].append(isbn)
    return f"Libro '{libro['titulo']}' prestado a {usuario['nombre']} con éxito."

def devolver_libro(id_usuario, isbn):
    usuario = next((u for u in usuarios if u['id'] == id_usuario), None)
    if not usuario:
        return f"Error: Usuario con ID {id_usuario} no encontrado."
    if isbn not in usuario['libros_prestados']:
        return f"Error: El usuario no tiene prestado el libro con ISBN {isbn}."
    libro = next((l for l in libros if l['isbn'] == isbn), None)
    if not libro:
        return f"Error: Libro con ISBN {isbn} no encontrado."
    libro['disponible'] = True
    usuario['libros_prestados'].remove(isbn)
    return f"Libro '{libro['titulo']}' devuelto por {usuario['nombre']} con éxito."

# ————— Ejemplo de uso —————
print(agregar_libro("El Quijote", "Miguel de Cervantes", "12345"))
print(agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", "67890"))

print(agregar_usuario("Ana Pérez", "U001"))

print("\nLista de libros inicial:")
print(mostrar_libros())

print("\nPréstamo de libro:")
print(prestar_libro("U001", "12345"))

print("\nLista de libros tras el préstamo:")
print(mostrar_libros())

print("\nDevolución de libro:")
print(devolver_libro("U001", "12345"))

print("\nLista de libros tras la devolución:")
print(mostrar_libros())
