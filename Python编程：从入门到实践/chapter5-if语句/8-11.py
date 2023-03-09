list1 =  ["admin","jack","mack","marry","tom"]
name = input("请输入用户名：")
list1.append(name)
if name == "admin":
    print("Hello admin, would you like to see a status report?",end="")
else:
    print(f"Hello {name}, thank you for logging in again.",end="")


list1.clear()
if not list1:
    print("We need to find some users!")


current_users = ["jack","tom","marry","mack","sary"]
new_users = ["jack","tom","lee","ray","kelly"]
current_users_replication = []

for i in current_users:
    current_users_replication.append(i.upper())

for i in new_users:
    if i.upper() in current_users_replication:
        print("需要输入别的用户名!")
        break
    else:
        print("这个用户名未被使用")


list2 = [1,2,3,4,5,6,7,8,9,]
for i in list2:
    if i == 1:
        print("1st",end="")
    elif i == 2:
        print(" 2nd",end="")
    elif i == 3:
        print(" 3rd",end="")
    else:
        print(f" {i}th",end="")
