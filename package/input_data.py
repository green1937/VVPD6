"""
Модуль для введения данных, на основе которых находится кол-во ходов для одного,
либо двух коней.

Исползуется для подсчета минимального кол-ва ходов в случае, если по шахматной доске ходит один конь,
либо же в случае, если по шахматной передвигаются два коня.

Функция get_data() - ввод данных
"""


def get_data():
    """
    Функция ввода данных для первой и второй функций.

    :return: 4 кортежа с целыми числами по 2 числа в каждом (координаты точек)
    """
    flag = 0
    while flag != 4:
        flag = 0
        XY = input("Введите координаты двух точек: ")
        XY = list(XY.split())
        if len(XY) == 4:
            for i in range(0, 4):
                if XY[i].isdigit():
                    XY[i] = int(XY[i])
                    if 9 > XY[i] > 0:
                        flag += 1
                    else:
                        break
                else:
                    break
        if flag != 4:
            print("Неверно! Введите вновь.")
    start, finish = [],[]
    start.extend([XY[0], XY[1]])
    finish.extend([XY[2], XY[3]])
    start = tuple(start); finish = tuple(finish)
    first = start; second = finish
    return start, finish, first, second
