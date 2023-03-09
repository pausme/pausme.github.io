list1 = []
with open("learning_python.txt","r") as wstream:
    content = wstream.readlines()
    print(content)
    for i in content:
        print(i.rstrip())
        list1.append(i)
print(list1)

for i in content:
    print(i.replace("Python","C").rstrip())
