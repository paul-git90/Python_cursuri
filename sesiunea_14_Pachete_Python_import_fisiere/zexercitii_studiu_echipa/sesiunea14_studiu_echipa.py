"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 14)
"""


"""
1. Creaza un fisier text, numit "hello.txt" si adauga urmatoarele linii in el:
Python                                                                                              
Java
Javascript                                                                                              
C/C++/C#
PHP
Node.js

Citeste continutul din fisier si afiseaza-l.
"""
# Creăm fișierul "hello.txt" și adăugăm linii în el
with open("hello.txt", "w") as file:
    file.writelines([
        "Python\n",
        "Java\n",
        "Javascript\n",
        "C/C++/C#\n",
        "PHP\n",
        "Node.js\n"
    ])

# Citim conținutul din fișierul "hello.txt" și îl afișăm
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

"""
2.
Adauga urmatoarele linii in fisierul "hello.txt" generat la exercitiul 1:

Go                                                                                              
Kotlin
Swift

HINT: Foloseste o lista cu string-uri si un for loop. 

Afiseaza continutul noului fisier.
"""
# Liniile noi care trebuie adăugate în fișier
linii_noi = ["Go\n", "Kotlin\n", "Swift\n"]

# Deschidem fișierul "hello.txt" în modul "append" (adăugare)
with open("hello.txt", "a") as file:
    for linie in linii_noi:
        file.write(linie)

# Citim și afișăm conținutul noului fișier
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

"""
4. Citeste continutul din fisierul "hello.txt" si afiseaza
doar liniile impare.
"""
# Deschidem fișierul "hello.txt" în modul "read" (citire)
with open("hello.txt", "r") as file:
    # Citim toate liniile din fișier și le stocăm într-o listă
    linii = file.readlines()

# Afișăm doar liniile impare (indexurile 0, 2, 4, etc.)
for index, linie in enumerate(linii):
    # Deoarece numerotarea indexurilor începe de la 0, verificăm dacă indexul este par
    if index % 2 == 0:
        print(linie.strip())

"""
5.
Genereaza 26 de fisiere txt, numite "A.txt", "B.txt", ... , "Z.txt".
Fiecare fisier va avea urmatorul continut:

My name is letter X.
I am the 24th letter of the alphabet.

Fii atent la folosirea terminatiei potrivite pentru fiecare litera in functie
de a cata litera este in alphabet (1st, 2nd, 3rd, 4th...)
"""
# Lista cu sufixele pentru numere
sufixe = ['th', 'st', 'nd', 'rd']


# Functie care determina sufixul corect pentru un numar
def get_sufix(num):
    if 10 <= num % 100 <= 20:  # Pentru numere de la 10 la 20 folosim "th"
        return 'th'
    elif num % 10 in [1, 2, 3]:  # Pentru 1, 2, 3 se folosesc "st", "nd", "rd"
        return sufixe[num % 10]
    else:  # Pentru restul numerelor folosim "th"
        return 'th'


# Generam cele 26 de fisiere pentru literele A-Z
for i in range(26):
    # Convertim numarul literei in caracter (A este 65 in codul ASCII)
    litera = chr(65 + i)  # A = 65, B = 66, ... , Z = 90

    # Determinam sufixul pentru litera curenta (1st, 2nd, 3rd, etc.)
    sufix = get_sufix(i + 1)

    # Numele fisierului
    nume_fisier = f"{litera}.txt"

    # Continutul fisierului
    continut = f"My name is letter {litera}.\nI am the {i+1}{sufix} letter of the alphabet.\n"

    # Scriem continutul in fisier
    with open(nume_fisier, 'w') as file:
        file.write(continut)

    print(f"Fisierul {nume_fisier} a fost creat cu succes!")
