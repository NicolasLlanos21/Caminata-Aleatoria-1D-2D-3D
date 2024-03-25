import matplotlib.pyplot as plt
import numpy as np
import time
import uniforme

# Función para simular el movimiento de la rana en un plano cartesiano hasta una posición objetivo
def simular_movimiento_hasta_posicion(posicion_objetivo, lista_aleatoria):
    posicion = [0, 0]  # Inicializar la posición de la rana en (0,0)
    posiciones = []

    while tuple(posicion) != posicion_objetivo:
        # Obtener el siguiente número aleatorio de la lista
        direccion_x = "derecha" if lista_aleatoria[len(posiciones)] > 0.5 else "izquierda"
        direccion_y = "arriba" if uniforme.generarDistrUniforme(1,0,None,1)[0] > 0.5 else "abajo"
        #Movimiento en 2 ejes a la vez
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
        
        """
         # Movimiento en un eje a la vez
        if lista_aleatoria[len(posiciones)] < 0.25:       #iz
            posicion[0] -= 1
        elif lista_aleatoria[len(posiciones)] < 0.5:      #der
            posicion[0] += 1
        elif lista_aleatoria[len(posiciones)] < 0.75:     #Abajo
             posicion[1] -= 1
        elif lista_aleatoria[len(posiciones)] > 1:        #Arriba
            posicion[1] += 1
        """    
        # Guardar la posición actual
        posiciones.append(tuple(posicion))

    return posiciones

# Parámetros de la simulación
posicion_objetivo = (250, 300)

# Medir el tiempo de ejecución
start_time = time.time()

# Generar una lista de números aleatorios suficientemente larga
lista_aleatoria =  uniforme.generarDistrUniforme(1,0,3859806572,10000000) # Genera 10 millones de números aleatorios

# Simular el movimiento de la rana hasta la posición objetivo
posiciones = simular_movimiento_hasta_posicion(posicion_objetivo, lista_aleatoria)

# Calcular el tiempo transcurrido
elapsed_time = time.time() - start_time
print("La rana llegó a la posición objetivo en", len(posiciones), "saltos.")
print("Tiempo de ejecución:", elapsed_time, "segundos")

# Crear un array 2D para el mapa de calor
heatmap, xedges, yedges = np.histogram2d([pos[0] for pos in posiciones], [pos[1] for pos in posiciones], bins=(50, 50))

# Rotar heatmap
heatmap = np.rot90(heatmap)
heatmap = np.flipud(heatmap)

# Graficar el mapa de calor
plt.imshow(heatmap, extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='plasma')
plt.colorbar(label='Frecuencia')
plt.title('Mapa de calor de frecuencia de posiciones de la rana hasta la posición objetivo')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.show()
