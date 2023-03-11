# Задача 3. Квадраты нечётных чисел

# Вводится число N. Напишите программу, которая выводит квадраты 
# нечетных чисел от 1 до N. Нельзя использовать условные операторы. 
# Можно использовать цикл while, но постарайтесь всё-таки решить с 
# помощью конструкции for in range. Не нужно искать решение в интернете, 
# попробуйте подумать сами, в следующем уроке мы обязательно разберём эту задачу.

numberN = int(input("Введите число: "))
for i in range(1, numberN // 2 + numberN % 2 + 1):
    odd = i * 2 - 1
    print("Квадрат нечетного числа", odd, "равен", odd ** 2)