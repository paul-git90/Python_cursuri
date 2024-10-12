"""
Exercitii din cursul Cicluri Repetitive
# WHILE/WHILE ELSE
"""

"""
#sintaxa while
while conditie_adevarata: # conditia se evalueaza ca True sau False
    # bloc de instructiuni care se executa atata timp
    # cat conditia <conditie_adevarata> ramane adevarata
    # de exemplu:
    print("Hello")
    x = 2
    y = 2 * x
    # OBLIGATORIU: cod care schimba valoarea de adevar
    # a conditiei trecute la while, astfel incat
    # sa nu se execute codul la infinit!
"""

# Exemplul 1 - Afisarea numerelor de la 0 la 3
i = 0
while i <= 3:
    print(i)
    i += 1

# Exemplul 2 - Afisarea numerelor pozitive

x = 8

while x > 0:
    print(f"Numarul {x} este pozitiv")
    x -= 1
print("S-a iesit din while")
print(f"Dupa while, x are valoarea {x}")

# Exemplul 3 - validarea credentialelor de conectare

username = input("Introduceti numele de utilizator: ")
password = input("Introduceti parola: ")

while len(username) < 6 and len(password) < 6:
    print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
    username = input("Introduceti numele de utilizator: ")
    password = input("Introduceti parola: ")
print("Autentificare reusita")

# Exemplul 4 - ghicirea unui numar introdus la tastatura
import random

secret_number = random.randint(1, 10)

guessed = False

while not guessed:
    guess_number = int(input("Alege un numar de la 1 la 10: "))
    if guess_number == secret_number:
        print("Felicitari! Ai ghicit!")
        guessed = True # conditia de iesire
    elif guess_number < secret_number:
        print("Numarul este prea mic. Incercati din nou.")
    else:
        print("Numarul este prea mare. Incercati din nou.")

# OPTIONAL: La final, se poate pune un else. Blocul de cod din else se va executa mereu 1 data, la final,
# atata timp cat ciclul repetitiv nu este intrerupt intentionat

# Exemplul 1 - Afisarea cifrelor de la 0 la 3

i = 0

while i <= 3:
    print(i)
    i += 1
else:
    print("Am terminat ciclul repetitiv while.")

# Exemplul 2 - Validarea inputului de la tastatura ca nr pozitiv

number = int(input("Introduceti un numar intreg pozitiv: "))

while number <= 0:
    print("Numarul introdus e negativ!")
    number = int(input("Introduceti un numar intreg pozitiv"))
else:
    print("Numarul introdus este pozitiv!")

# Exemplul 3 - Cautarea unui element intr-o lista
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

search_value = int(input("Ce numar cautati? "))

index = 0
while index < len(numbers):
    if numbers[index] == search_value:
        print(f"Valoarea a fost gasita la indexul: {index}")
        break
    index += 1
else:
    print("Valoarea nu a fost gasita in lista!")

"""
EX1: Se da numarul x = -5.
Foloseste un while pentru a afisa numerele negative pornind
de la -5.
La final, afiseaza un mesaj ca s-au afisat toate numerele
negative.
"""

x = -5

while x <= 0:
    print(x)
    x += 1

print("S-au afișat toate numerele negative.")

"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""

# Inițializăm variabilele

suma_notelor = 0
numar_note = 0

# Afișăm instrucțiuni pentru utilizator

print("Introduceți notele la examene. Introduceți -1 pentru a termina.")

while True:
    nota = float(input("Introdu nota: "))

    if nota == -1:
        break

    suma_notelor += nota
    numar_note += 1

# Calculăm și afișăm media aritmetică dacă există note introduse

if numar_note > 0:
    media = suma_notelor / numar_note
    print(f"Media aritmetică a notelor introduse este: {media:.2f}")
else:
    print("Nu au fost introduse note.")