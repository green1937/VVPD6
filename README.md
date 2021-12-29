# **Пакет, решающий задачу "Про шахматного коня"**
<img height="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Chessboard480.svg/312px-Chessboard480.svg.png" width="100"/>

## **Описание задачи**
В шахматах конь является весьма уникальной фигурой, а всё из-за схемы
его хода (рисунок 10.1). За один ход конь может преодолеть маршрут
напоминающий букву «Г». Также математически доказано, что конь за
некоторое количество ходов может из любой клетки попасть в любую другую.

Функция ```knight_move``` считает количество ходов, необходимое коню, чтобы
добраться из одной клетки шахматной доски до другой.
Код функции:
```python
def knight_move(start: tuple[int, int], finish: tuple[int, int]) -> int:
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
```

### **Пример 1**
При (1, 1), (6, 1) - количество ходов равно 3, а при (2, 2), (2, 2) - количество ходов равно 1.

Функция ```knights_collision``` считает, через какое минимальное количество ходов могут
встретиться два коня, расположенных на двух разных клетках доски.
Код функции:
```python
def knights_collision(first: tuple[int, int], second: tuple[int, int]) -> int:
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
```

### **Пример 2**
При (1, 2), (3, 4) - количество ходов равно 2, а при (1, 2), (4, 4) - кони никогда не встретятся.
