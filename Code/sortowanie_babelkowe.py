import random

lista_nieposortowana = random.sample(range(1, 101), 100)
print(f"Lista nieposortowana: {lista_nieposortowana}")


def sortowanie_babelkowe(lista):
    n = len(lista)

    for i in range(0, n):  # od 0 do n
        for j in range(1, n - i):
            if lista[j - 1] > lista[j]:
                lista[j - 1], lista[j] = lista[j], lista[j - 1]

    return lista


def zapis(lista_posortowana):
    with open("sortowanie_babelkowe.txt", "a") as plik:
        plik.write(lista_posortowana + "\n")


lista_posortowana = sortowanie_babelkowe(lista_nieposortowana)
zapis(str(lista_posortowana))
print(" -> ".join(map(str, lista_posortowana)))
