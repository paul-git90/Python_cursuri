"""
Exercitii din curs: Structuri de date
    Dictionar - ordonata, keys unice, mutabila, poate fi editata, valorile sunt indexate dupa keys si pot fi accesate.
Un dicționar în Python este o structură de date care stochează perechi cheie-valoare. Fiecare cheie este unică și este
utilizată pentru a accesa valoarea asociată acesteia. Dicționarele sunt mutabile, ceea ce înseamnă că se pot modifica
după ce au fost create (adică se pot adăuga, elimina sau modifica perechi cheie-valoare).

Utilitatea dicționarelor:

Stocare rapidă și eficientă a datelor:
Dicționarele oferă o metodă eficientă de a stoca și accesa datele folosind chei unice.

Mapare și relaționare:

Dicționarele sunt ideale pentru maparea relațiilor între date, de exemplu, stocarea informațiilor despre studenți, unde
cheile ar putea fi ID-uri de studenți și valorile ar putea fi detalii despre studenți.

Căutare rapidă:

Accesarea valorilor în dicționare este foarte rapidă, având complexitatea O(1) în medie, ceea ce le face foarte utile
pentru operațiuni de căutare și recuperare.
"""
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
student1 = {
    "nume": "Paul",
    "prenume": "Eugen",
    "varsta": 34,
    "an_studiu": 4,
    "facultatea": "Fizica",
    "medie": 9.89
}
print(student1)
print(len(student1))
print(student1["nume"])
student1["tara"] = "Romania"
print(student1)
if "oras" in student1:
    print("Cheia 'oras' există în dicționar.")
else:
    print("Cheia 'oras' nu există în dicționar.")
