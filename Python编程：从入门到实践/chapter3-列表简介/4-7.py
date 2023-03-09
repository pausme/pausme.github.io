names = ["jack","mark","marry"]
for name in names:
    print(f"{name},欢迎您共进晚餐")
print("jack不能到来")
names.remove("jack")
print(names)
for name in names:
    print(f"{name},欢迎您共进晚餐")
print("找到一个更大的餐桌，可以容纳更多的人")
names.insert(0,"tom")
names.insert(1,"smith")
names.append("john")
for name in names:
    print(f"{name},欢迎您共进晚餐")
print("餐桌无法按时到达，只能邀请两位嘉宾")
print(names)
while len(names)>2:
    detele_name = names.pop()
    print(f"{detele_name}，抱歉无法邀请您的到来")
for name in names:
    print(f"{name},您仍在受邀嘉宾当中，欢迎您共进晚餐")
del names
try:
    print(names)
except:
    print("名单打印有误")
