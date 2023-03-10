# Пользователь покупает курс стоимостью 75 000 рублей. 
# Если денег на счету достаточно, то нужно:

# Списать со счёта деньги.
# Проверить баланс счёта. Если там меньше 5000 рублей, то зачислить на счёт 1000 рублей и вывести сообщение: «Сделана скидка».
# Вывести сообщение: «Курс успешно приобретён».
# А иначе вывести: «Не хватает денег на счету». Также в конце вывести остаток счёта и сообщение: «Хорошего дня!»

# Пример:
# Сколько денег на счету? 78500
# Курс успешно приобретён
# Сделана скидка
# Остаток на счету: 4500
# Хорошего дня!
print("Курс стоит 75000")
wallet = int(input("Сколько у вас денег на счету? "))
if wallet >= 75000:
    wallet -= 75000
    print("Курс успешно приобретён")
    if wallet < 5000:
        wallet += 1000
        print("Сделана скидка")
else:
    print("Не хватает денег на счету")
print("Остаток на счету:", wallet)
print("Хорошего дня!")