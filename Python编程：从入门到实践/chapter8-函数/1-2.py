def display_message():
    print("没有人会永远爱你，但永远会有人爱你！")

display_message()


def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("西游记")

# 测试默认值 默认参数后面不能跟着非默认参数
def describe_pet(pet_name, animal_type = "dog"):
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet("丁力")