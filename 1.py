# Демкин Алексей 368096 поток 1.4
import random
import numpy
import time

A1, A2, N1, N2, D1, D2 = [], [], [], [], [], []
t_start = time.perf_counter()
for i in range(1, 1000001):                         # создаем стандартные массивы
    A1.append(random.randint(1, 100))
    A2.append(random.randint(1, 100))
t_start = time.perf_counter()
for i in range(1000000):                            # перемножаем их
    D1.append(A1[i] * A2[i])
all_time = time.perf_counter() - t_start
print(all_time, "Стандартный массив")
for i in range(1, 1000001):                         # генерируем numpy-массивы
    N1.append(random.randint(1, 100))
    N2.append(random.randint(1, 100))
N1 = numpy.array(N1)
N2 = numpy.array(N2)
t_start = time.perf_counter()                       # перемножаем их
D2 = numpy.multiply(N1, N2)
all_time = time.perf_counter() - t_start
print(all_time, "Numpy")
