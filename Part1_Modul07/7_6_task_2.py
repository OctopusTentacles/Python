print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.

year_salary = 0
for i in range(1, 13):
    print("Зарплата за", i, "месяц -")
    salary = int(input("составила: "))
    year_salary += salary
print("Средняя зарплата за год составляет:", round(year_salary / 12, 2))
