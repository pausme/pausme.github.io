def sandwich(*args):
    print("The sandwich has these foods:")
    for i in args:
        print(f" {i}")

sandwich("apple","orange","watermolen")


def build_profile(first, last, **kwargs):
    kwargs["first_name"] = "黄"
    kwargs["last_anme"] = "思豪"
    return kwargs

user_profile = build_profile("黄", "思豪", location = "九江", field = "computer science")
print(user_profile)


def make_car(manufacturer, size, *args, **kwargs):
    print(f"{manufacturer},{size},{kwargs}")

car = make_car("subaru", "outback", color = "blue", tow_package = "True")
