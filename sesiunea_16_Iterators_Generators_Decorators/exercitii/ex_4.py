"""
Generators

EX4: Implementeaza un generator de puteri ale unui numar.
Va lua doi parametri: numarul ce va fi ridicat la putere, si
un numar care va reprezenta puterea maxima pana la care primul
parametru va fi ridicat.
"""


def puteri_generator(numar, putere_maxima):
    putere = 0
    # Generăm numărul ridicat la putere în intervalul [0, putere_maxima]
    while putere <= putere_maxima:
        yield numar ** putere
        putere += 1


# Testăm generatorul pentru numărul 2 ridicat la puteri până la 5
numar = 2
putere_maxima = 5
for rezultat in puteri_generator(numar, putere_maxima):
    print(rezultat)
