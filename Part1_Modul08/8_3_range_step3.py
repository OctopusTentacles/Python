# Задача 3. Диета

# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать. 
# Питается Саша следующим образом: 
# каждые 3 часа он выпивает литр воды и съедает N калорий. 
# Пить и есть он, кстати, начинает сразу как только проснётся. 
# Напишите программу, которая считает сколько он выпьет литров воды и 
# сколько калорий он съест перед тем как пойдёт спать.

wakeUp = int(input("Во сколько проснулся? "))
water = 0
calories = 0
for i in range(wakeUp, 23, 3):
    print("Сейчас", i, "часов")
    cal = int(input("Сколько съел? "))
    calories += cal
    water += 1
print("Выпито воды", water, "литров")
print("Съедено калорий", calories)