list1 = ["Hello","Welcome","Congratulations"]

def show_message(list1):
    for i in list1:
        print(i)

show_message(list1)


sent_message = []

def send_message(list1,sent_message):
    while list1:
        temp = list1.pop()
        sent_message.append(temp)

send_message(list1,sent_message)
print(sent_message)
print(list1)


# 8-11 传参时改成list1[:]
send_message(list1[:],sent_message)
print(sent_message)
print(list1)