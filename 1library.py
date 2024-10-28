import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o', color='b', label="Пример данных")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.title("Пример линейной диаграммы")
plt.legend()
plt.grid(True)
plt.show()
