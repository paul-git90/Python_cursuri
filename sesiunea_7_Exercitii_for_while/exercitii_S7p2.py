"""
Exercitii sesiunea 7 p2
"""
# Exercițiul 1: Afișează numerele prime dintr-un interval
"""
Scrie un program care primește două numere de la utilizator și folosește 
o buclă for pentru a afișa toate numerele prime din acel interval.

def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Introdu începutul intervalului: "))
end = int(input("Introdu sfârșitul intervalului: "))

for num in range(start, end + 1):
    if este_prim(num):
        print(num)
"""
# Exercițiul 2: Găsește cel mai mare divizor comun (GCD)
"""
Scrie un program care citește două numere de la utilizator și folosește un algoritm bazat 
pe o buclă while pentru a calcula cel mai mare divizor comun (GCD) al celor două numere.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numar1 = int(input("Introdu primul număr: "))
numar2 = int(input("Introdu al doilea număr: "))

print("GCD-ul este:", gcd(numar1, numar2))
"""
# Exercițiul 3: Numere Fibonacci până la un anumit termen
"""
Scrie un program care folosește o buclă while pentru a genera și afișa termenii din 
șirul Fibonacci până la un anumit număr dat de utilizator.

n = int(input("Introdu numărul maxim de termeni Fibonacci: "))

a, b = 0, 1
count = 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1
"""
# Exercițiul 4: Triunghi de stele inversat
"""
Scrie un program care folosește o buclă for pentru a afișa un triunghi de stele inversat, 
cu un număr de linii dat de utilizator.

n = int(input("Introdu numărul de linii: "))

for i in range(n, 0, -1):
    print('*' * i)
"""
# Exercițiul 5: Produsul elementelor de pe diagonala principală a unei matrice
"""
Scrie un program care ia o matrice pătrată de la utilizator (dimensiunea și elementele) 
și calculează produsul elementelor de pe diagonala principală folosind o buclă for.

n = int(input("Introdu dimensiunea matricei: "))

matrice = []
for i in range(n):
    while True:
        rand = list(map(int, input(f"Introdu {n} elemente pentru rândul {i+1}, separate prin spațiu: ").split()))
        if len(rand) == n:
            matrice.append(rand)
            break
        else:
            print(f"Trebuie să introduci exact {n} elemente. Încearcă din nou.")

produs_diagonala = 1
for i in range(n):
    produs_diagonala *= matrice[i][i]

print("Produsul elementelor de pe diagonala principală este:", produs_diagonala)
"""
# Exercițiul 6: Verifică dacă o listă este palindrom
"""
Scrie un program care verifică dacă o listă dată este palindrom. Folosește o buclă for 
pentru a compara elementele de la începutul și sfârșitul listei.

def este_palindrom(lista):
    for i in range(len(lista) // 2):
        if lista[i] != lista[-i - 1]:
            return False
    return True

lista = list(map(int, input("Introdu elementele listei separate prin spațiu: ").split()))

if este_palindrom(lista):
    print("Lista este un palindrom.")
else:
    print("Lista nu este un palindrom.")
"""
def este_palindrom(lista):
    # Convertim toate elementele la lowercase și ignorăm spațiile
    lista_curata = ''.join(lista).replace(" ", "").lower()
    return lista_curata == lista_curata[::-1]


while True:
    # Cerem introducerea unui cuvânt sau frază
    cuvant = input("Introdu un cuvânt sau o frază: ")

    # Verificăm dacă este palindrom
    if este_palindrom(cuvant):
        print("Este un palindrom.")
    else:
        print("Nu este un palindrom.")

    # Întrebăm utilizatorul dacă dorește să repete
    repeat = input("Dorești să verifici un alt cuvânt/frază? (da/nu): ").lower()

    if repeat != 'da':
        print("Programul s-a terminat.")
        break
