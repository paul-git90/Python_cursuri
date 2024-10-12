"""
Generators

EX2: Creeaza un generator care face acelasi lucru ca si clasa MyRange
implementata la exercitiul anterior.
"""
from ex_1 import Range


def my_range(start, stop):
    valoare_curenta = start
    while valoare_curenta < stop:
        yield valoare_curenta
        valoare_curenta += 1


print("folosim clasa Range din iteratori")

for numar in Range(1, 5):
    print(numar)

print("folosim functia generator my_range")

for number in my_range(1, 5):
    print(number)
