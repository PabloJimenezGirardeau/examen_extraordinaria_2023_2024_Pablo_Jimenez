class Coche:
    def __init__(self, nombre, velocidad_maxima, aceleracion):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.posicion = 0.0
        self.velocidad = 0.0

    def mover(self, tiempo):
        self.velocidad += self.aceleracion * tiempo
        if self.velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        self.posicion += self.velocidad * tiempo

    def __str__(self):
        return f'{self.nombre} - Posición: {self.posicion:.1f} m' if self.posicion != 0 else f'{self.nombre} - Posición: 0 m'

class Carrera:
    def __init__(self):
        self.coches = []

    def agregar_coche(self, coche):
        self.coches.append(coche)

    def iniciar_carrera(self, duracion, intervalo):
        tiempo_actual = 0
        while tiempo_actual <= duracion:
            print(f'Tiempo: {tiempo_actual:.1f} s')
            for coche in self.coches:
                if tiempo_actual > 0:
                    coche.mover(intervalo)
                print(coche)
            tiempo_actual += intervalo
            print('---')
        
        ganador = max(self.coches, key=lambda c: c.posicion)
        print(f'Ganador: {ganador.nombre} - Posición: {ganador.posicion:.1f} m' if ganador.posicion != 0 else f'Ganador: {ganador.nombre} - Posición: 0 m')

def solicitar_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingresa un número válido.")
