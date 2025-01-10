def sito_eratostenesa(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1, 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]


def wypelnij_liste(n):
    primes = sito_eratostenesa(n)
    print(f"Liczby pierwsze z przedziału od 0 do {n}: {', '.join(map(str, primes))}")

    return f"Liczby pierwsze z przedziału od 0 do {n}: {primes}"


def zapis(primes):
    with open("algorytm_eratostenesa.txt", "a", encoding="utf-8") as plik:
        plik.write(primes + "\n")


n = 100
primes = wypelnij_liste(n)
zapis(primes)
