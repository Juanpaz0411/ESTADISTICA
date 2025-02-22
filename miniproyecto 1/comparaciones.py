import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom

def probabilidad_simulada(n, muestras):
    """Simula caminos aleatorios y evalúa la fracción que cumple las condiciones."""
    pasos = np.random.choice([-1, 1], size=(muestras, 2 * n))
    condiciones = (np.sum(pasos, axis=1) == 0) & (np.min(np.cumsum(pasos, axis=1), axis=1) >= 0)
    return np.mean(condiciones)

def probabilidad_teorica(n):
    """Calcula la probabilidad teórica basada en combinatoria."""
    return binom(2 * n, n) / ((2 ** (2 * n)) * (n + 1))

def comparar_probabilidades(n_max, muestras_lista):
    """Grafica la relación entre probabilidades simuladas y teóricas para distintos tamaños de muestra."""
    plt.figure(figsize=(12, 6))

    for muestras in muestras_lista:
        razones = [probabilidad_simulada(n, muestras) / probabilidad_teorica(n) for n in range(1, n_max + 1)]
        plt.plot(range(1, n_max + 1), razones, label=f'Muestras={muestras}')

    plt.xlabel('Numero de pasos')
    plt.ylabel('Relación Simulada/Teórica')
    plt.title('Comparación de Probabilidades')
    plt.legend()
    plt.grid()
    plt.show()

# Parámetros
n_max = 100  
muestras_lista = [50, 500, 1000, 10000, 50000]

comparar_probabilidades(n_max, muestras_lista)
