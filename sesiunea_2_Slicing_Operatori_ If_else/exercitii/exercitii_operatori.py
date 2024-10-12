"""
Exercitii operatori aritmetici, logici si de atribuire
"""
"""
EX6: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""
"""
a = 10
b = 2
c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)
g = a ** b
print(g)
h = a // b
print(h)
"""
"""
EX7: Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu
rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand
si ruleaza exemplele si verifica output-ul.
"""
# Exemplul 1:
a = True
b = False
# print(not(a))
# print(not(b))
# Exemplul 2:
a = True
b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)
# Exemplul 3:
a = False
b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)
"""
EX8: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""
num = 12
if num >= 0:
    print(f'12 este numar pozitiv')
else:
    print(f'false')
if num > 5:
    print(f'12 este mai mare decat 5')
else:
    print(f'false')
if 0 <= num <= 20:
    print(f'12 este intre 0 si 20')
else:
    print(f'false')
"""
EX9: Verifica daca varsta introdusa de utilizator este mai mare
decat 18 ani.
"""
user = int(input(f'Introduceti varsta dvs: '))
if user >= 18:
    print(f'Admis')
else:
    print(f'Respins')
"""
EX10: Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
"""
pret_user = int(input(f'Introduceti pret: '))
if pret_user <= 100:
    print(f'Pret corect')
else:
    print(f'Pret fals')
"""
EX11:
a. Citeste un numar de la tastatura.
b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
"""
number = int(input(f'Scrie un numar: '))
if number % 2 == 0:
    print(f'Numarul este par')
else:
    print(f'Numarul este impar')
"""
EX12:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
"""
speed = int(input(f'Viteza masinii este: '))
if speed <= 50:
    print(f'Viteza normala')
else:
    print(f'Viteza depasita')

