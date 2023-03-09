car = input("你要租赁什么样的汽车：")
print(f"Let me see if I can find you a {car}")


people_num = eval(input("有多少人用餐："))
if people_num > 8:
    print("没有空桌")
else:
    print("有空桌")


num = eval(input("输入一个数:"))
if num % 10 == 0:
    print("是10的整数倍")
else:
    print("不是10的整数倍")