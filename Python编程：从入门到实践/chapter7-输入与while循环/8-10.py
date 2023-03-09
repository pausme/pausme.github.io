sandwich_orders = ["cat","dog","tiger"]
finished_sandwiches = []
# 使用for循环加上remove删除 会导致少情况
while sandwich_orders:
    i = sandwich_orders.pop()
    print(f"I made your {i} sandwich.")
    finished_sandwiches.append(i)
print(finished_sandwiches)


sandwich_orders = ["cat","pastrami","dog","pastrami","tiger","pastrami"]
print("店里的五香烟熏牛肉卖完了!")
# 使用反向遍历来防止有相邻而下标超越无法删除的情况
for i in sandwich_orders[::-1]:
    if i == "pastrami":
        sandwich_orders.remove(i)
print(sandwich_orders)

place = input("If you could visit one place in the world, where would you go?")
print(f"{place} is a picture-postcard place!")