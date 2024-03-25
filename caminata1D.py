import matplotlib.pyplot as plt
import uniforme
import time

# Función para simular el movimiento de la rana
def simular_movimiento(num_saltos, lista_aleatoria):
    posicion = 0
    frecuencias = {}

    for i in range(num_saltos):
        # Obtener el siguiente número aleatorio de la lista
        paso = 1 if lista_aleatoria[i] > 0.5 else -1
        posicion += paso
        # Actualizar el diccionario de frecuencias
        if posicion in frecuencias:
            frecuencias[posicion] += 1
        else:
            frecuencias[posicion] = 1

    return frecuencias

# Parámetros de la simulación
num_saltos = 1000000

# Medir el tiempo de ejecución
start_time = time.time()

# Generar una lista de un millón de números aleatorios entre 0 y 1
lista_aleatoria = uniforme.generarDistrUniforme(1,0,315366927,num_saltos)

# Simular el movimiento de la rana
frecuencias = simular_movimiento(num_saltos, lista_aleatoria)

# Calcular el tiempo transcurrido
elapsed_time = time.time() - start_time
print("Tiempo de ejecución:", elapsed_time, "segundos")

# Obtener posiciones y frecuencias para graficar
posiciones = list(frecuencias.keys())
frecuencias_valores = list(frecuencias.values())

# Graficar las frecuencias de salida
plt.bar(posiciones, frecuencias_valores, color='skyblue')
plt.title('Frecuencia de posiciones después de {} saltos'.format(num_saltos))
plt.xlabel('Posición')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()