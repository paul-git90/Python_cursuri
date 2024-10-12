"""
Exercitii sesiunea 2
"""
"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. 
X este un int.
"""
"""
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
"""
"""
If este o declaratie/ un statement in cod prin care ghidam programul nostru sa execute 
o bucata de cod in functie de un criteriu/o conditie.
x = 5
if x == 5:
    print("x este egal cu 5") # indentare cod
"""
"""
2. Verifică și afișează dacă x este număr natural sau nu.
"""
print(f'**Numar natural**')
def este_numar_natural(x):
    if isinstance(x, int) and x > 0:
        return True
    else:
        return False

# Exemplu de utilizare
x = 9
if este_numar_natural(x):
    print(f"{x} este un număr natural.")
else:
    print(f"{x} nu este un număr natural.")
"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
print(f'**Pozitiv, negativ, neutru**')
def verifica_numar(x):
    if x > 0:
        print(f"{x} este un număr pozitiv.")
    elif x < 0:
        print(f"{x} este un număr negativ.")
    else:
        print(f"{x} este un număr neutru (zero).")

# Exemple de utilizare
numere = [5, -3, 0, 4.5, -2.5]

for numar in numere:
    verifica_numar(numar)
"""
4. Verifică și afișează dacă x este între -2 și 13.
"""
print(f'**Interval**')
def verifica_interval(x):
    if -2 <= x <= 13:
        print(f"{x} este între -2 și 13.")
    else:
        print(f"{x} nu este între -2 și 13.")

# Exemple de utilizare
numere = [-3, -2, 0, 10, 13, 14]

for numar in numere:
    verifica_interval(numar)
"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
print(f'**Diferenta dintre numere**')
def verifica_diferenta(x, y):
    diferenta = abs(x - y)
    if diferenta < 5:
        print(f"Diferența dintre {x} și {y} este mai mică de 5.")
    else:
        print(f"Diferența dintre {x} și {y} nu este mai mică de 5.")

# Exemple de utilizare
perechi_numere = [(10, 6), (3, 8), (14, 10), (2, -1)]

for x, y in perechi_numere:
    verifica_diferenta(x, y)
"""
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
print(f'**Interval using not**')
def verifica_interval_not(x):
    if not (5 <= x <= 27):
        print(f"{x} nu este între 5 și 27.")
    else:
        print(f"{x} este între 5 și 27.")

# Exemple de utilizare
numere = [4, 5, 10, 27, 28]

for numar in numere:
    verifica_interval_not(numar)
"""
7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
"""
print(f'**Compara numere**')
def compara_numere(x, y):
    if x == y:
        print(f"{x} și {y} sunt egale.")
    elif x > y:
        print(f"{x} este mai mare decât {y}.")
    else:
        print(f"{y} este mai mare decât {x}.")

# Exemple de utilizare
perechi_numere = [(10, 10), (3, 8), (14, 10), (5, 5), (2, -1)]

for x, y in perechi_numere:
    compara_numere(x, y)
