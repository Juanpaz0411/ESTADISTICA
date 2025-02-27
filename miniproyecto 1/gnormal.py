import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # Importamos la distribución normal

def camino_aleatorio(N):
    x = np.arange(0, 2*N + 1)  # Rango de pasos en el eje x
    y = np.zeros(2*N + 1, dtype=int)
    pasos_y = np.random.choice([-1, 1], size=2*N)  # Pasos aleatorios
    for i in range(1, 2*N + 1):
        y[i] = y[i - 1] + pasos_y[i - 1]
    return x, y

def graficar_caminos(N, num_trayectorias=10):
    # Generamos todas las trayectorias
    caminos = [camino_aleatorio(N) for _ in range(num_trayectorias)]

    # Contamos los eventos A, B y A∩B
    evento_A = sum(1 for _, y in caminos if y[-1] == 0)
    caminos_positivos = [(x, y) for x, y in caminos if np.all(y >= 0)]
    evento_B = len(caminos_positivos)
    evento_A_y_B = sum(1 for _, y in caminos_positivos if y[-1] == 0)

    # --- 3) Gráfico adicional: HISTOGRAMA de las posiciones finales ---
    posiciones_finales = [y[-1] for _, y in caminos]
    
    # Definimos los bordes de los bins con un ancho de 2
    min_pos = min(posiciones_finales)
    max_pos = max(posiciones_finales)
    bin_edges = np.arange(min_pos - 0.5, max_pos + 2.5, 2)  # Bordes de los bins con ancho 2
    
    plt.figure(figsize=(8, 6))
    # Histograma con frecuencia de pasos (density=False)
    plt.hist(posiciones_finales, bins=bin_edges, edgecolor='black', alpha=0.7, color='skyblue', density=False)
    plt.title("Histograma de las Posiciones Finales (Bins de ancho 2)")
    plt.xlabel("Posición Final")
    plt.ylabel("Frecuencia de caminos")

    # --- Añadimos la distribución normal teórica ESCALADA ---
    media = np.mean(posiciones_finales)  # Media de las posiciones finales
    desviacion = np.std(posiciones_finales)  # Desviación estándar de las posiciones finales
    x_vals = np.linspace(min_pos, max_pos, 1000)  # Valores de x para la curva normal
    y_vals = norm.pdf(x_vals, media, desviacion) * num_trayectorias * (bin_edges[1] - bin_edges[0])  # Escalamos la curva normal
    plt.plot(x_vals, y_vals, color='blue', linewidth=2, label='Distribución normal escalada')  # Graficamos la curva

    plt.grid(True)
    plt.legend()  # Mostramos la leyenda
    plt.show()

# Ejecución con parámetros
graficar_caminos(N=10000, num_trayectorias=10000)