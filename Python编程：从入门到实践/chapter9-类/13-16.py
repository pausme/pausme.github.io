import random


class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1,self.sides))

die1 = Die()
for i in range(10):
    die1.roll_die()
print("-----")
die2 = Die(10)
for i in range(10):
    die2.roll_die()
print("-----")
die3 = Die(20)
for i in range(10):
    die3.roll_die()


prize_number = ""
list1 = ["1",'2','3','4','5','6','7','8','9',"a","b","c","d","e"]
for i in range(4):
    temp = random.choice(list1)
    prize_number += temp
print(f"中奖号码为{prize_number}")


my_ticket = ["4762"]
count = 0
while True:
    for i in range(4):
        temp = random.choice(list1)
        prize_number += temp
    count += 1
    if prize_number in my_ticket:
        break
    prize_number = ""
print(count)
