alien_color = "green"
if alien_color == "green":
    print("获得5分!")
print("------------------")
if alien_color == "green":
    print("射杀外星人，获得5分！")
else:
    print("获得10分!")
print("------------------")
if alien_color == "green":
    print("获得5分")
elif alien_color == "yellow":
    print("获得10分")
else:
    print("获得15分")
print("------------------")
age = 19
if age <2:
    print("婴儿")
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
else:
    print("老年人")
print("------------------")
favorite_fruits = ["apple","watermolen","banana","orange"]
check_fruit = input("输入想要检查的水果：")
if check_fruit in favorite_fruits:
    print(f"I really like {check_fruit}!")
else:
    print(f"I don't like {check_fruit}!")
