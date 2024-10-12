"""
Exercitii din curs: Structuri de date
  LISTA - colectie ordonata de elemente, mutabila, accepta valori duplicate, poate fi editata si accesata dupa index.
  O listă în Python este o structură de date ordonată care poate conține un număr variabil de elemente de orice tip
(inclusiv alte liste). Listele sunt foarte flexibile și permit adăugarea, eliminarea și modificarea elementelor.
Ele sunt utile în multe contexte datorită capacității lor de a gestiona colecții de date într-un mod organizat și eficient.
"""
"""
EX1: 
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""
my_list = ["filme", "seriale", "anime"]
# b. Da, lista este o structură de date ordonată. Acest lucru înseamnă că elementele din listă au o ordine specifică și
# fiecare element poate fi accesat printr-un index. Ordinea elementelor este menținută și elementele sunt accesibile în
# funcție de poziția lor în listă.
print(my_list[1])
print(len(my_list))
"""
EX2:
a. Defineste o lista numita filme_preferate, cu cel putin 3 elemente.
b. Inverseaza lista folosind slicing. (ca la string)
c. Folosind if, verifica daca lista este goala sau nu,
si afiseaza un mesaj corespunzator pentru fiecare situatie.
"""
filme_preferate = ["LOTR", "PDC", "HP"]
print(filme_preferate[::-1])
if len(filme_preferate) == 0:
    print(f'Lista {filme_preferate} este goala')
else:
    print(f'Lista {filme_preferate} nu este goala.')

if not filme_preferate:
    print("Lista este goală.")
else:
    print("Lista nu este goală.")
"""
EX3: Se da structura de date cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8].
a. Verifica tipul structurii de date dat.
b. Accesand metodele de pe lista, sorteaza lista cifre.
c. Verifica daca 9 este in lista cifre. Afiseaza un mesaj corespunzator.
"""
cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
print(type(cifre))
cifre.sort()
print(cifre)
if 9 in cifre:
    print(True)
else:
    print(False)


"""
Defineste o lista si exploreaza metodele ajutatoare ale listelor. 
"""
# Definirea listei
fructe = ["mar", "banana", "cireasa", "portocala", "kiwi"]

# Metoda append - Adaugă un element la sfârșitul listei.
fructe.append("mango")
print(fructe)  # Output: ["mar", "banana", "cireasa", "portocala", "kiwi", "mango"]

# Metoda insert - Inserează un element la o poziție specificată.
fructe.insert(2, "capsuna")
print(fructe)  # Output: ["mar", "banana", "capsuna", "cireasa", "portocala", "kiwi", "mango"]

# Metoda remove - Elimină prima apariție a unui element specificat.
fructe.remove("banana")
print(fructe)  # Output: ["mar", "capsuna", "cireasa", "portocala", "kiwi", "mango"]

# Metoda pop - Elimină elementul de la o poziție specificată (implicit, ultimul element) și îl returnează.
eliminat = fructe.pop()
print(eliminat)  # Output: "mango"
print(fructe)    # Output: ["mar", "capsuna", "cireasa", "portocala", "kiwi"]

# Metoda index - Returnează indexul primei apariții a unui element specificat.
index_portocala = fructe.index("portocala")
print(index_portocala)  # Output: 3

# Metoda count - Returnează numărul de apariții ale unui element specificat.
numar_capsuna = fructe.count("capsuna")
print(numar_capsuna)  # Output: 1

# Metoda reverse - Inversează ordinea elementelor din listă.
fructe.reverse()
print(fructe)  # Output: ["portocala", "mar", "kiwi", "cireasa", "capsuna"]

# Metoda extend - Extinde lista prin adăugarea tuturor elementelor dintr-o altă listă.
alte_fructe = ["ananas", "pepene"]
fructe.extend(alte_fructe)
print(fructe)  # Output: ["portocala", "mar", "kiwi", "cireasa", "capsuna", "ananas", "pepene"]

# Metoda clear - Elimină toate elementele din listă.
fructe.clear()
print(fructe)  # Output: []

# Metoda copy - Returnează o copie superficială a listei.
fructe_original = ["mar", "banana", "cireasa"]
fructe_copie = fructe_original.copy()
print(fructe_copie)  # Output: ["mar", "banana", "cireasa"]

# Metoda sort - Sortează lista în ordine crescătoare.
fructe.sort()
print(fructe)  # Output: ["capsuna", "cireasa", "kiwi", "mar", "portocala"]

# Metoda sort cu key - Sortează lista în funcție de un criteriu specificat.
fructe = ["mar", "banana", "cireasa"]
fructe.sort(key=len)
print(fructe)  # Output: ["mar", "banana", "cireasa"]