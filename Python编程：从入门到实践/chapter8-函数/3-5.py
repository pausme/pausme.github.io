def make_shirt(size, word):
    print(f"The shirt is {size} and the word is {word}.")

make_shirt("M","apple")
make_shirt(word="orange",size="S")


def make_shirt2(size = "M",word = "I love Python"):
    print(f"The shirt is {size} and the word is {word}.")

make_shirt2()
make_shirt2(size="S")
make_shirt2(word="I love C")


def describe_city(name, country = "Iceland"):
    print(f"{name} is in {country}.")

describe_city("Beijing","China")