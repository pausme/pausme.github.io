dict1 = {"print":"打印","for":"循环","key":"键","value":"值","in":"是否存在"}
for i in dict1.keys():
    print(i,end="\n")
    print("\t",dict1[i])


dict2 = {"nile":"egypt","huanghe":"china","zhangjiang":"china"}
for i in dict2.items():
    print(f"The {i[0].title()} runs through {i[1].title()}.")
for i in dict2.keys():
    print(i)
for i in dict2.values():
    print(i)


dict3 = {"jen":"python","sarah":"c","edward":"ruby","phil":"python"}
list1 = ["jack","jen","mary","phil"]
for i in list1:
    if i in dict3.keys():
        print(f"thank you!, {i}")
    else:
        print(f"welcome you to come!, {i}")
