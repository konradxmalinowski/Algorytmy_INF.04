lista_nieposortowana = list(
    map(int, input("Wprowadź liczbę dziesięciu liczb rozdzielonych spacją: ").split())
)


def sortowanie_przez_wybor(lista):
    n = len(lista)

    for i in range(n):
        index_najmniejszego = i
        for j in range(i + 1, n):
            if lista[j] > lista[index_najmniejszego]:
                index_najmniejszego = j
        lista[i], lista[index_najmniejszego] = lista[index_najmniejszego], lista[i]
    return lista


def save_list(lista):
    with open("sortowanie_przez_wybor.txt", "a") as zapis:
        zapis.write(str(lista) + "\n")


lista_posortowana = sortowanie_przez_wybor(lista_nieposortowana)
print(f'Lista posortowana {" -> ".join(map(str, lista_posortowana))}')
