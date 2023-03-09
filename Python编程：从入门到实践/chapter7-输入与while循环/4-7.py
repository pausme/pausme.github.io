while True:
    ingredientes = input()
    if ingredientes == "quit":
        break
    print(f"我们会加入{ingredientes}.")


while True:
    audience_age = eval(input())
    if audience_age == 0:
        break
    if audience_age > 12:
        print("收费15美元")
    elif audience_age > 3:
        print("收费10美元")
    else:
        print("免费")


# 无限循环
# while True:
#     print("hello!")
