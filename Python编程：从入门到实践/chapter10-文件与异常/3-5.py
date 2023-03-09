with open("guest.txt", "w") as wstream:
    guest = input("输入用户名:")
    wstream.write(guest)


with open("guest_book.txt", "w") as Wstream:
    while True:
        guest_book = input("输入用户名:")
        if guest_book.upper() == "Q":
            break
        else:
            Wstream.writelines(f"{guest_book}\n")
            print(f"Welcome {guest_book}!")


with open("result.txt", "w") as wstreaM:
    while True:
        result = input("你为什么爱编程:")
        if result.upper() == "Q":
            break
        else:
            wstreaM.writelines(f"{result}\n")
