# Задача 2. Расшифровка кода

# Нам нужно расшифровать определённый код в виде одного большого числа.
# Для этого нужно посчитать сумму цифр справа налево.
# Если мы встречаем в числе цифру 5, то выводим сообщение «Обнаружен разрыв»
# и заканчиваем считать сумму. В конце программы на экран выводится
# сумма тех цифр, которые мы взяли.

number = int(input("Введите целое число: "))
summ_numbers = 0
while number != 0:
    last_number = number % 10
    if last_number == 5:
        print("Обнаружен разрыв")
        break
    print(last_number)
    summ_numbers += last_number
    number //= 10
print(summ_numbers)
