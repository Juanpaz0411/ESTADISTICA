import numpy as np
import matplotlib.pyplot as plt

def camino_aleatorio(N):
    x = np.arange(0, N + 1)
    y = np.zeros(N + 1, dtype=int)
    pasos_y = np.random.choice([-1, 1], size=N)  # Pasos completamente aleatorios
    for i in range(1, N + 1):
        y[i] = y[i-1] + pasos_y[i-1]
    return x, y

def graficar_caminos(N, num_trayectorias=10):
    caminos = [camino_aleatorio(N) for _ in range(num_trayectorias)]
    
    # Evento A: Trayectorias que terminan en (2N, 0)
    evento_A = sum(1 for _, y in caminos if y[-1] == 0)
    
    # Evento B: Trayectorias que nunca bajan del eje positivo
    caminos_positivos = [(x, y) for x, y in caminos if np.all(y >= 0)]
    evento_B = len(caminos_positivos)
    
    # Probabilidades
    Pr_A = evento_A / num_trayectorias
    Pr_B = evento_B / num_trayectorias
    Pr_A_y_B = Pr_A * Pr_B
    
    print(f"Número de trayectorias que terminan en (2N, 0) (Evento A): {evento_A}")
    print(f"Número de trayectorias que permanecen en el eje positivo (Evento B): {evento_B}")
    print(f"Pr(A) = {Pr_A:.4f}")
    print(f"Pr(B) = {Pr_B:.4f}")
    print(f"Pr(A y B) = {Pr_A_y_B:.4f}")
    
    # Gráfico con todas las trayectorias
    plt.figure(figsize=(8, 6))
    for x, y in caminos:
        plt.plot(x, y, alpha=0.6)
    plt.xlabel("2N")
    plt.ylabel("X")
    plt.title("Todas las Trayectorias")
    plt.grid(True)
    plt.show()
    
    # Gráfico con solo trayectorias que permanecen en el eje positivo
    if evento_B > 0:
        plt.figure(figsize=(8, 6))
        for x, y in caminos_positivos:
            plt.plot(x, y, alpha=0.6)
        plt.xlabel("2N")
        plt.ylabel("X")
        plt.title("Trayectorias que se Mantienen en el Eje Positivo")
        plt.grid(True)
        plt.show()
    else:
        print("No hay trayectorias que se mantengan en el eje positivo.")

# Parámetro N
graficar_caminos(N=10000, num_trayectorias=1000)


