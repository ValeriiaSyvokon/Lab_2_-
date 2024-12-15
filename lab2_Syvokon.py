import matplotlib.pyplot as plt
import os

#шлях до файлу (замініть на свій)
data_file = "C:/Users/LERA/Desktop/DS1.txt"

#перевірка наявності файлу
if not os.path.exists(data_file):
    print(f"Файл {data_file} не знайдено у поточній папці: {os.getcwd()}")
    exit()

#зчитування даних із файлу
points = []
with open(data_file, "r") as file:
    for line in file:
        x, y = map(int, line.strip().split())
        points.append((x, y))

#розділення координат на X та Y
x_coords, y_coords = zip(*points)

#розміри полотна
canvas_width, canvas_height = 960, 540

#системи координат (0,0 в нижньому правому куті)
plt.figure(figsize=(canvas_width / 100, canvas_height / 100))
plt.scatter(x_coords, y_coords, c="blue", s=10)
plt.gca().invert_yaxis()
plt.xlim(0, canvas_width)
plt.ylim(0, canvas_height)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Точки з датасету")

#збереження у графічний файл
output_file = os.path.join(os.path.expanduser("~"), "Desktop", "output_plot.png")
if not os.access(os.path.dirname(output_file), os.W_OK):
    output_file = "output_plot.png"

plt.savefig(output_file, dpi=100)
print(f"Графік збережено у файл: {output_file}")
