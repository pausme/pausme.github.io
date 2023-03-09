class Restaurant:

    def __init__(self, restaurant, cuisine_type, number_served=0):
        self.restaurant_name = restaurant
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and {self.cuisine_type}")

    def show_number_served_info(self):
        print(f"There are {self.number_served} in the restaurant now!")

    def open_restaurant(self):
        print("餐馆正在营业！")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,number_served):
        self.number_served += number_served

restaurant = Restaurant("仝安餐馆","中餐厅",2)
restaurant.show_number_served_info()


class User:

    def __init__(self, first_name, last_name, age, height,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"Uesr name is {self.first_name} {self.last_name}.age is {self.age}.height is {self.height}")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("jack", "tom", 24, 186)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)