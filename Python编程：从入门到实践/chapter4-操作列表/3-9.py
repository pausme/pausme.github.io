for i in range(1,21):
    print(i)
#for a in range(1,1_000_001):
#    print(a)
list1 = [value for value in range(1,1_000_001)]
print(min(list1))
print(max(list1))
x = sum(list1)
print(x)

list2 = [ b for b in range(1,21,2)]
for x in list2:
    print(x)
list3 = [c for c in range(3,31,3)]
for x in list3:
    print(x)
list4 = [d**3 for d in range(1,11)]
for x in list4:
    print(x)
