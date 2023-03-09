from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

x = np.setdiff1d(np.linspace(-np.pi, 0, 75), [0])
y = np.array(1 / x)
z = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, c='navy')

x = np.setdiff1d(np.linspace(0, np.pi, 75), [0])
y = np.array(1 / x)
z = np.sin(x)
ax.plot(x, y, z, c="navy")
plt.title("График функций")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
