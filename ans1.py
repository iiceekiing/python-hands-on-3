meals = ["Gwote", "Masa", "Tuwon Acha", "Fura da Nono", "Kunu", "Miyan Kuka"]
print(meals)

meals.insert(-2, "Miyan Taushe")
print(meals)

meals.remove("Masa")

print(meals)

last = meals.pop(2)

print(meals)

meals.append(last)

print(meals)



middle = len(meals) // 2

print("Middle item is: ", meals[middle])

meals.sort()

print(meals)
