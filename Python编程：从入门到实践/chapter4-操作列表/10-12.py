list1 = ["1","2","3","4","5","6","7","8","9"]
print("The first three items in the list are:")
print(list1[:3])
print("Three items from the middle of the list are:")
print(list1[3:6])
print("The last three items in the list are:")
print(list1[6:9])
print("------------------------------------")
pizzas = ["1","2","3"]
for pizza in pizzas:
    print(f"I love {pizza} pizza")
print("I really love pizza!")
friend_pizzas = pizzas[:]
friend_pizzas.append("4")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
