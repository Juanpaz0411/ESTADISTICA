import numpy as np
import matplotlib.pyplot as plt

def camino_aleatorio(N):
    x = np.arange(0, 2 * N + 1)  # Rango correcto de pasos
    y = np.zeros(2 * N + 1, dtype=int)
    pasos_y = np.random.choice([-1, 1], size=2 * N)  # Pasos aleatorios
    for i in range(1, 2 * N + 1):
        y[i] = y[i - 1] + pasos_y[i - 1]
    return x, y

def graficar_caminos(N, num_trayectorias=10):
    caminos = [camino_aleatorio(N) for _ in range(num_trayectorias)]

    # Evento A: Trayectorias que terminan en (2N, 0)
    evento_A = sum(1 for _, y in caminos if y[-1] == 0)

    # Evento B: Trayectorias que nunca bajan del eje positivo
    caminos_positivos = [(x, y) for x, y in caminos if np.all(y >= 0)]
    evento_B = len(caminos_positivos)

    # Contar eventos que cumplen A y B simultáneamente
    evento_A_y_B = sum(1 for _, y in caminos_positivos if y[-1] == 0)

    # Probabilidades
    Pr_A = evento_A / num_trayectorias
    Pr_B = evento_B / num_trayectorias
    Pr_A_y_B = evento_A_y_B / num_trayectorias  # Nueva cuenta correcta

    print(f"Número de trayectorias que terminan en (2N, 0) (Evento A): {evento_A}")
    print(f"Número de trayectorias que permanecen en el eje positivo (Evento B): {evento_B}")
    print(f"Número de trayectorias que cumplen A y B simultáneamente: {evento_A_y_B}")
    print(f"Pr(A) = {Pr_A:.4f}")
    print(f"Pr(B) = {Pr_B:.4f}")
    print(f"Pr(A ∩ B) = {Pr_A_y_B:.4f}")

    # Gráfico con todas las trayectorias
    plt.figure(figsize=(8, 6))
    for x, y in caminos:
        plt.plot(x, y, alpha=0.6)
    plt.xlabel("2N")
    plt.ylabel("X")
    plt.title("Todas las Trayectorias")
    plt.grid(True)
    plt.text(N, max(max(y) for _, y in caminos) * 0.9, f"Total Caminos: {num_trayectorias}",
             bbox=dict(facecolor='white', alpha=0.5))
    plt.show()

    # Gráfico con solo trayectorias que permanecen en el eje positivo
    if evento_B > 0:
        plt.figure(figsize=(8, 6))
        for x, y in caminos_positivos:
            plt.plot(x, y, alpha=0.6)
        plt.xlabel("2N")
        plt.ylabel("X")
        plt.title("Trayectorias en el Eje Positivo")
        plt.grid(True)
        plt.text(N, max(max(y) for _, y in caminos_positivos) * 0.9, f"Total Caminos Positivos: {evento_B} \nTotal Caminos que cumplen con A y B: {evento_A_y_B}",
                 bbox=dict(facecolor='white', alpha=0.5))
        plt.show()
    else:
        print("No hay trayectorias que se mantengan en el eje positivo.")

# Parámetro N
graficar_caminos(N=1000, num_trayectorias=1000)

