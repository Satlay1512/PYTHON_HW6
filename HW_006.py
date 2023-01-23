# **44. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
# 1) моя некрасивая версия
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# f1 = lambda x1, x2: (x1 - x2)  **  2
# f2 = lambda y1, y2: (y2 - y1)  **  2
# print((f1(x1, x2) + f2(y1, y2))  **  0.5)

# 2) ваша, более красива версия
# a = [int(input("Введите {i} координату точки а")) for i in 'xy']
# b = [int(input("Введите {i} координату точки b")) for i in 'xy']
# c = list(zip(a, b))
# print(c)
# res = sum([(element[1] - element[0])**2 for element in zip(a, b)])**0.5
# print(res)

# 45. Найти сумму чисел списка стоящих на нечетной позиции

# import random

# a = [random.randint(1, 10) for i in range(6)]
# print(a)
# # res = sum([value for indx, value in enumerate(a) if indx%2==1])
# res = list(map(lambda x: a[x] if (x)%2==1 else None, list(range(len(a)))))
# res = [i for i in res if i!=None]
# print(res)


# 46. Найти произведение пар чисел списка(парой считаем первый и последний,
# второй предпоследний и тд)

# import random
# a = [random.randint(1, 10) for i in range(int(input('Enter number')))]
# print(a)
# res = [a[indx]*a[-indx-1] for indx in range(len(a)//2+len(a)%2)]
# print(res)

# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

# n = int(input('Enter power of number (-3) '))
# res = [(-3)**i for i in range(n)]
# print(res)

# print([(-3)**i for i in range(int(input()))])