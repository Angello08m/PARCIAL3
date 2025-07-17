# PARCIAL3
Este repositorio contiene una implementación en Python de un sistema de gestión de biblioteca usando programación funcional.

## Cómo ejecutar el código

La forma más rápida de probar el código es en [Google Colab](https://colab.research.google.com):

1. Abre Google Colab en tu navegador.  
2. Crea un nuevo cuaderno (Notebook).  
3. En la primera celda, copia y pega todo el contenido de `biblioteca.py`.  
4. Ejecuta la celda (haz clic en el botón ▶️ o presiona **Shift + Enter**).  
5. Añade una nueva celda debajo y escribe, por ejemplo:
   ```python
   # Ejemplo de uso
   from biblioteca import Biblioteca, Libro, Usuario

   # Crear biblioteca, libros y usuario
   biblioteca = Biblioteca()
   libro1 = Libro("El Quijote", "Miguel de Cervantes", "12345")
   biblioteca.agregar_libro(libro1)
   user = Usuario("Ana Pérez", "U001")
   biblioteca.agregar_usuario(user)

   # Préstamo y devolución
   print(user.tomar_prestado(libro1))
   print(user.devolver_libro(libro1))
