'''
Решение реализовано с помощью правила ближайшего соседа.
Знаю, что в задании написано про n! сложность, но решение, которое было найдено мною
на просторах интернета и оптимизировано под нашу задачу,
показалось мне слишком хорошим чтобы его не показать.
'''
# import matplotlib.pyplot as plt
import numpy as np
from itertools import accumulate


def path_finding():
    # n = int(input("Введите количество адресов: "))
    n = 5
    m = 50  # число для генерации координат
    a = 0  # число для генерации координа
    distance = []
    x = [2, 5, 6, 8, 0]
    y = [5, 2, 6, 3, 2]
    # x = np.random.uniform(a, m, n)  # генерации  X координат в виде numpy матрицы
    # y = np.random.uniform(a, m, n)  # генерации  Y координат в виде numpy матрицы
    # x[len(x) - 1] = 0  # делаем начальный пункт всегда в нуле
    # y[len(y) - 1] = 2  # делаем начальный пункт всегда в нуле
    start = len(x) - 1  # номер города откуда почтальон начинает движение
    mas = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            if i != j:
                mas[i, j] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
                # Заполнение матрицы расстояниями от каждой точки до всех ее соседей
            else:
                mas[i][j] = float('inf')  # Заполнение главной диагонали матрицы (расстояние до самого себя)
    way = [start, ]  # будущий список точек, которые входят в кратчайший путь
    for i in range(1, n):
        s = []
        for j in range(n):
            s.append(mas[way[i - 1]][j])  # расстояние от i-ой точки до всех ее соседей
        distance.append(min(s))
        way.append(s.index(min(s)))  # индексы пунктов ближайших городов соседей
        for j in range(i):
            mas[way[i], way[j]] = float('inf')
    distance += [
        ((x[way[n - 1]] - x[way[0]]) ** 2 + (y[way[n - 1]] - y[way[0]]) ** 2) ** 0.5, ]  # прибавляем путь обратно
    s = sum(distance)  # длина всего пути
    path = [(x[i], y[i]) for i in way]  # путь в виде координат точек
    answer = str(path[0])
    distance = list(accumulate(distance))
    print(way)
    print(distance)
    for i in range(1, len(way)):
        answer += ' -> ' + str(path[i]) + ' ' + str(distance[i - 1])
    # """Визуализация"""
    # plt.title('Общий путь - %s.Всего городов - %i.\n Координаты X,Y случайные числа от %i до %i'
    #           % (round(s, 3), n, a, m), size=14)
    # x1 = [x[way[i]] for i in range(n)]
    # y1 = [y[way[i]] for i in range(n)]
    # plt.plot(x1, y1, color='r', linestyle=' ', marker='o')
    # plt.plot(x1, y1, color='b', linewidth=1)
    # x2 = [x[way[n-1]], x[way[0]]]
    # y2 = [y[way[n-1]], y[way[0]]]
    # plt.plot(x2, y2, color='g', linewidth=2,  linestyle='-', label='Путь от  последнего \n к первому городу')
    # plt.legend(loc='best')
    # plt.grid(True)
    # plt.show()
    # return answer + ' -> (0.0, 2.0) ' + str(distance[-1]) + ' = ' + str(s)


print(path_finding())
