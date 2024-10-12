"""
Generators

EX3: Implementeaza un generator de numere pare care ne va da acces la toate
numerele pare pana la un numar maxim luat ca si parametru.
"""


def numere_pare_generator(maxim):
    # Începem de la primul număr par (0)
    numar = 0
    # Continuăm să generăm numere până la valoarea maximă
    while numar <= maxim:
        yield numar
        numar += 2


# Testăm generatorul pentru a genera numere pare până la 10
maxim = 10
for numar in numere_pare_generator(maxim):
    print(numar)