"""
EX8:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
ingrediente, timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""
# a. Citire date de la tastatura
nume_reteta = input("Introduceți numele rețetei: ")
ingrediente = input("Introduceți ingredientele rețetei (separate prin virgulă): ")
timp_preparare = input("Introduceți timpul de preparare (în minute): ")

# b. Salvare date într-un dicționar
reteta = {
    "nume": nume_reteta,
    "ingrediente": ingrediente.split(","),
    "timp_preparare": int(timp_preparare)
}

# Afișare dicționar
print("Dicționar inițial:", reteta)

# c. Actualizare nume rețetă cu litere mari
reteta["nume"] = reteta["nume"].upper()

# Afișare dicționar actualizat
print("Dicționar actualizat:", reteta)
"""
EX9:
a. Se da un dictionar cu contacte din agenda telefonica:
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
b. Aurel si-a schimbat numarul de telefon. Actualizeaza-l.
c. Ai obtinut numarul de telefon a lui Mihai. Adauga-l in contacte.
d. Maria a plecat in strainatate si nu mai are numar de telefon. Sterge-l.
e. Verifica daca ai numarul Mihaelei si afiseaza un mesaj corespunzator.
"""
# a. Se dă un dicționar cu contacte din agenda telefonică
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}

# b. Aurel și-a schimbat numărul de telefon. Actualizează-l.
contacte['Aurel'] = '0745123456'
print("Contacte actualizate:", contacte)

# c. Ai obținut numărul de telefon al lui Mihai. Adaugă-l în contacte.
contacte['Mihai'] = '0733123456'
print("Contacte actualizate cu Mihai:", contacte)

# d. Maria a plecat în străinătate și nu mai are număr de telefon. Șterge-l.
del contacte['Maria']
print("Contacte după ștergerea Mariei:", contacte)

# e. Verifică dacă ai numărul Mihaelei și afișează un mesaj corespunzător.
if 'Mihaela' in contacte:
    print("Numărul Mihaelei este:", contacte['Mihaela'])
else:
    print("Nu există numărul Mihaelei în agendă.")


"""
Defineste un dictionar si exploreaza metodele ajutatoare ale dictionarelor
"""
student = {
    "nume": "Ion Popescu",
    "varsta": 21,
    "universitate": "Universitatea din București",
    "cursuri": ["Matematică", "Informatică", "Fizică"]
}

# dict.get(key[, default]):
# Returnează valoarea pentru cheia specificată. Dacă cheia nu există, returnează default (implicit None).
varsta = student.get("varsta")
facultate = student.get("facultate", "Necunoscut")
print(varsta)      # Output: 21
print(facultate)   # Output: Necunoscut

# dict.keys():
# Returnează o vedere a tuturor cheilor din dicționar.
chei = student.keys()
print(chei)  # Output: dict_keys(['nume', 'varsta', 'universitate', 'cursuri'])

# dict.values():
# Returnează o vedere a tuturor valorilor din dicționar.
valori = student.values()
print(valori)  # Output: dict_values(['Ion Popescu', 21, 'Universitatea din București', ['Matematică', 'Informatică', 'Fizică']])

# dict.items():
# Returnează o vedere a tuturor perechilor cheie-valoare din dicționar sub formă de tupluri.
elemente = student.items()
print(elemente)  # Output: dict_items([('nume', 'Ion Popescu'), ('varsta', 21), ('universitate', 'Universitatea din București'), ('cursuri', ['Matematică', 'Informatică', 'Fizică'])])

# dict.update([other]):
# Actualizează dicționarul cu perechile cheie-valoare dintr-un alt dicționar sau dintr-o secvență de perechi cheie-valoare.
actualizari = {"varsta": 22, "specializare": "Informatică"}
student.update(actualizari)
print(student)
# Output: {'nume': 'Ion Popescu', 'varsta': 22, 'universitate': 'Universitatea din București', 'cursuri': ['Matematică', 'Informatică', 'Fizică'], 'specializare': 'Informatică'}

# dict.pop(key[, default]):
# Elimină cheia specificată și returnează valoarea asociată. Dacă cheia nu există, returnează default (sau ridică o excepție KeyError dacă default nu este furnizat).
varsta = student.pop("varsta")
print(varsta)  # Output: 22
print(student)
# Output: {'nume': 'Ion Popescu', 'universitate': 'Universitatea din București', 'cursuri': ['Matematică', 'Informatică', 'Fizică'], 'specializare': 'Informatică'}

# dict.clear():
# Elimină toate elementele din dicționar.
student.clear()
print(student)  # Output: {}

# dict.copy():
# Returnează o copie superficială a dicționarului.
student = {
    "nume": "Ion Popescu",
    "varsta": 21,
    "universitate": "Universitatea din București",
    "cursuri": ["Matematică", "Informatică", "Fizică"]
}
copie_student = student.copy()
print(copie_student)
# Output: {'nume': 'Ion Popescu', 'varsta': 21, 'universitate': 'Universitatea din București', 'cursuri': ['Matematică', 'Informatică', 'Fizică']}

# dict.setdefault(key[, default]):
# Dacă cheia există, returnează valoarea acesteia. Dacă nu, inserează cheia cu valoarea default și returnează default.
specializare = student.setdefault("specializare", "Nespecificat")
print(specializare)  # Output: Nespecificat
print(student)
# Output: {'nume': 'Ion Popescu', 'varsta': 21, 'universitate': 'Universitatea din București', 'cursuri': ['Matematică', 'Informatică', 'Fizică'], 'specializare': 'Nespecificat'}

# Metode avansate
# Comprehensiuni de Dicționare
# Comprehensiunile de dicționare permit crearea de dicționare într-un mod concis și expresiv.
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Utilizarea collections.defaultdict
# defaultdict din modulul collections permite crearea de dicționare cu valori implicite, astfel încât nu trebuie să verificați dacă o cheie există înainte de a adăuga o valoare.
from collections import defaultdict

# Dicționar de liste
dd_list = defaultdict(list)
dd_list['a'].append(1)
dd_list['a'].append(2)
dd_list['b'].append(3)
print(dd_list)
# Output: defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# Dicționar de contor
dd_int = defaultdict(int)
dd_int['a'] += 1
dd_int['a'] += 2
dd_int['b'] += 3
print(dd_int)
# Output: defaultdict(<class 'int'>, {'a': 3, 'b': 3})

# Utilizarea collections.OrderedDict
# OrderedDict din modulul collections păstrează ordinea de inserare a elementelor.
from collections import OrderedDict

ord_dict = OrderedDict()
ord_dict['banana'] = 3
ord_dict['apple'] = 4
ord_dict['pear'] = 1
ord_dict['orange'] = 2
print(ord_dict)
# Output: OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])

# Utilizarea collections.Counter
# Counter este o subclasă a dicționarului care este utilă pentru numărarea obiectelor hashabile.
from collections import Counter

fruits = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana', 'apple']
counter = Counter(fruits)
print(counter)
# Output: Counter({'apple': 3, 'orange': 2, 'pear': 1, 'banana': 1})

# Utilizarea dict.fromkeys()
# Metoda fromkeys() creează un nou dicționar cu chei specificate și o valoare comună.
keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)
# Output: {'a': 0, 'b': 0, 'c': 0}

# Sortarea Dicționarelor
# Puteți sorta dicționarele după chei sau valori folosind funcțiile sorted() și itemgetter din modulul operator.
# Exemplu: Sortarea după chei:
unsorted_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_dict = dict(sorted(unsorted_dict.items()))
print(sorted_dict)
# Output: {'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}

# Exemplu: Sortarea după valori:
from operator import itemgetter

sorted_dict_by_value = dict(sorted(unsorted_dict.items(), key=itemgetter(1)))
print(sorted_dict_by_value)
# Output: {'pear': 1, 'orange': 2, 'banana': 3, 'apple': 4}

# Fusionarea Dicționarelor
# În Python 3.9 și versiuni ulterioare, puteți utiliza operatorul | pentru a fuziona dicționare.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)
# Output: {'a': 1, 'b': 3, 'c': 4}

# Verificarea Existenței unei Chei
# Pentru a verifica dacă o cheie există într-un dicționar, puteți utiliza operatorul in.
if 'nume' in student:
    print("Cheia 'nume' există în dicționar.")
# Output: Cheia 'nume' există în dicționar.



