"""Exercitii practice - sesiunea 4: Structuri de date"""
"""
Se dau doua variabile, x = 10, z = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""
"""
x = 10
z = 2
y = x + z
print(y)  # 12
y = x - z
print(y)  # 8
y = x * z
print(y)  # 20
y = x / z
print(y)  # 5.0
y = x ** z
print(y)  # 100
y = x // z
print(y)  # 5
y = x % z
print(y)  # 0
"""
"""
list1 = ["abc", 34, True, 40, "male", "male"]
print(list1)
print(list1[0])
print(len(list1))
list1[0] = 123
print(list1[0])
list1.append("female")
print(list1)
list1.insert(0, "child")
print(list1)
list1.pop(5)
print(list1)
element_sters = list1.pop(5)
print(element_sters)
print(list1)
list1.remove("female")
print(list1)
"""
"""
EX1: 
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""
print("ex 1 - rezolvare")

"""
EX2:
a. Defineste o lista numita filme_preferate, cu cel putin 3 elemente.
b. Inverseaza lista folosind slicing. (ca la string)
c. Folosind if, verifica daca lista este goala sau nu,
si afiseaza un mesaj corespunzator pentru fiecare situatie.
"""
print("ex 2 - rezolvare")

"""
EX3: Se da structura de date cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8].
a. Verifica tipul structurii de date dat.
b. Accesand metodele de pe lista, sorteaza lista cifre.
c. Verifica daca 9 este in lista cifre. Afiseaza un mesaj corespunzator.
"""
print("ex 3 - rezolvare")

"""
EX4: Defineste o lista si exploreaza metodele ajutatoare ale listelor. 
"""
print("ex 4 - rezolvare")

"""
EX5: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
print("ex 5 - rezolvare")

"""
EX6:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""
print("ex 6 - rezolvare")

"""
EX7: 
a. Defineste un dictionar, numit student1, cu urmatoarele chei:
nume, prenume, varsta, an_studiu, facultate, medie. 
Valorile le alegi tu.
b. Afiseaza lungimea dictionarului.
c. Printeaza prenumele studentului.
d. Adauga o noua pereche cheie-valoare, cu tara in care studiaza studentul.
e. Verifica daca dictionarul contine cheia oras.
"""
print("ex 7 - rezolvare")

"""
EX8:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
ingrediente, timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""
print("ex 8 - rezolvare")

"""
EX9:
a. Se da un dictionar cu contacte din agenda telefonica:
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
b. Aurel si-a schimbat numarul de telefon. Actualizeaza-l.
c. Ai obtinut numarul de telefon a lui Mihai. Adauga-l in contacte.
d. Maria a plecat in strainatate si nu mai are numar de telefon. Sterge-l.
e. Verifica daca ai numarul Mihaelei si afiseaza un mesaj corespunzator.
"""
print("ex 9 - rezolvare")