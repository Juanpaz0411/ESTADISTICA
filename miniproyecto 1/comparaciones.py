import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

def probabilidad_simulada(n, muestras):
    """Simula caminos aleatorios en paralelo y cuenta la fracción de trayectorias que cumplen A y B."""
    pasos = np.random.choice([-1, 1], size=(muestras, 2 * n))  # Generar todas las muestras a la vez
    trayectorias = np.cumsum(pasos, axis=1)  # Acumulado de cada fila (cada trayectoria)

    # Condiciones vectorizadas: terminar en 0 y nunca ser negativo
    cumple_condicion = (trayectorias[:, -1] == 0) & np.all(trayectorias >= 0, axis=1)

    return np.mean(cumple_condicion)  # Fracción de caminos que cumplen A y B

def probabilidad_teorica(n):
    """Calcula la probabilidad teórica basada en combinatoria."""
    return binom(2 * n, n) / ((2 ** (2 * n)) * (n + 1))

def comparar_probabilidades(n_max, muestras_lista):
    """Grafica la relación entre probabilidades simuladas y teóricas para distintos tamaños de muestra."""
    plt.figure(figsize=(12, 6))

    for muestras in muestras_lista:
        razones = [probabilidad_simulada(n, muestras) / probabilidad_teorica(n) for n in range(1, n_max + 1)]
        plt.plot(range(1, n_max + 1), razones, label=f'caminos={muestras}')

    plt.xlabel('Número de pasos (2N)')
    plt.ylabel('Relación Simulada/Teórica')
    plt.title('Comparación de Probabilidades')
    plt.legend()
    plt.grid()
    plt.show()

# Parámetros
n_max = 100  # Máximo número de pasos
muestras_lista = [50,500,1000,10000,50000]  # Diferentes tamaños de simulaciones

comparar_probabilidades(n_max, muestras_lista)