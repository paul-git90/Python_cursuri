"""
Generatorii în Python sunt o modalitate eficientă de a crea iteratoare. Ei permit generarea de valori "la cerere"
(on-demand), fără a fi necesar să fie încărcate toate valorile simultan în memorie. Generatorii sunt mai eficienți din
punct de vedere al memoriei față de funcțiile care returnează liste, deoarece oferă elementele pe măsură ce sunt cerute,
în loc să le genereze pe toate dintr-o dată.
"""


def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count  # Returnăm valorile pe rând, fără a opri execuția complet
        count += 1


# Folosim generatorul
counter = count_up_to(5)

# Parcurgem generatorul
for num in counter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# În exemplul de mai sus:

# Funcția count_up_to() folosește yield pentru a returna numere de la 1 până la valoarea maximă.
# După fiecare yield, funcția își amintește valoarea variabilei count și continuă de unde a rămas
# la următoarea iterație.
"""
Cum funcționează generatorii?
Generatorii sunt creați folosind cuvântul cheie yield în loc de return într-o funcție. O funcție obișnuită folosește 
return pentru a returna o valoare și apoi își termină execuția. O funcție generator, în schimb, folosește yield pentru 
a returna o valoare, dar își „amintește” starea în care a fost lăsată și poate relua execuția de la acea stare data 
viitoare când este apelată.

Logica din spatele generatorilor:
yield și starea funcției: Atunci când o funcție generator întâlnește cuvântul yield, ea returnează o valoare 
apelantului, dar nu își termină execuția. Funcția „îngheață” (își păstrează starea) și își reia execuția de unde a 
rămas data viitoare când este apelată.

Memoria și eficiența: Generatorii nu stochează toate elementele în memorie. În schimb, ei generează elemente pe măsură 
ce este necesar, unul câte unul, folosind puțină memorie. Acest lucru este extrem de util când lucrăm cu mari secvențe 
de date.

Iterator implicit: Un generator este un iterator implicit. Asta înseamnă că implementarea unui generator implică 
automat metodele __iter__() și __next__(), făcându-l utilizabil în for loops și alte contexte de iterare.
"""
# Diferența între return și yield:
# return: Oprește complet execuția funcției și returnează o valoare.
# yield: Returnează o valoare, dar păstrează starea funcției și permite reluarea execuției ulterior.
# Un exemplu mai complex – generator de numere pare:


def even_numbers(limit):
    numar = 0
    while numar <= limit:
        if numar % 2 == 0:
            yield numar
        numar += 1


# Utilizarea generatorului
for even in even_numbers(10):
    print(even)

# Output:
# 0
# 2
# 4
# 6
# 8
# 10

# Un alt exemplu – secvența Fibonacci:
# Generatorii sunt adesea utilizați pentru secvențe de date infinite sau foarte mari, cum ar fi secvențele Fibonacci.


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Folosim generatorul Fibonacci
fib = fibonacci()

# Afișăm primele 10 numere Fibonacci
for _ in range(10):
    print(next(fib))

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

"""
Generatorii sunt funcții care folosesc yield pentru a returna secvențial valori fără a stoca toate valorile în memorie.
yield suspendă execuția funcției și reia de unde a rămas la apeluri ulterioare.
Generatorii sunt utili pentru parcurgerea secvențelor mari de date, evaluând elementele „pe măsură ce sunt necesare”.
Aceasta este logica din spatele generatorilor: eficiență, memorie redusă și ușurința cu care pot fi creați și utilizați.
"""