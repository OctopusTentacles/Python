# Задача 3. Поел — можно и поспать, поспал — можно и поесть

# Напишите программу, разобранную в уроке.

# У Саши интересный режим сна: он может проснуться когда угодно, 
# хоть ночью, но засыпает всегда до того, как наступит полночь, 
# обычно в 23 часа. А ещё он очень любит поесть. 
# Он ест каждый час и если съедает больше 2000 калорий, 
# то он просто падает спать. Напишите программу, которая 
# поможет Саше понять, всё ли с ним хорошо. Для этого нужно посчитать, 
# сколько он всего съест калорий и сколько часов будет бодрым.

wakeup = int(input("Во сколько проснулся: "))
calories = 0
hour = 0
for i in range(wakeup, 23):
    print("Сейчас", i, "часов")
    eating = int(input("Сколько съел: "))
    calories += eating
    if calories > 2000:
        print("Поел — можно и поспать")
        break
    hour += 1
print("Часов не спал", hour, "съедено калорий", calories)