"""
Un iterator în Python este un obiect care permite parcurgerea unui set de date (cum ar fi liste, tuple, dicționare
sau chiar string-uri) într-o manieră secvențială, element cu element. Acesta implementează două metode esențiale:
__iter__() și __next__().
"""
# Definirea unei liste (un obiect iterabil)
my_list = [1, 2, 3, 4]

# Obținem un iterator folosind iter()
my_iterator = iter(my_list)

# Parcurgem lista folosind next()
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4

# Dacă încercăm să apelăm next() din nou, va arunca StopIteration
# print(next(my_iterator))  # StopIteration
"""
Cum funcționează un iterator:
__iter__(): Returnează obiectul iterator însuși. Este apelată implicit atunci când folosim obiectul într-un context 
care cere un iterator (de exemplu, într-un for loop).
__next__(): Returnează elementul următor din secvență și mută cursorul la elementul următor. Când nu mai sunt elemente, 
aruncă excepția StopIteration.

Crearea propriului iterator:
Poți defini un iterator personalizat prin crearea unei clase care implementează metodele __iter__() și __next__().
"""


class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1


# Utilizarea iteratorului
countdown = CountDown(5)

for number in countdown:
    print(number)

# Output:
# 5
# 4
# 3
# 2
# 1

"""
Utilizări:
Iteratoarele sunt utile în parcurgerea obiectelor mari, secvențelor și în generarea valorilor dinamic, pe măsură ce 
sunt necesare (de exemplu, la citirea unui fișier linie cu linie, utilizarea generatorilor, etc.).

Un for loop în Python funcționează în spatele scenei pe baza unui iterator, de aceea nu este nevoie să apelăm explicit 
funcția next().
"""
