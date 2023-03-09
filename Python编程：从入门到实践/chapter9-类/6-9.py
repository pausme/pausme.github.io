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

class IceCreamStand(Restaurant):
    flavors = []
    def __init__(self, restaurant, cuisine_type, flavor, number_served=0):
        super().__init__(restaurant,cuisine_type,number_served)
        self.flavors = flavor

    def show_IceCream_info(self):
        print(self.flavors)

icecream = IceCreamStand("仝安冰激淋小店","冰激凌小店",["香蕉味","苹果味","橘子味"])
icecream.show_IceCream_info()


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

class Admin(User):
    def __init__(self, first_name, last_name, age, height, privileges, login_attempts=0):
        super(Admin, self).__init__( first_name, last_name, age, height,login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

admin = Admin("jack", "tom", 24, 186,["can add post", "can delete post", "can ban user"])
admin.show_privileges()


class Privileges:

    def __init__(self,privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)
# 将Admin中 self.privileges = privileges 改成 self.privileges = Privileges()即可 (需将Privileges类移至Admin类前)


