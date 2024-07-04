from carrera_coches import Coche, Carrera, solicitar_float

def main():
    carrera = Carrera()

    while True:
        nombre = input("Ingrese el nombre del coche (o 'fin' para comenzar la carrera): ")
        if nombre.lower() == 'fin':
            break
        velocidad_maxima = solicitar_float("Ingrese la velocidad máxima del coche (m/s): ")
        aceleracion = solicitar_float("Ingrese la aceleración del coche (m/s²): ")

        coche = Coche(nombre, velocidad_maxima, aceleracion)
        carrera.agregar_coche(coche)

    if len(carrera.coches) == 0:
        print("No hay coches en la carrera. Fin del programa.")
        return

    duracion = solicitar_float("Ingrese la duración de la carrera (s): ")
    intervalo = solicitar_float("Ingrese el intervalo de tiempo para la simulación (s): ")

    carrera.iniciar_carrera(duracion, intervalo)

if __name__ == "__main__":
    main()
