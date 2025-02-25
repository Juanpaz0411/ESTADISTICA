import numpy as np
import pandas as pd

def camino_aleatorio(steps):
    y = np.zeros(steps + 1, dtype=int)
    pasos_y = np.random.choice([-1, 1], size=steps)
    for i in range(1, steps + 1):
        y[i] = y[i - 1] + pasos_y[i - 1]
    return y

def calcular_probabilidades(steps, num_trayectorias=1000):
    caminos = [camino_aleatorio(steps) for _ in range(num_trayectorias)]

    evento_A = sum(1 for y in caminos if y[-1] == 0)
    evento_B = sum(1 for y in caminos if np.all(y >= 0))
    evento_A_y_B = sum(1 for y in caminos if np.all(y >= 0) and y[-1] == 0)
    
    Pr_A = evento_A / num_trayectorias
    Pr_B = evento_B / num_trayectorias
    Pr_A_y_B = evento_A_y_B / num_trayectorias

    return steps, Pr_A, Pr_B, Pr_A_y_B

# Valores de 2N directamente
steps_values = [40, 100, 200, 2000, 20000]  # Esto representa 2*N
num_trayectorias = 10000

# Crear la tabla de resultados
datos = [calcular_probabilidades(steps, num_trayectorias) for steps in steps_values]
df = pd.DataFrame(datos, columns=["2*N", "P_A", "P_B", "P_A∩B"])

# Mostrar la tabla
print(df)
