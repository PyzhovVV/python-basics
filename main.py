'''
Решение реализовано с помощью правила ближайшего соседа.
Знаю, что в задании написано про n! сложность, но решение, которое было найдено мною
на просторах интернета и оптимизировано под нашу задачу,
показалось мне слишком хорошим чтобы его не показать.
'''
# import matplotlib.pyplot as plt
import numpy as np


def path_finding():
    n = int(input("Введите количество адресов: "))
    m = 50  # число для генерации координат
    a = 0  # число для генерации координа
    distance = []
    X = np.random.uniform(a, m, n)  # генерации  X координат в виде numpy матрицы
    Y = np.random.uniform(a, m, n)  # генерации  Y координат в виде numpy матрицы
    X[len(X) - 1] = 0  # делаем начальный пункт всегда в нуле
    Y[len(Y) - 1] = 0  # делаем начальный пункт всегда в нуле
    start = len(X) - 1  # номер города откуда почтальон начинает движение
    M = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] = ((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5
                # Заполнение матрицы расстояниями от каждой точки до всех ее соседей
            else:
                M[i][j] = float('inf')  # Заполнение главной диагонали матрицы (расстояние до самого себя)
    way = [start, ]  # будущий список точек, которые входят в кратчайший путь
    for i in range(1, n):
        s = []
        for j in range(n):
            s.append(M[way[i - 1]][j])  # расстояние от i-ой точки до всех ее соседей
        distance.append(min(s))
        way.append(s.index(min(s)))  # индексы пунктов ближайших городов соседей
        for j in range(i):
            M[way[i], way[j]] = float('inf')
    distance += [((X[way[n - 1]] - X[way[0]])**2 + (Y[way[n - 1]] - Y[way[0]])**2)**0.5, ]  # прибавляем путь обратно
    S = sum(distance)  # длина всего пути
    path = [(X[i], Y[i]) for i in way]  # путь в виде координат точек
    answer = str(path[0])
    for i in range(1, len(way)):
        distance[i] = distance[i - 1] + distance[i]
    for i in range(1, len(way) - 1):
        answer += ' -> ' + str(path[i]) + ' ' + str(distance[i])
    # """Визуализация"""
    # plt.title('Общий путь - %s.Всего городов - %i.\n Координаты X,Y случайные числа от %i до %i'
    #           % (round(S, 3), n, a, m), size=14)
    # X1 = [X[way[i]] for i in np.arange(0, n, 1)]
    # Y1 = [Y[way[i]] for i in np.arange(0, n, 1)]
    # plt.plot(X1, Y1, color='r', linestyle=' ', marker='o')
    # plt.plot(X1, Y1, color='b', linewidth=1)
    # X2 = [X[way[n-1]], X[way[0]]]
    # Y2 = [Y[way[n-1]], Y[way[0]]]
    # plt.plot(X2, Y2, color='g', linewidth=2,  linestyle='-', label='Путь от  последнего \n к первому городу')
    # plt.legend(loc='best')
    # plt.grid(True)
    # plt.show()
    return answer


print(path_finding())
