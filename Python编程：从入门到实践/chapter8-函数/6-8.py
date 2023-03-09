def city_country(name, country):
    temp = f"{name}, {country}"
    return temp.title()

print(city_country("Beijing","China"))


def make_album(singer_name,CD_name,count=None):
    return {"singer_name":singer_name,"CD_name":CD_name,"count":count}

print(make_album("ray","1"))


while True:
    singer_name = input()
    if singer_name.upper() == "Q":
        break
    CD_name = input()
    print(make_album(singer_name,CD_name))
