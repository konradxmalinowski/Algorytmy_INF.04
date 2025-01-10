liczby = input("Wprowadź dwie liczby rozdzielone spacją: ").split()
a = liczby[0]
b = liczby[1]


def euklides(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def zapis_nwd(nwd):
    with open("euklides.txt", "a", encoding="utf-8") as file:
        file.write(f"NWD liczb {a} i {b} to: {str(nwd)} \n")


if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)

    if a > 0 and b > 0:
        nwd = euklides(a, b)
        print(f"NWD liczb {a} i {b} to: {nwd}")
        zapis_nwd(nwd)
else:
    print("Obie wartości muszą być liczbami dodatnimi")
