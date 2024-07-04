def es_entero_positivo(numero):
    try:
        valor = int(numero)
        return valor > 1
    except ValueError:
        return False

def factorizar(n):
    factores = []
    # Dividir por 2 hasta que n sea impar
    while n % 2 == 0:
        factores.append(2)
        n = n // 2
    # Dividir por los números impares a partir de 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factores.append(i)
            n = n // i
    # Si n es un número primo mayor que 2
    if n > 2:
        factores.append(n)
    return factores

while True:
    # Solicitar al usuario un número entero positivo mayor que 1
    numero = input("Ingrese un número entero mayor que 1 (o 'salir' para terminar): ")
    if numero.lower() == 'salir':
        print("Saliendo del programa.")
        break
    while not es_entero_positivo(numero):
        print("Entrada no válida. Intente de nuevo.")
        numero = input("Ingrese un número entero mayor que 1 (o 'salir' para terminar): ")
        if numero.lower() == 'salir':
            print("Saliendo del programa.")
            break
    
    if numero.lower() == 'salir':
        break
    
    numero = int(numero)
    factores_primos = factorizar(numero)
    print(f"Factores primos de {numero}: {factores_primos}")
