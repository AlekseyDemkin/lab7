import numpy as np
import pandas as pd
import numpy
import matplotlib.pyplot as plt

Dt = pd.read_csv("data2.csv")
N = numpy.array(Dt["Solids"])
data = N[~np.isnan(N)]
data = data.astype("float")
fig = plt.figure(figsize=(7, 4))

plt.title("Гистограмма", fontweight="bold", fontsize=14, pad=10)
plt.xlabel("Solids", fontweight="bold", labelpad=5)
plt.ylabel("Frequency", fontweight="bold", labelpad=5)
plt.hist(data, 45, edgecolor="w", color="navy")
plt.grid()

plt.show()

ig = plt.figure(figsize=(7, 4))

plt.title("Нормализированная гистограмма", fontweight="bold", fontsize=14, pad=10)
plt.xlabel("Solids", fontweight="bold", labelpad=5)
plt.ylabel("Frequency", fontweight="bold", labelpad=5)
plt.hist(data, 45, edgecolor="w", color="firebrick", density=True)
plt.grid()

plt.show()
print("Среднеквадратичное отклонение:", np.std(data))
