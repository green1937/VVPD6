"""
Модуль для нахождения минимального кол-ва ходов для двух коней.

Используется подсчета минимального кол-ва ходов в случае, если по шахматной доске ходит один конь,
на основании данных, полученних в модуле input_data (координаты двух точек)

Ф-я knights_collision() - нахождение кол-ва ходов
"""


def knights_collision(first: tuple[int, int], second: tuple[int, int]) -> int:
    """
    Эта функция считает, через какое минимальное количество ходов могут
    встретиться два коня, расположенных на двух разных клетках доски.

    :param first: кортеж (два целых числа - координата первого коня)
    :param second: кортеж (два целых числа - координата второго коня)
    :return: целое число (кол-во ходов, которое должны проделать оба коня)

    >>> knights_collision((1,2), (3,4))
    Нельзя посчитать.
    >>> knights_collision((1,1), (1,1))
    0
    >>> knights_collision((1,1), (6,4))
    2
    """
    step = [[100 for _ in range(0, 13)] for _ in range(0, 13)]
    step[first[0]+1][first[1]+1] = 0
    for _ in range(0, 9):
        for i in range(2, 10):
            for j in range(2, 10):
                if step[i][j] > 0:
                    step[i][j] = min(step[i+2][j+1], step[i-2][j-1],
                                    step[i-1][j-2], step[i+1][j+2],
                                    step[i+2][j-1], step[i-2][j+1],
                                    step[i+1][j-2], step[i-1][j+2])+1
    answer = step[second[0]+1][second[1]+1]
    sum1 = first[0]+first[1]
    sum2 = second[0] + second[1]
    if (sum1 % 2 == 0 and sum2 % 2 == 0) or (sum1 % 2 == 1 and sum2 % 2 == 1):
        return answer // 2
    else:
        answer = 0
        return answer
