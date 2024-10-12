"""
Partea 2 - Operatori, condiționale

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""
"""
8. 
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""
# Citirea laturilor triunghiului de la tastatură
x = int(input("Introduceți lungimea laturii x: "))
y = int(input("Introduceți lungimea laturii y: "))
z = int(input("Introduceți lungimea laturii z: "))
# Verificarea tipului triunghiului
if x == y == z:
    print("Triunghiul este echilateral.")
elif x == y or x == z or y == z:
    print("Triunghiul este isoscel.")
else:
    print("Triunghiul este oarecare.")
"""
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
"""
# Citirea unei litere de la tastatură
litera = input("Introduceți o literă: ")
# Verificarea dacă litera este vocală
if litera.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"Litera '{litera}' este o vocală.")
else:
    print(f"Litera '{litera}' nu este o vocală.")
"""
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
"""
# Citirea notei de la tastatură
nota_romaneasca = float(input("Introduceți nota în sistemul românesc: "))
# Transformarea și afișarea notei în sistemul specificat
if nota_romaneasca > 9:
    print("A")
elif nota_romaneasca > 8:
    print("B")
elif nota_romaneasca > 7:
    print("C")
elif nota_romaneasca > 6:
    print("D")
elif nota_romaneasca > 4:
    print("E")
else:
    print("F")
"""
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
# Citirea numărului întreg de la tastatură
x = int(input("Introduceți un număr întreg: "))
# Conversia numărului la șir de caractere și verificarea lungimii
if len(str(x)) >= 4:
    print(f"{x} are cel puțin 4 cifre.")
else:
    print(f"{x} nu are cel puțin 4 cifre.")
"""
12.Verifică dacă x are exact 6 cifre.
"""
# Citirea numărului întreg de la tastatură
x = int(input("Introduceți un număr întreg: "))
# Conversia numărului la șir de caractere și verificarea lungimii
if len(str(x)) == 6:
    print(f"{x} are exact 6 cifre.")
else:
    print(f"{x} nu are exact 6 cifre.")
"""
13.Verifică dacă x este număr par sau impar (x e int).
"""
# Citirea numărului întreg de la tastatură
x = int(input("Introduceți un număr întreg: "))
# Verificarea dacă numărul este par sau impar
if x % 2 == 0:
    print(f"{x} este un număr par.")
else:
    print(f"{x} este un număr impar.")
"""
14. x, y, z (int)
Afișează care este cel mai mare dintre ele?
"""
# Citirea numerelor întregi de la tastatură
x = int(input("Introduceți primul număr întreg: "))
y = int(input("Introduceți al doilea număr întreg: "))
z = int(input("Introduceți al treilea număr întreg: "))
# Determinarea celui mai mare număr
if x >= y and x >= z:
    print(f"Cel mai mare număr este: {x}")
elif y >= x and y >= z:
    print(f"Cel mai mare număr este: {y}")
else:
    print(f"Cel mai mare număr este: {z}")
"""
15. x, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
"""
# Citirea unghiurilor triunghiului de la tastatură
x = float(input("Introduceți mărimea primului unghi: "))
y = float(input("Introduceți mărimea celui de-al doilea unghi: "))
z = float(input("Introduceți mărimea celui de-al treilea unghi: "))
# Verificarea dacă triunghiul este valid
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print("Triunghiul este valid.")
else:
    print("Triunghiul nu este valid.")
"""
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
●	Citește de la tastatură un int x
●	Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
# Citirea unui număr întreg de la tastatură
x = int(input("Introduceți un număr întreg: "))
# Șirul original
sir_original = 'Coral is either the stupidest animal or the smartest rock'
# Afișarea șirului fără ultimele x caractere
sir_modificat = sir_original[:-x]
print(f"Șirul fără ultimele {x} caractere: '{sir_modificat}'")
"""
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
"""
# Șirul original
sir_original = 'Coral is either the stupidest animal or the smartest rock'
# Crearea unui nou șir format din primele 5 caractere + ultimele 5
sir_nou = sir_original[:5] + sir_original[-5:]
# Afișarea noului șir
print("Noul șir format din primele 5 caractere + ultimele 5:", sir_nou)
"""
18. Același string. 
●	Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
●	Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
●	output: 'Coral is either the stupidest animal or the smartest' 
"""
# Șirul original
sir_original = 'Coral is either the stupidest animal or the smartest rock'
# Găsirea indexului de start al cuvântului "rock"
index_rock = sir_original.find('rock')
# Afișarea indexului de start
print("Indexul de start al cuvântului 'rock':", index_rock)
# Afișarea porțiunii de șir până la cuvântul "rock"
sir_pana_la_rock = sir_original[:index_rock]
print("Șirul până la cuvântul 'rock':", sir_pana_la_rock)
"""
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
●	Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
●	Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
●	Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
"""
import random

# Generarea unui număr aleatoriu între 1 și 6 (simulând aruncarea unui zar)
dice_roll = random.randint(1, 6)
# Citirea numărului ghicit de la utilizator
numar_ghicit = int(input("Ghicește numărul aruncat de zar (între 1 și 6): "))
# Verificarea și afișarea rezultatului
if numar_ghicit < dice_roll:
    print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
elif numar_ghicit > dice_roll:
    print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
else:
    print(f"Ai ghicit. Felicitări! Ai ales {numar_ghicit} și zarul a fost {dice_roll}.")
"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
"""
# Citirea unui string de la tastatură
sir = input("Introdu un string: ")
# Verificarea dacă primul și ultimul caracter sunt la fel, ignorând diferența de caz
assert sir[0].lower() == sir[-1].lower(), "Primul și ultimul caracter nu sunt la fel."
# Afișarea unui mesaj de confirmare în cazul în care assertul este adevărat
print("Primul și ultimul caracter sunt la fel.")
"""
21. Având stringul '0123456789'
●	Afișează doar numerele pare 
●	Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
"""
sir = '0123456789'
# Afișarea numerelor pare:
numere_pare = sir[::2]
print("Numerele pare:", numere_pare)
# Afișarea numerelor impare:
numere_impare = sir[1::2]
print("Numerele impare:", numere_impare)
"""
22. Avand stringul '5132486790'
●	Afișează doar numerele pare 
●	Afișează doar numerele impare
"""
# Pentru a afișa doar numerele pare și impare din șirul dat, putem utiliza o buclă for pentru a itera
# prin fiecare caracter din șir și apoi verifica dacă caracterul este un număr par sau impar.
sir = '5132486790'
# Afișarea numerelor pare:
numere_pare = [c for c in sir if int(c) % 2 == 0]
print("Numerele pare:", ''.join(numere_pare))
# Afișarea numerelor impare:
numere_impare = [c for c in sir if int(c) % 2 != 0]
print("Numerele impare:", ''.join(numere_impare))
