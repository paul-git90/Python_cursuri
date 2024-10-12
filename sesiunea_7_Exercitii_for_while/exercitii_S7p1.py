"""
Exercitii sesiunea 7 p1
"""
# Exercițiul 1: Afișează numerele de la 1 la 20
"""
Scrie un program care folosește o buclă for pentru a afișa numerele 
de la 1 la 20, fiecare pe o linie nouă.

for i in range(1, 21):
    print(i)
"""
# Exercițiul 2: Numărătoare inversă
"""
Scrie un program care folosește o buclă while pentru a face o numărătoare 
inversă de la 10 la 1. La final, afișează mesajul "Start!".

i = 10
while i > 0:
    print(i)
    i -= 1
print("Start!")
"""
# Exercițiul 3: Suma primelor 10 numere naturale
"""
Folosind o buclă for, calculează suma primelor 10 numere naturale 
(1, 2, 3, ..., 10) și afișează rezultatul.

suma = 0
for i in range(1, 11):
    suma += i
print("Suma primelor 10 numere este:", suma)
"""
# Exercițiul 4: Afișează elementele unei liste
"""
Dă o listă de numere, parcurge lista folosind o buclă for each 
(în Python, se folosește doar for) și afișează fiecare element.

lista = [3, 5, 7, 9, 11]
for numar in lista:
    print(numar)
"""
# Exercițiul 5: Numere pare între 1 și 20
"""
Folosind o buclă for, afișează toate numerele pare între 1 și 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
"""
# Exercițiul 6: Numără vocalele dintr-un cuvânt
"""
Scrie un program care primește un cuvânt de la utilizator și 
folosește o buclă for pentru a număra câte vocale conține acel cuvânt.

cuvant = input("Introdu un cuvânt: ")
vocale = "aeiouAEIOU"
numar_vocale = 0

for litera in cuvant:
    if litera in vocale:
        numar_vocale += 1

print("Cuvântul conține", numar_vocale, "vocale.")
"""

