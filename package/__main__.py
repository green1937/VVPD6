"""
Основной модуль пакета, выступает в роли точки входа

Ф-я reenter - повторный ввод с возможностью завершения,
и вывода соответствующей информации в случае некорректного ввода
Ф-я main - командный линейный интерфейс (выбор режима запуска)
"""

import click
import pytest
import doctest
import coverage
from input_data import get_data
from knight_move import knight_move
from knights_collision import knights_collision


def reenter():
    """
    Главная функция.

    :return: результат работы программы
    """
    start, finish, first, second = get_data()
    print("Минимальное кол-во ходов для коня: ", knight_move(start, finish))
    print("Кони встретятся через: ", knights_collision(first, second))


@click.command()
@click.option(
    "--mode", "-m", help="Выберите режим работы: pytest - вывод тестов pytest; doctest - вывод тестов doctest; "
                         "start - запуск программы")
def main(mode):
    """
    Ф-я для реализации командного интерфейса
    :param mode: str, режим запуска пакета
    """
    if mode == "pytest":
        pytest.main([r"package\tests\test_code.py"])
    elif mode == "doctest":
        doctest.testmod()
    elif mode == "start":
        reenter()


if __name__ == "__main__":
    main()
