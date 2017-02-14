# Начнем с того, что Python позволяет производить нам простейшие математические операции
# команда print() просто выводит выражение в скобках на экран

# Сложение
print(2 + 2)
#4

# Умножение
print(2 * 3)
#6

# Деление
print(3 / 2)
#1.5

# Для целочисленного деления поставим два слэша
print(3 // 2)
#1

# Взятие цисла по модулю
print(5 % 3)
#2

# Возведение в степень
print(2 ** 5)
#32

# Точно так же мы можем работать и с дробными цислами, для этого просто используем точку
print(2.5 + 3.3)
#5.8


# Переменные
# В Python динамическая типизация переменных, то есть нам не надо прямо говорить, что в этой переменной будет цисло или строка
a = 10
# Естественно, мы можем сразу вывести эту переменную
print(a)
#10
# Теперь покажем, что такое динамическая типизация
a = 'Hello World!'
print(a)
# Hello World
# Да, в паскале такие операции были бы незаконными :) но в Python мы запросто можем присвоить переменной строку, когда до этого она содержала число
a = True
a = False
print(a)
#False
# И даже булевое значение :)


# Math
# Для того, чтобы использовать более сложные математические операции, можно подключить библиотеку math
# Для этого используем команду import
import math

# Теперь мы можем, например, извлекать квадратный корень
print(math.sqrt(3))
#1.7320508075688772

# И там даже лежат некоторые стандартные математические константы
print(math.pi)
#3.141592653589793
print(math.e)
#2.718281828459045


# Считывание значений
# Для того, чтобы позволить пользователю самому задавать значения переменных, используем команду input()
a = input()
# > 5
print(a)
#5

# Замечание: Python всё считывает как строки, чтобы работать потом с переменной как с числом, надо превести её к целочисленному значению или к дробному
a = int(a)
print(a ** 2)
#25

# К дробному
# Мы можем передовать в input() некоторую строки для создания некого подобия пользовательского интерфейса
a = float(input("Введите дробное число: "))
# Введите дробное число: 1.1
# И с print() так же
print("Ваше число в квадрате: %f" % (a ** 2))
#Ваше число в квадрате: 1.21

# Здесь для вывода дробных переменных используем %f, а для целочисленных %i
# Потом ставим % и в скобочках через запятую перечисляем все переменные, которые хотим вывести

# Думаю, что этого достаточно для первого семинара :)