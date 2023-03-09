dict1 = {"first_name":"jack","last_name":"tom","age":18,"city":"Beijing"}
for i in dict1.items():
    print(i,end=" ")


print("")
dict2 = {"jack":1,"tom":10,"mack":8,"mary":4,"ray":88}
for i in dict2.items():
    print(i,end=" ")


print("")
dict3 = {"print":"打印","for":"循环","key":"键","value":"值","in":"是否存在"}
for i in dict3.keys():
    print(i,end="\n")
    print("\t",dict3[i])