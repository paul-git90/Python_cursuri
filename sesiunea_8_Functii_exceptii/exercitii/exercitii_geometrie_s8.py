import math

"""
Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.

Pentru a folosi functiile matematice, puteti pune la inceputul programului:
import math

Iar mai apoi folositi functiile necesare, precum:

-	math.sqrt(x)  – calculeaza radical din x
-	math.cos(x) – calculeaza cosinusul lui x
"""

"""
 1. Scrieţi o funcţie care primeşte ca parametru lungimea laturii unui pătrat şi returnează aria sa.
"""

"""
Cod și explicație:
Parametru: Funcția primește un singur parametru, lungimea laturii pătratului.
Formula: Aria pătratului se calculează folosind formula aria = latura * latura.
Return: Funcția returnează aria calculată.
"""


def calculeaza_aria(latura):
    # Calculează aria pătratului
    aria = latura * latura
    return aria


# Testare funcție
print(f"Aria unui pătrat cu latura 4 este: {calculeaza_aria(4)}")
print(f"Aria unui pătrat cu latura 7 este: {calculeaza_aria(7)}")

"""
2. Scrieți un subprogram care primește ca parametru lungimea laturii unui pătrat și returnează 
atât lungimea diagonalei, cât și perimetrul pătratului.
"""

"""
Cod și explicație:
Parametru: Funcția primește lungimea laturii pătratului.
Diagonala: Diagonala pătratului se calculează cu formula diagonala = latura * sqrt(2).
Perimetrul: Perimetrul se calculează cu formula perimetrul = 4 * latura.
Return: Funcția returnează atât diagonala, cât și perimetrul.
"""

# import math


def calculeaza_diagonala_si_perimetrul(latura):
    # Calculează diagonala și perimetrul
    diagonala = latura * math.sqrt(2)
    perimetrul = 4 * latura
    return diagonala, perimetrul


# Testare funcție
d1, p1 = calculeaza_diagonala_si_perimetrul(5)
print(f"Pentru un pătrat cu latura 5, diagonala este {d1:.2f} și perimetrul este {p1}")

d2, p2 = calculeaza_diagonala_si_perimetrul(8)
print(f"Pentru un pătrat cu latura 8, diagonala este {d2:.2f} și perimetrul este {p2}")

"""
3. Scrieți o funcție care primește ca parametri de intrare lungimile celor două catete ale unui 
triunghi dreptunghic și returnează lungimea ipotenuzei.
"""

"""
Cod și explicație:
Parametri: Funcția primește lungimile celor două catete.
Ipotenuza: Se calculează ipotenuza folosind teorema lui Pitagora: ipotenuza = sqrt(cateta1^2 + cateta2^2).
Return: Returnează ipotenuza.
"""


def calculeaza_ipotenuza(cateta1, cateta2):
    # Calculează lungimea ipotenuzei folosind teorema lui Pitagora
    ipotenuza = math.sqrt(cateta1**2 + cateta2**2)
    return ipotenuza


# Testare funcție
i1 = calculeaza_ipotenuza(3, 4)
print(f"Ipotenuza unui triunghi cu catetele 3 și 4 este: {i1:.2f}")

i2 = calculeaza_ipotenuza(6, 8)
print(f"Ipotenuza unui triunghi cu catetele 6 și 8 este: {i2:.2f}")

"""
4. Scrieți o funcție care primește 3 parametri de tip real, cu semnificația de lungimi pentru 3 segmente. 
Funcția va returna 1 dacă cele trei segmente pot forma un triunghi și 0, în caz contrar.
"""

"""
Cod și explicație:
Parametri: Funcția primește trei segmente ca parametri.
Verificare triunghi: Condiția pentru formarea unui triunghi este ca suma a două oricare dintre laturi 
să fie mai mare decât a treia latură.
Dacă a + b > c, a + c > b și b + c > a, atunci segmentele formează un triunghi.
Return: Returnează 1 dacă este posibil să formeze un triunghi, altfel returnează 0.
"""


def verifica_triunghi(a, b, c):
    # Verifică dacă segmentele pot forma un triunghi
    if a + b > c and a + c > b and b + c > a:
        return 1
    else:
        return 0


# Testare funcție
rezultat1 = verifica_triunghi(3, 4, 5)
print(f"Segmentele 3, 4 și 5 pot forma un triunghi: {rezultat1}")

rezultat2 = verifica_triunghi(1, 2, 3)
print(f"Segmentele 1, 2 și 3 pot forma un triunghi: {rezultat2}")
