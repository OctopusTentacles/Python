# запрашивает у пользователя два числа и выводит их сумму на экран.
# Используйте функцию int() для преобразования входящих данных из текста в число.
# Для этого внутри скобок функции int вставьте команду input.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print('Сумма =', a + b)


# Продолжая программу прошлой задачи, добавьте ввод третьего и четвёртого числа, вычислите значение выражения и выведите результат на экран.
# 2(c+5+ab/4b)(d-2(a**3/30))-10
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
s = 2*(c + 5 + (a*b)/(4*b))*(d - 2*a**3/30) - 10
print(s)


# Дана программа:
# a = '2'
# b = '5'
# c = '3'
# num = 6 ** a + (7 - b) * c
# print(num)
# исправьте в ней четвёртую строку, используя только функцию int().
# Запустите и проверьте работу программы. Результат должен быть равен 42.
a = '2'
b = '5'
c = '3'
num = 6 ** int(a) + (7 - int(b)) * int(c)
print(num)