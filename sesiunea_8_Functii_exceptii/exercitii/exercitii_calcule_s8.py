import math

"""
Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

"""
1. Funcție care să calculeze și să returneze suma a două numere.

Cod și explicație:
Parametri: Funcția primește două numere.
Suma: Se calculează suma celor două numere.
Return: Funcția returnează suma calculată.
"""


def suma_doua_numere(numar1, numar2):
    return numar1 + numar2


# Testare funcție
print(f"Suma lui 3 și 5 este: {suma_doua_numere(3, 5)}")
print(f"Suma lui 10 și 20 este: {suma_doua_numere(10, 20)}")

"""
2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar.
Cod și explicație:
Parametru: Funcția primește un număr.
Par sau impar: Se verifică dacă numărul este divizibil cu 2.
Return: Returnează True dacă este par și False dacă este impar.
"""


def este_par(numar):
    return numar % 2 == 0


# Testare funcție
print(f"Numărul 4 este par: {este_par(4)}")
print(f"Numărul 7 este par: {este_par(7)}")

"""
3. Funcție care returnează numărul total de caractere din numele tău complet (nume, prenume, nume_mijlociu).

Cod și explicație:
Parametri: Funcția primește numele complet ca trei parametri: nume, prenume, nume mijlociu.
Calcul lungime: Se calculează lungimea totală a tuturor caracterelor din numele complet.
Return: Returnează suma lungimilor.
"""


def numar_caractere_nume(nume, prenume, nume_mijlociu=""):
    return len(nume) + len(prenume) + len(nume_mijlociu)


# Testare funcție
print(f"Numărul total de caractere din 'Popescu Ion' este: "
      f"{numar_caractere_nume('Popescu', 'Ion')}")
print(f"Numărul total de caractere din 'Popescu Ioan Alexandru' este: "
      f"{numar_caractere_nume('Popescu', 'Ioan', 'Alexandru')}")

"""
4. Scrieţi o funcţie care returnează prima cifră a unui număr natural. De exemplu, dacă parametrul efectiv este 127, 
funcţia va returna 1.

Cod și explicație:
Parametru: Funcția primește un număr natural.
Prima cifră: Folosim o metodă pentru a determina prima cifră (prin împărțiri repetate la 10).
Return: Returnează prima cifră.
"""


def prima_cifra(numar):
    while numar >= 10:
        numar //= 10
    return numar


# Testare funcție
print(f"Prima cifră a numărului 127 este: {prima_cifra(127)}")
print(f"Prima cifră a numărului 54321 este: {prima_cifra(54321)}")

"""
5. Să se tipărească toate numerele prime aflate între doi întregi citiţi. 
Programul va folosi o funcţie care testează dacă un număr este prim sau nu.

Cod și explicație:
Parametri: Funcția primește doi întregi care definesc intervalul.
Funcția de verificare: O funcție verifică dacă un număr este prim.
Afișare: Afișăm toate numerele prime din acel interval.
"""
# import math


def este_prim(numar):
    if numar <= 1:
        return False
    for i in range(2, int(math.sqrt(numar)) + 1):
        if numar % i == 0:
            return False
    return True


def numere_prime_in_interval(start, end):
    prime = []
    for i in range(start, end + 1):
        if este_prim(i):
            prime.append(i)
    return prime


# Testare funcție
print(f"Numerele prime între 10 și 30 sunt: {numere_prime_in_interval(10, 30)}")
print(f"Numerele prime între 50 și 70 sunt: {numere_prime_in_interval(50, 70)}")

"""
6. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, numere care se divid cu 
suma cifrelor lor. Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.

Cod și explicație:
Parametri: Funcția primește doi întregi pentru a defini intervalul.
Suma cifrelor: Funcția care calculează suma cifrelor unui număr.
Verificare: Se verifică dacă numărul se divide exact cu suma cifrelor sale.
Afișare: Afișăm toate numerele care îndeplinesc condiția.
"""


def suma_cifrelor(numar):
    suma = 0
    while numar > 0:
        suma += numar % 10
        numar //= 10
    return suma


def numere_divizibile_cu_suma_cifrelor(start, end):
    rezultat = []
    for i in range(start, end + 1):
        suma = suma_cifrelor(i)
        if suma != 0 and i % suma == 0:
            rezultat.append(i)
    return rezultat


# Testare funcție
print(f"Numerele între 10 și 50 care se divid cu suma cifrelor lor sunt: "
      f"{numere_divizibile_cu_suma_cifrelor(10, 50)}")
print(f"Numerele între 100 și 150 care se divid cu suma cifrelor lor sunt: "
      f"{numere_divizibile_cu_suma_cifrelor(100, 150)}")
