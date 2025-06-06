import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
# # x = [1, 2, 3, 4, 5, 6, 7]
# # y = [2, 4, 6, 8, 10, 12, 50]

# hrsEstudo = [1, 2, 3, 4, 5]
# notaProva = [50, 60, 70, 80, 90]

# plt.scatter(hrsEstudo, notaProva, color = 'blue')
# plt.title("Gráfico de dispersão - Possível Outlier")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# # plt.show()


# temperatura = [30, 25, 20, 15, 10]
# vendasSopa = [50, 70, 90, 110, 130]




# plt.scatter(temperatura, vendasSopa, color = 'red')
# plt.title("Gráfico de dispersão - Possível Outlier")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# # plt.show()

# hrsSono = [6, 7, 5, 6, 8]
# coposCafe = [3, 2, 4, 3, 2]

# correlacao, _ = pearsonr(hrsSono, coposCafe)
# print(correlacao)

# plt.scatter(hrsSono, coposCafe, color = 'brown')
# plt.title("Gráfico de dispersão")
# plt.xlabel("Horas de Sono")
# plt.ylabel("Copos de Café")
# plt.grid(True)
# plt.show()s

# tamanhoSapato = [38, 40, 42, 36, 44]
# notaMatematica = [70, 55, 90, 65, 75]

# plt.scatter(tamanhoSapato, notaMatematica, color = 'black')
# plt.title("Gráfico de dispersão - Possível Outlier")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# plt.show()

# estresse = [1, 2, 3, 4, 5]
# desempenho = [60, 70, 80, 75, 60]

# plt.scatter(hrsEstudo, notaProva, color = 'yellow')
# plt.title("Gráfico de dispersão - Possível Outlier")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# # plt.show()


# print(correlacao)
#SO2
# y = [66, 76, 73, 86, 178, 108, 96, 59, 22, 58, 120, 144, 100, 104, 67, 89, 192, 301, 99, 66]
# Cor
# y = [5.65, 6.95, 5.75, 4.0, 2.25, 3.2, 2.7, 6.1, 5.0, 6.0, 5.5, 3.35, 3.25, 5.1, 4.4, 3.15, 3.9, 2.4, 7.7, 2.75]
# IntensidadeCor
y = [9.35, 11.15, 9.4, 6.4, 3.6, 5.8, 5.0, 10.25, 8.2, 10.15, 8.8, 5.6, 5.55, 8.7, 7.41, 5.35, 6.35, 4.25, 12.85, 4.9]
# pH
x = [19.2, 18.3, 17.1, 15.2, 14.0, 13.8, 12.8, 17.3, 16.3, 16.0, 15.7, 15.3, 14.3, 14.0, 13.8, 12.5, 11.5, 14.2, 17.3, 15.8]
# y = [3.38, 3.75, 3.88, 3.66, 3.47, 3.75, 3.92, 3.97, 3.98, 3.75, 3.76, 3.77, 3.76, 3.76, 3.9, 3.8, 3.65, 3.6, 3.86, 3.93]


# Regressão "na mão"
media_x = np.mean(x)
media_y = np.mean(y)
m = np.sum((x - media_x) * (y - media_y)) / np.sum((x - media_x)**2)
b = media_y - m * media_x

# Valores previstos da reta
x_modelo = np.linspace(min(x)-5, max(x)+30, 100)  # estender um pouco o eixo x
y_modelo = m * x_modelo + b


# Pontos a destacar
x = np.array(x)
x1, x2 = 16.0, 21.0
y1 = m * x1 + b
y2 = m * x2 + b

# Plotando
plt.figure(figsize=(8,5))
plt.scatter(x, y, color='blue', label='Pontos observados')
plt.plot(x_modelo, y_modelo, color='red', label=f'Reta: y = {m:.2f}x + {b:.2f}')
plt.scatter(x1, y1, color='green', label=f'Interpolação: x={x1}, y={y1:.2f}', zorder=5)
plt.scatter(x2, y2, color='orange', label=f'Extrapolação: x={x2}, y={y2:.2f}', zorder=5)

# Estética
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear com Pontos de Previsão')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# n = len(x)

# sum_x = sum(x)
# sum_y = sum(y)
# sum_xy = sum(x[i] * y[i] for i in range(n))
# sum_x_squared = sum(xi ** 2 for xi in x)

# # fórmula do coeficiente angular m
# m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)

# print(f"m = {m:.4f}")


correlacao, _ = pearsonr(x, y)
print(correlacao)
# print(correlacao)
# # plt.boxplot(fc)
# # plt.title('Frequência Cardíaca - Boxplot')
# # plt.grid(True)
# # plt.show()

# # plt.boxplot(qt)
# # plt.title('Intervalo QT - Boxplot')
# # plt.grid(True)
# # plt.show()

# # plt.scatter(fc, qt, color = 'blue')
# plt.title('FC por QT')
# plt.xlabel('Frequência Cardíaca')
# plt.ylabel('Intervalo QT')
# plt.grid(True)
# # plt.show()