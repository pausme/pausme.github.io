def new_add(n1, n2):
    try:
        result = n1 + n2
    except:
        print("请输入数来进行相加!")
    else:
        print(result)

new_add("1",2)


while True:
    num1 = eval(input())
    num2 = eval(input())
    if num1 == "0":
        break
    new_add(num1,num2)


def storage_name(filename):
    try:
        with open(filename,encoding="utf-8") as rstream:
            contents = rstream.read()
    except:
        print(f"Sorry, the file {filename} does not exist")
    else:
        print(contents)

storage_name("dog.txt")

# 10-10
# 将except中内容改成pass即可