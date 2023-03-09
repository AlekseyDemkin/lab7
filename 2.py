# Демкин Алексей 368096 поток 1.4
import numpy as np
import pandas as pd
import numpy
import matplotlib.pyplot as plt

Dt = pd.read_csv("data2.csv")  # считываем данные
N = numpy.array(Dt["Solids"])  # оставляем нужный нам столбец
data = N[~np.isnan(N)]  # удаляем пустые элементы
data = data.astype("float")  # преобразуем в числа
fig = plt.figure(figsize=(7, 4))

plt.title("Гистограмма", fontweight="bold", fontsize=14, pad=10)  # название гистограммы
plt.xlabel("Solids", fontweight="bold", labelpad=5)         # подписываем оси
plt.ylabel("Frequency", fontweight="bold", labelpad=5)       # подписываем оси
plt.hist(data, 45, edgecolor="w", color="navy")         # настройка самой гистограммы
plt.grid()

plt.show()

ig = plt.figure(figsize=(7, 4))

plt.title("Нормализированная гистограмма", fontweight="bold", fontsize=14, pad=10)  # название гистограммы
plt.xlabel("Solids", fontweight="bold", labelpad=5)         # подписываем оси
plt.ylabel("Frequency", fontweight="bold", labelpad=5)         # подписываем оси
plt.hist(data, 45, edgecolor="w", color="firebrick", density=True) # настройка самой гистограммы
plt.grid()

plt.show()
print("Среднеквадратичное отклонение:", np.std(data))  # подсчет среднеквадратичного отклонения
