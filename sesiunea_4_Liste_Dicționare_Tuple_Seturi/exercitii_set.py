"""
Exercitii din curs: Structuri de date
  SET - neordonata, elemente unice, mutabila, poate fi editata, elementele nu pot fi accesate dupa index.
Un set în Python este o colecție neordonată de elemente unice. Elementele dintr-un set nu pot fi duplicate, ceea ce face
seturile utile pentru stocarea colecțiilor de elemente distincte și pentru efectuarea operațiilor matematice de mulțimi,
cum ar fi intersecția, uniunea, diferența și diferența simetrică.
"""
"""
EX5: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.add(6)
print(my_set)
my_set.add(1)
print(my_set)
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)


"""
Defineste un set si exploreaza metodele ajutatoare ale seturilor
"""
# Definirea setului
fructe_set = {"mar", "banana", "cireasa"}

# Metoda add - Adaugă un element în set.
fructe_set.add("portocala")
print(fructe_set)  # Output: {'banana', 'portocala', 'mar', 'cireasa'}

# Metoda update - Adaugă mai multe elemente în set.
fructe_set.update(["kiwi", "ananas"])
print(fructe_set)  # Output: {'banana', 'portocala', 'kiwi', 'ananas', 'mar', 'cireasa'}

# Metoda remove - Elimină un element din set. Dacă elementul nu există, aruncă o eroare.
fructe_set.remove("banana")
print(fructe_set)  # Output: {'portocala', 'kiwi', 'ananas', 'mar', 'cireasa'}

# Metoda discard - Elimină un element din set. Dacă elementul nu există, nu aruncă o eroare.
fructe_set.discard("banana")  # Nu aruncă eroare
print(fructe_set)  # Output: {'portocala', 'kiwi', 'ananas', 'mar', 'cireasa'}

# Metoda pop - Elimină și returnează un element arbitrar din set.
element_eliminat = fructe_set.pop()
print(element_eliminat)  # Output: Un element arbitrar din set
print(fructe_set)  # Output: Set-ul fără elementul eliminat

# Metoda clear - Elimină toate elementele din set.
fructe_set.clear()
print(fructe_set)  # Output: set()

# Metoda union - Returnează un nou set care conține toate elementele din ambele seturi.
set1 = {"mar", "banana"}
set2 = {"portocala", "kiwi"}
set3 = set1.union(set2)
print(set3)  # Output: {'banana', 'portocala', 'kiwi', 'mar'}

# Metoda intersection - Returnează un nou set cu elementele comune ambelor seturi.
set1 = {"mar", "banana", "portocala"}
set2 = {"portocala", "kiwi", "banana"}
set3 = set1.intersection(set2)
print(set3)  # Output: {'banana', 'portocala'}

# Metoda difference - Returnează un nou set cu elementele care sunt doar în primul set.
set1 = {"mar", "banana", "portocala"}
set2 = {"portocala", "kiwi"}
set3 = set1.difference(set2)
print(set3)  # Output: {'mar', 'banana'}

# Metoda symmetric_difference - Returnează un nou set cu elementele care sunt în oricare dintre seturi, dar nu în ambele.
set1 = {"mar", "banana", "portocala"}
set2 = {"portocala", "kiwi"}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {'banana', 'mar', 'kiwi'}

# Metoda copy - Returnează o copie superficială a setului.
set1 = {"mar", "banana", "portocala"}
set_copy = set1.copy()
print(set_copy)  # Output: {'banana', 'portocala', 'mar'}

# Metoda isdisjoint - Verifică dacă două seturi sunt disjuncte (nu au elemente comune).
set1 = {"mar", "banana", "portocala"}
set2 = {"kiwi", "ananas"}
print(set1.isdisjoint(set2))  # Output: True

# Metoda issubset - Verifică dacă un set este subsetul altui set
set1 = {"mar", "banana"}
set2 = {"mar", "banana", "portocala"}
print(set1.issubset(set2))  # Output: True

# Metoda issuperset - Verifică dacă un set este supersetul altui set.
set1 = {"mar", "banana", "portocala"}
set2 = {"mar", "banana"}
print(set1.issuperset(set2))  # Output: True

# Funcția len - Returnează numărul de elemente din set.
set1 = {"mar", "banana", "portocala"}
print(len(set1))  # Output: 3

# Operatorul in - Verifică dacă un element este în set.
print("mar" in set1)  # Output: True

# Operatorul not in - Verifică dacă un element nu este în set.
print("kiwi" not in set1)  # Output: True