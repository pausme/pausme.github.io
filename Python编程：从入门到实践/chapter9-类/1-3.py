class Restaurant:

    def __init__(self, restaurant, cuisine_type):
        self.restaurant_name = restaurant
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and {self.cuisine_type}")

    def open_restaurant(self):
        print("餐馆正在营业！")

restaurant = Restaurant("仝安餐馆","中餐厅")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 创建3个实例


class User:

    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def describe_user(self):
        print(f"Uesr name is {self.first_name} {self.last_name}.age is {self.age}.height is {self.height}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}!")

user = User("jack", "tom", 24, 186)
user.describe_user()
user.greet_user()