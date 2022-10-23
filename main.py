# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Quadratic
import math


def solution():
    try:
        # дозволяє перевірити блок коду на наявність помилок.
        a, b, c = map(float, input('Введите a, b, c через пробел: ').split())
    except:
        # дозволяє обробити помилку.
        print('Ошибочный формат ввода данных')
    else:
        # дозволяє виконувати код, коли немає помилок.
        d = b * b - 4 * a * c
        print("Дискримінант D = %.2f" % d)
        if d > 0:
            sd = math.sqrt(d)
            root = lambda k: '{:.2f}'.format((-b + k * sd) / (2 * a))
            solution = ' та '.join(set(map(root, (-1, 1))))
        elif d == 0:
            sd = math.sqrt(d)
            solution = (-b) / (2 * a)
        else:
            solution = 'рівняння не має рішень'
        print('Відповідь: %s' % solution)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("")
    print("Вирішуємо квадратне рівняння a*x^2 + b*x + c = 0 ")
    print("Трохи поміркуючи")
    solution()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
