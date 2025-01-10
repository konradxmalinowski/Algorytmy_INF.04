import random


def rand_pass():
    alphabet = "qwertyuiopasdfghjklzxcvbnmęóąłżźćń"
    letters = list(alphabet)
    numbers = "1234567890"
    numbers = list(numbers)
    symbols = "!#%&()*+"
    symbols = list(symbols)

    random_elements = (
        random.sample(
            letters, k=8
        )  # losuje znaki bez powtórek, k=8 -> ilośc do wylosowania
        + random.choices(
            numbers, k=2
        )  # losuje znaki Z POWTÓRKAMI, k=8 -> ilośc do wylosowania
        + random.choices(symbols, k=2)
    )

    random.shuffle(random_elements)
    return "".join(random_elements)


def save(password):
    with open("password.txt", "a", encoding="utf-8") as file:
        file.write(password + " \n")


password = rand_pass()
print(rand_pass())
save(password)
