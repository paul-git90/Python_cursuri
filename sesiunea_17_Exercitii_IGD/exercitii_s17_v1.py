"""
1.	Iterators

Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d
"""


class ReverseIterator:
    def __init__(self, data):
        self.data = data  # Stocăm lista de date în iterator
        self.index = len(data)  # Inițializăm indexul la lungimea listei (care va scădea în timpul iterației)

    def __iter__(self):
        return self  # Metoda iter trebuie să returneze obiectul iteratorului

    def __next__(self):
        if self.index == 0:  # Dacă indexul ajunge la 0, nu mai avem elemente
            raise StopIteration  # Aruncăm excepția care semnalează sfârșitul
        self.index -= 1  # Reducem indexul cu 1
        return self.data[self.index]  # Returnăm elementul de la indexul curent


# Exemplu de folosire:
note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)

# Afișează elementele din lista 'note' în ordine inversă:
print(next(rev_it))  # Printează 10
print(next(rev_it))  # Printează 8
print(next(rev_it))  # Printează 5
print(next(rev_it))  # Printează 7
print(next(rev_it))  # Printează 3

# Dacă mai încercăm să apelăm `next`, va arunca StopIteration.
# print(next(rev_it))  # Acum arunca StopIteration

for element in ReverseIterator(note):
    print(element)


# todo Logica din spate
"""
Pentru a implementa un iterator care parcurge o colecție în sens opus, vom crea o clasă numită ReverseIterator. 
Aceasta trebuie să respecte două reguli pentru a fi un iterator valid:

Să implementeze metoda __iter__, care va returna obiectul iteratorului.
Să implementeze metoda __next__, care va returna următorul element din secvență.
Logica din spate este simplă:

__iter__: aceasta va întoarce chiar obiectul pe care vrem să-l folosim ca iterator.
__next__: va returna elementele din colecție în ordine inversă, până când ajungem la capăt. Odată ce am terminat, 
va arunca o excepție StopIteration, care semnalează sfârșitul iterației.
Pași de implementare:
Stocarea listei și inițializarea indexului: Când inițializăm iteratorul, stocăm lista și setăm un index care 
pornește de la ultimul element (indicele final).
Metoda __next__: De fiecare dată când se apelează next(), indexul scade cu 1 și returnează elementul corespunzător 
din listă. Când nu mai sunt elemente (adică indexul ajunge sub 0), va arunca StopIteration.
"""

"""
Explicația pas cu pas:
Inițializare (__init__):

Stocăm lista dată în self.data.
Setăm self.index la lungimea listei, pentru a începe de la ultimul element.
__iter__:

Metoda __iter__ face obiectul iterator returnabil ca pe sine, astfel încât să poate fi iterat în contextul unui for 
sau al unei apelări next.
__next__:

De fiecare dată când apelăm next(), index se reduce cu 1 și returnează elementul corespunzător din listă.
Dacă index ajunge la 0, atunci nu mai sunt elemente de iterat, și StopIteration este aruncat pentru a opri bucla.
Utilizare:
Poți folosi acest iterator într-o buclă for dacă implementezi doar metoda __iter__ și __next__. De exemplu, următorul 
cod va funcționa automat:

for element in ReverseIterator(note):
    print(element)

"""