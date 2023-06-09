# В каждой клетке прямоугольной таблицы N×M записано некоторое число. Изначально игрок находится в левой верхней клетке.
# За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено).
# При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке
# (еду берут также за первую и последнюю клетки его пути).
# Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

n, m = map(int, input().split())
d = [list(map(int, input().split())) for row in range(n)]

w = [[0] * m for row in range(n)]
w[0][0] = d[0][0]

for x in range(1, m):
    w[0][x] = d[0][x] + w[0][x - 1]
for y in range(1, n):
    w[y][0] = d[y][0] + w[y - 1][0]
for y in range(1, n):
    for x in range(1, m):
        w[y][x] = d[y][x] + min(w[y][x - 1], w[y - 1][x])
print(w[-1][-1])