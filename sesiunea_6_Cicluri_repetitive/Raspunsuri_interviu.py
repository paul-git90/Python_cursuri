"""
RASPUNSURI INTERVIU din cursul Cicluri Repetitive
"""

# 1. Când folosim while și când folosim for?

"""
while: Folosim while atunci când nu știm dinainte câte iterații vor fi necesare. De obicei, while este utilizat pentru 
bucle care se repetă atâta timp cât o anumită condiție este adevărată. De exemplu, când așteptăm un input specific de 
la utilizator sau când iterăm până când găsim o soluție.
"""
i = 0
while i < 5:
    print(i)
    i += 1

"""
for: Folosim for atunci când știm dinainte câte iterații dorim să facem. Este utilizat pentru a itera prin elementele 
unui obiect iterabil (cum ar fi liste, tuple, stringuri, sau intervale).
"""
for i in range(5):
    print(i)

# 2. Ce este obligatoriu să avem în interiorul blocului de cod while?

"""
În interiorul blocului while, trebuie să existe o instrucțiune care să modifice condiția buclei astfel încât bucla 
să se poată opri la un moment dat. Altfel, bucla ar deveni infinită. De obicei, aceasta este o actualizare a 
variabilei de control.
"""
i = 0
while i < 5:
    print(i)
    i += 1  # Actualizarea variabilei de control

# 3. Ce reprezintă funcția range?

"""
Funcția range generează o secvență de numere. Este adesea utilizată în buclele for pentru a specifica intervalul de 
iterații. Poate lua până la trei argumente: start (început), stop (sfârșit, exclusiv) și step (pas).
"""
for i in range(1, 10, 2):  # Generază 1, 3, 5, 7, 9
    print(i)

# 4. Când alegem să folosim BREAK într-o structură repetitivă?

"""
Folosim break pentru a ieși din buclă înainte ca aceasta să-și termine toate iterațiile. De obicei, break este folosit 
atunci când o anumită condiție este îndeplinită și nu mai dorim să continuăm cu iterațiile.
"""
for i in range(10):
    if i == 5:
        break  # Ieșim din buclă când i este 5
    print(i)

# 5. Când alegem să folosim CONTINUE într-o structură repetitivă?

"""
Folosim continue pentru a sări peste restul codului din buclă pentru iterația curentă și a trece direct la următoarea 
iterație. Este util atunci când dorim să evităm anumite condiții specifice în interiorul unei bucle.
"""
for i in range(10):
    if i % 2 == 0:
        continue  # Sărim peste iterațiile pentru numere pare
    print(i)

# 6. Ce face else-ul dintr-un for/else și while/else?

"""
Blocul else atașat unui for sau while se execută doar dacă bucla se termină în mod normal (fără a se întâlni un break). 
Dacă bucla este întreruptă de un break, atunci blocul else nu se execută.
"""
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Bucla s-a terminat fără a întâlni un `break`")

# Va afișa:
# 0
# 1
# 2

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Bucla s-a terminat fără a întâlni un `break`")

# Va afișa:
# 0
# 1
# 2

# 7. Dacă avem un while/else, în ce caz nu se va executa codul din else?

"""
Codul din blocul else nu se va executa dacă bucla while este întreruptă de un break. Dacă bucla se termină în mod normal 
(adică condiția while devine falsă), atunci blocul else se va executa.
"""
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Bucla s-a terminat fără a întâlni un `break`")

# În acest caz, "else" nu se va executa pentru că bucla s-a oprit la `break`


