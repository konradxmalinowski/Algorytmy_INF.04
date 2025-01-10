import random

# algorytm eratostenesa
# ###################


# sortowanie przez wybór
# ###################


# sortowanie bąbelkowe
# ###################

# szukanie z wartownikiem
# ###################


# algorytm euklidesa
# ###################


# generowanie hasła
# ###################


def rand_pass():
    letters1 = "qwertyuiopasdfghjklzxcvbnmęóąłżźćń"
    letters = list(letters1)
    numbers1 = "1234567890"
    numbers = list(numbers1)
    symbols1 = "!#%&*()+"
    symbols = list(symbols1)

    random_chars = (
        random.sample(letters, 8)
        + random.choices(numbers, k=2)
        + random.choices(symbols, k=2)
    )

    random.shuffle(random_chars)

    return "".join(random_chars)


def save(password):
    with open("password.txt", "a", encoding="utf-8") as file:
        file.write(password + "\n")


generated_password = rand_pass()
print(f"Generated password: {generated_password}")
save(generated_password)
