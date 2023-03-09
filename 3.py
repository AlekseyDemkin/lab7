# Демкин Алексей 368096 поток 1.4
import numpy as np
import matplotlib.pyplot as plt

x = np.setdiff1d(np.linspace(-np.pi, 0, 75), [0])  # генерируем наборы координат,
# из-за ОДЗ (1/х) график пришлось разбить на два
y = np.array(1 / x)
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, c='navy')          # настраиваем сам график

x = np.setdiff1d(np.linspace(0, np.pi, 75), [0])
y = np.array(1 / x)
z = np.sin(x)
ax.plot(x, y, z, c="navy")      # настраиваем сам график

plt.title("График функций")
ax.set_xlabel("x")              # подписываем оси
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
