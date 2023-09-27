import random
import time
import threading

# Función para la Búsqueda Secuencial
def busqueda_secuencial(arreglo, elemento):
    inicio = time.time()
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:
            fin = time.time()
            return fin - inicio
    fin = time.time()
    return fin - inicio

# Función para la Búsqueda Binaria (el arreglo debe estar ordenado)
def busqueda_binaria(arreglo, elemento):
    inicio = time.time()
    inicio_binaria = 0
    fin_binaria = len(arreglo) - 1
    while inicio_binaria <= fin_binaria:
        medio = (inicio_binaria + fin_binaria) // 2
        if arreglo[medio] == elemento:
            fin = time.time()
            return fin - inicio
        elif arreglo[medio] < elemento:
            inicio_binaria = medio + 1
        else:
            fin_binaria = medio - 1
    fin = time.time()
    return fin - inicio

# Función para el Algoritmo de Ordenamiento de la Burbuja
def burbuja(arreglo):
    inicio = time.time()
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    fin = time.time()
    return fin - inicio

# Función para Quick Sort
def quick_sort(arreglo):
    inicio = time.time()
    
    def particion(arreglo, bajo, alto):
        pivote = arreglo[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            if arreglo[j] < pivote:
                i += 1
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        arreglo[i + 1], arreglo[alto] = arreglo[alto], arreglo[i + 1]
        return i + 1
    
    def quick_sort_recursivo(arreglo, bajo, alto):
        if bajo < alto:
            pivote = particion(arreglo, bajo, alto)
            quick_sort_recursivo(arreglo, bajo, pivote - 1)
            quick_sort_recursivo(arreglo, pivote + 1, alto)
    
    quick_sort_recursivo(arreglo, 0, len(arreglo) - 1)
    
    fin = time.time()
    return fin - inicio

# Función para el Método de Inserción
def insercion(arreglo):
    inicio = time.time()
    for i in range(1, len(arreglo)):
        valor_actual = arreglo[i]
        j = i - 1
        while j >= 0 and valor_actual < arreglo[j]:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = valor_actual
    fin = time.time()
    return fin - inicio

# Generar un arreglo aleatorio
arreglo = [random.randint(1, 1000) for _ in range(10000)]

# Crear hilos para ejecutar los algoritmos de manera simultánea
threads = []

# Búsqueda Secuencial
thread_secuencial = threading.Thread(target=lambda: print("Tiempo de Búsqueda Secuencial:", busqueda_secuencial(arreglo, random.randint(1, 1000))))
threads.append(thread_secuencial)

# Búsqueda Binaria (requiere un arreglo ordenado)
arreglo_ordenado = sorted(arreglo)
thread_binaria = threading.Thread(target=lambda: print("Tiempo de Búsqueda Binaria:", busqueda_binaria(arreglo_ordenado, random.randint(1, 1000))))
threads.append(thread_binaria)

# Algoritmo de Ordenamiento de la Burbuja
arreglo_burbuja = arreglo.copy()
thread_burbuja = threading.Thread(target=lambda: print("Tiempo de Burbuja:", burbuja(arreglo_burbuja)))
threads.append(thread_burbuja)

# Quick Sort
arreglo_quick = arreglo.copy()
thread_quick = threading.Thread(target=lambda: print("Tiempo de Quick Sort:", quick_sort(arreglo_quick)))
threads.append(thread_quick)

# Método de Inserción
arreglo_insercion = arreglo.copy()
thread_insercion = threading.Thread(target=lambda: print("Tiempo de Inserción:", insercion(arreglo_insercion)))
threads.append(thread_insercion)

# Iniciar los hilos
for thread in threads:
    thread.start()

# Esperar a que todos los hilos finalicen
for thread in threads:
    thread.join()