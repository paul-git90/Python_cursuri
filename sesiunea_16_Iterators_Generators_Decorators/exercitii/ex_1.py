"""
Iterators

EX1: Implementeaza o clasa care sa fie atat iterabila cat si un iterator
si sa aiba acelasi comportament ca si functia range din Python.
"""


class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        valoarea_curenta = self.start
        self.start += 1
        return valoarea_curenta


for numar in range(1, 5):
    print(numar)

for number in Range(1, 5):
    print(number)
