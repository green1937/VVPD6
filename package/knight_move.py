"""
Модуль для нахождения минимального кол-ва ходов для одного коня.

Используется подсчета минимального кол-ва ходов в случае, если по шахматной доске ходит один конь,
на основании данных, полученних в модуле input_data (координаты двух точек)

Ф-я knight_move() - нахождение кол-ва ходов
"""


def knight_move(start: tuple[int, int], finish: tuple[int, int]) -> int:
    """
    Эта функция считает количество ходов, необходимое коню, чтобы
    добраться из одной клетки шахматной доски до другой.

    :param start: кортеж (два целых числа - начальная координата коня)
    :param finish: кортеж (два целых числа - конечная координата коня)
    :return: целое число (кол-во ходов, которое необходимое сделать коню)

    >>> knight_move((1,1), (1,1))
    0
    >>> knight_move((1,2), (6,4))
    3
    """
    step = [[100 for _ in range(0,13)] for _ in range(0,13)]
    step[start[0]+1][start[1]+1] = 0
    for _ in range(0,9):
        for i in range(2, 10):
            for j in range(2, 10):
                if step[i][j] > 0:
                    step[i][j] = min(step[i+2][j+1], step[i-2][j-1],
                                    step[i-1][j-2], step[i+1][j+2],
                                    step[i+2][j-1], step[i-2][j+1],
                                    step[i+1][j-2], step[i-1][j+2])+1
    answer = step[finish[0]+1][finish[1]+1]
    return answer