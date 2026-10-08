import time
import random
import matplotlib.pyplot as plt

# Algoritmo original del maestro O(n²)

def suma_objetivo_lenta(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True
    return False

#Algoritmo O(n)

def suma_objetivo_rapida(lista, objetivo):
    vistos = set()
    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            return True
        vistos.add(num)
    return False

if __name__ == "__main__":

    tamanios = [1000, 2000, 4000, 8000]

    tiempos_lenta = []
    tiempos_rapida = []

    objetivo_imposible = -1

    print(f"{'n':<10}{'Tiempo O(n²) [s]':<22}{'Tiempo O(n) [s]':<20}")
    print("-" * 52)

    for n in tamanios:

        lista = [random.randint(1, 100000) for _ in range(n)]

        inicio = time.perf_counter()
        suma_objetivo_lenta(lista, objetivo_imposible)
        fin = time.perf_counter()
        tiempo_lenta = fin - inicio
        tiempos_lenta.append(tiempo_lenta)

        inicio = time.perf_counter()
        suma_objetivo_rapida(lista, objetivo_imposible)
        fin = time.perf_counter()
        tiempo_rapida = fin - inicio
        tiempos_rapida.append(tiempo_rapida)

        print(f"{n:<10}{tiempo_lenta:<22.6f}{tiempo_rapida:<20.6f}")

    plt.figure(figsize=(9, 5))
    plt.plot(tamanios, tiempos_lenta, marker='o', color='red', label='suma_objetivo (Lenta) - O(n²)')
    plt.plot(tamanios, tiempos_rapida, marker='s', color='green', label='suma_objetivo (Rápida) - O(n)')

    plt.title('Comparación de Complejidad Algorítmica (Peor Caso)')
    plt.xlabel('Tamaño de la lista (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.legend()
    plt.show()