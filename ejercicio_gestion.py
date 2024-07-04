class Tarea:
    def __init__(self, titulo, descripcion=""):
        # Inicializa una nueva tarea con un título y una descripción opcional
        self.titulo = titulo
        self.descripcion = descripcion

    def __str__(self):
        # Representación en string de una tarea para mostrarla fácilmente
        return f"Título: {self.titulo}, Descripción: {self.descripcion}"


class GestorDeTareas:
    def __init__(self):
        # Inicializa una lista vacía de tareas
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion=""):
        # Crea una nueva tarea y la añade a la lista de tareas
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' agregada.")
        print(f"Tareas actuales: {[t.titulo for t in self.tareas]}")  

    def eliminar_tarea(self, titulo):
        # Elimina una tarea de la lista basada en su título
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada.")
                return
        print(f"Tarea '{titulo}' no encontrada.")

    def mostrar_tareas(self):
        # Muestra todas las tareas en la lista
        print("Mostrando tareas...")  
        if not self.tareas:
            print("No hay tareas.")
        else:
            for tarea in self.tareas:
                print(tarea)


def menu():
    gestor = GestorDeTareas()
    while True:
        # Muestra el menú de opciones al usuario
        print("\n--- Menú de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Opción para agregar una tarea
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea (opcional): ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            # Opción para eliminar una tarea
            titulo = input("Título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == "3":
            # Opción para listar todas las tareas
            print("Ejecutando opción 'Listar tareas'...")  # Mensaje de depuración
            gestor.mostrar_tareas()
        elif opcion == "4":
            # Opción para salir del programa
            print("Saliendo del gestor de tareas.")
            break
        else:
            # Mensaje para opción no válida
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
