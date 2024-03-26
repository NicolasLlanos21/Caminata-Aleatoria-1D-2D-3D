import matplotlib.pyplot as plt
import numpy as np
import time
import uniforme

# Función para simular el movimiento de la rana en tres dimensiones hasta una posición objetivo
def simular_movimiento_hasta_posicion_3D(posicion_objetivo, lista_aleatoria):
    posicion = [0, 0, 0]  # Inicializar la posición de la rana en (0, 0, 0)
    posiciones = []

    while tuple(posicion) != posicion_objetivo:
        # Obtener el siguiente número aleatorio de la lista
        direccion_x = "derecha" if lista_aleatoria[len(posiciones)] > 0.5 else "izquierda"
        direccion_y = "arriba" if lista_aleatoria[len(posiciones) + 1] > 0.5 else "abajo"
        direccion_z = "adelante" if lista_aleatoria[len(posiciones) + 2] > 0.5 else "atrás"
        
        # Determinar el movimiento en función de la dirección en el eje X
        if direccion_x == "izquierda":
            posicion[0] -= 1
        elif direccion_x == "derecha":
            posicion[0] += 1

        # Determinar el movimiento en función de la dirección en el eje Y
        if direccion_y == "abajo":
            posicion[1] -= 1
        elif direccion_y == "arriba":
            posicion[1] += 1
        
        # Determinar el movimiento en función de la dirección en el eje Z
        if direccion_z == "atrás":
            posicion[2] -= 1
        elif direccion_z == "adelante":
            posicion[2] += 1
        
        # Guardar la posición actual
        posiciones.append(tuple(posicion))

    return posiciones

# Parámetros de la simulación
posicion_objetivo_3D = (45, 23, 17)

# Medir el tiempo de ejecución
start_time = time.time()

# Generar una lista de números aleatorios suficientemente larga
lista_aleatoria_3D = uniforme.generarDistrUniforme(0,1,2275456998,100000000)  # Genera 100 millones de números aleatorios
print("numero generados")

# Simular el movimiento de la rana en tres dimensiones hasta la posición objetivo
posiciones_3D = simular_movimiento_hasta_posicion_3D(posicion_objetivo_3D, lista_aleatoria_3D)

# Calcular el tiempo transcurrido
elapsed_time = time.time() - start_time
print("La rana llegó a la posición objetivo en", len(posiciones_3D), "saltos.")
print("Tiempo de ejecución:", elapsed_time, "segundos")

# Convertir posiciones a arrays numpy
posiciones_3D_array = np.array(posiciones_3D)

# Crear un array 3D para el mapa de calor
histogram, edges = np.histogramdd(posiciones_3D_array, bins=(50, 50, 50))

# Graficar el mapa de calor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*posiciones_3D_array.T, c='r', marker='o')  # Mostrar puntos de las posiciones
ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')
ax.set_zlabel('Coordenada Z')
ax.set_title('Mapa de calor de posiciones de la rana hasta la posición objetivo')
plt.show()
