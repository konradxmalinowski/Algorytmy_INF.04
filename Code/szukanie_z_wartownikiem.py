import random


def wypelnij_liste():
    lista = random.choices(range(1, 101), k=50)
    # [random.randint(1, 100) for _ in range(50)]
    return lista


def przeszukaj_liste(lista, szukana_wartosc):
    lista.append(szukana_wartosc)

    index = 0
    while lista[index] != szukana_wartosc:
        index += 1

    lista.pop()

    if index == len(lista):
        return -1
    else:
        return index


def zapis(wartosc):
    with open("wartownik.txt", "a", encoding="utf-8") as zapis:
        zapis.write(str(wartosc) + "\n")


def main():
    print("Skrypt przeszukiwania listy z wartownikiem.")

    lista = wypelnij_liste()

    komunikat_lista = "Lista liczb: " + ", ".join(map(str, lista))
    print(komunikat_lista)
    zapis(komunikat_lista)

    szukana_wartosc = int(input("Podaj szukana wartość: "))
    index = przeszukaj_liste(lista, szukana_wartosc)

    komunikat_wynik = "Wartość {} {}.".format(
        szukana_wartosc,
        (
            f"Wartość została znaleziona pod indexem {index}"
            if index != -1
            else "Nie występuje na liście"
        ),
    )
    zapis(komunikat_wynik)
    zapis("")

    print(komunikat_wynik)


if __name__ == "__main__":
    main()
