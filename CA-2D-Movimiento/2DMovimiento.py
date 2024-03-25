import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import csv
import math

class LectorCSV:
    def __init__(self, nombre_archivo, columna):
        self.datos = []
        self.indice = 0
        
        with open(nombre_archivo, 'r') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                self.datos.append(float(fila[columna]))
    
    def leer_proximo_dato(self):
        if self.indice < len(self.datos):
            dato = self.datos[self.indice]
            self.indice += 1
            return math.ceil(dato)  # Aproximar al siguiente número entero
        else:
            return None

# Ejemplo de uso
lector = LectorCSV('CA-2D-Movimiento\distribucionUniforme.csv', 'pseudoaleatorios')


# Función para mover el punto en el plano cartesiano
def mover_punto():
    global punto_actual, camino_x, camino_y, rana_annotation, meta_reached, posiciones_rana

    # Verificar si la rana ya alcanzó la meta
    if meta_reached:
        # Generar el histograma de frecuencia de las posiciones de la rana                
        return

    # Generar una dirección aleatoria entre 1 y 4
    direccion = lector.leer_proximo_dato()

    # Obtener la próxima posición sin realizar el movimiento
    next_position = punto_actual.copy()
    if direccion == 1:
        next_position[1] += 1  # Mover hacia arriba
    elif direccion == 2:
        next_position[1] -= 1  # Mover hacia abajo
    elif direccion == 3:
        next_position[0] += 1  # Mover a la derecha
    elif direccion == 4:
        next_position[0] -= 1  # Mover a la izquierda

    # Verificar si la próxima posición está dentro de los límites del plano cartesiano
    if 0 <= next_position[0] <= 250 and 0 <= next_position[1] <= 300:
        # Actualizar la posición del punto y la rana en el gráfico
        punto_actual[0], punto_actual[1] = next_position[0], next_position[1]

        camino_x.append(punto_actual[0])  # Agregar la posición X al camino
        camino_y.append(punto_actual[1])  # Agregar la posición Y al camino

        ax.clear()
        ax.plot(punto_actual[0], punto_actual[1], marker='o', color='red', markersize=10)  # Punto rojo
        ax.plot(camino_x, camino_y, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)  # Camino en azul

        # Colocar la rana encima del punto
        rana_annotation = AnnotationBbox(OffsetImage(imagen_rana, zoom=0.05), punto_actual, frameon=False)
        ax.add_artist(rana_annotation)

        # Colocar el punto de inicio (verde)
        ax.plot(0, 0, marker='o', color='green', markersize=10, label='Inicio')

        # Colocar el punto de meta (morado)
        ax.plot(250, 300, marker='o', color='purple', markersize=10, label='Meta')

        ax.set_xlim(0, 250)
        ax.set_ylim(0, 300)
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_title('Movimiento del Punto')

        # Mostrar la cuadrícula
        ax.grid(True, linestyle='--', alpha=0.7)

        # Mostrar la leyenda
        ax.legend()

        canvas.draw()

        # Guardar la posición de la rana en la lista
        posiciones_rana.append((punto_actual[0], punto_actual[1]))

        # Verificar si la rana alcanzó la meta
        if punto_actual[0] == 10 and punto_actual[1] == 11:
            meta_reached = True
            print("llego la rana")
            generar_histograma(posiciones_rana)
        else:
            # Programar la próxima llamada a mover_punto después de 500 milisegundos (0.5 segundos)
            root.after(1, mover_punto)
    else:
        # Si la próxima posición está fuera de los límites, intentar otro movimiento
        mover_punto()

# Función para generar el histograma de frecuencia de las posiciones de la rana
def generar_histograma(posiciones_rana):
    # Extraer las coordenadas X y Y de las posiciones de la rana
    posiciones_x = [pos[0] for pos in posiciones_rana]
    posiciones_y = [pos[1] for pos in posiciones_rana]

    # Crear el histograma de frecuencia de las posiciones de la rana
    plt.figure()
    plt.hist2d(posiciones_x, posiciones_y, bins=[50, 50], cmap='plasma')
    plt.colorbar(label='Frecuencia')
    plt.xlabel('Posición en X')
    plt.ylabel('Posición en Y')
    plt.title('Histograma de Frecuencia de Posiciones de la Rana')
    plt.show()

# Configurar la ventana de tkinter
root = tk.Tk()
root.title("Movimiento del Punto")

# Configurar el gráfico matplotlib y el lienzo
figure, ax = plt.subplots(figsize=(8, 8))  # Ajustar el tamaño de la figura
canvas = FigureCanvasTkAgg(figure, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)  # Hacer que el lienzo se expanda con la ventana

# Inicializar la posición del punto en el plano cartesiano
punto_actual = [0, 0]  # Iniciar en el centro

# Inicializar el camino
camino_x, camino_y = [punto_actual[0]], [punto_actual[1]]

# Cargar la imagen de la rana
imagen_rana = plt.imread("CA-2D-Movimiento/rana.png")  # Asegúrate de tener la imagen "rana.png" en la misma carpeta que este script

# Graficar el punto inicial en el gráfico
ax.plot(punto_actual[0], punto_actual[1], marker='o', color='red', markersize=10)  # Punto rojo
ax.set_xlim(0, 250)
ax.set_ylim(0, 300)
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Movimiento del Punto')

# Mostrar la cuadrícula
ax.grid(True, linestyle='--', alpha=0.7)

# Colocar la rana encima del punto inicial
rana_annotation = AnnotationBbox(OffsetImage(imagen_rana, zoom=0.05), punto_actual, frameon=False)
ax.add_artist(rana_annotation)

# Colocar el punto de inicio (verde)
ax.plot(0, 0, marker='o', color='green', markersize=10, label='Inicio')

# Colocar el punto de meta (morado)
ax.plot(250, 350, marker='o', color='purple', markersize=10, label='Meta')

canvas.draw()

# Variable para verificar si la rana ha alcanzado la meta
meta_reached = False

# Lista para almacenar las posiciones de la rana
posiciones_rana = []

# Programar la primera llamada a mover_punto después de 500 milisegundos (0.5 segundos)
root.after(1, mover_punto)

# Configurar la función de cierre al cerrar la ventana
root.protocol("WM_DELETE_WINDOW", root.quit)

# Ejecutar la aplicación
root.mainloop()
