""" Надрукує 4 без переведення курсору на новий рядок (бо end='' прибирає
символ переведення рядка). Тут 2 зводиться в ступінь 3 і ділиться націло на 2.
Усі операції цілочисленні.
"""
print(2 ** +3 // 2, end='') # output: 4

"""Надрукує 4.0 4 без переведення курсору на новий рядок. Тут 8 ділиться
на 2 як дійсне число. Потім 8 ділиться на 2 цілочисленно.
"""
print(8 / 2, 8 // 2, end='') # output: 4.0 4

"""Надрукує 50. Тут перший доданок 7 зводиться в ступінь 2. Другий доданок 4
зводиться в ступінь 3 і від нього береться залишок від поділу на 3.
Усі операції цілочисленні.
"""
print(7 ** 2 + 4 ** 3 % 3) # output: 50

"""Надрукує приблизно 2.0 0.2 (може бути похибка). Тут ціла частина дійсного
числа 4.8 ділиться націло на 2. Потім обчислюється залишок від поділу 4.2 на 2.
У результаті виходять дійсні числа, т.к. перший операнд в обох операціях також
дійсне число, хоча операції цілочисленні.
"""
print(4.8 // 2, 4.2 % 2) # output: 2.0 0.2
