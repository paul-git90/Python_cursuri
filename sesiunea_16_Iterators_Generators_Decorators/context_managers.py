"""
Context managers în Python sunt mecanisme care gestionează resursele de o manieră sigură și eficientă, asigurându-se că
anumite acțiuni sunt realizate la începutul și sfârșitul unui bloc de cod, chiar și în caz de erori. Acestea sunt
folosite cel mai adesea pentru gestionarea corectă a resurselor precum fișierele, conexiunile la baze de date sau
lock-urile de sincronizare.

Cea mai comună utilizare a unui context manager este împreună cu declarația with.

De ce avem nevoie de context managers?
Gestionarea corectă a resurselor este crucială. De exemplu, atunci când deschidem un fișier sau stabilim o conexiune
la o bază de date, este important să ne asigurăm că acele resurse sunt eliberate corect, chiar dacă apare o eroare în
timpul execuției. Context managers fac asta automat.
"""
# Exemple uzuale:
# Unul dintre cele mai simple exemple de context manager este utilizarea fișierelor:

with open('fisier.txt', 'r') as file:
    continut = file.read()

# În acest exemplu:
# open() deschide fișierul.
# with asigură că, la finalul blocului de cod, fișierul va fi închis automat,
# chiar dacă apare o eroare în timpul citirii.

# În mod tradițional, fără context managers, ar fi fost necesar să scriem manual codul de eliberare a resurselor:

file = open('fisier.txt', 'r')
try:
    continut = file.read()
finally:
    file.close()  # Trebuie să ne asigurăm că închidem fișierul, chiar dacă apare o eroare

"""
Cum funcționează context managers?
Context managers implementează două metode esențiale:

__enter__(): Această metodă este apelată la începutul blocului with. De obicei, ea inițializează și returnează resursa 
care va fi utilizată în acel context (de exemplu, un fișier sau o conexiune la o bază de date).

__exit__(exc_type, exc_value, traceback): Această metodă este apelată la ieșirea din blocul with, indiferent dacă 
execuția a fost finalizată cu succes sau din cauza unei erori. De obicei, aici sunt curățate sau eliberate resursele 
(cum ar fi închiderea fișierelor sau conexiunilor).

Crearea unui context manager personalizat:
Putem crea propriul context manager implementând aceste două metode, __enter__ și __exit__, într-o clasă.

Exemplu de context manager personalizat care lucrează cu fișiere:
"""


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f"Deschiderea fișierului {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Închiderea fișierului {self.filename}")
        self.file.close()


# Utilizarea context manager-ului personalizat
with FileManager('fisier.txt', 'w') as f:
    f.write("Acesta este un exemplu de utilizare a context manager-ului.")

# Output:
# Deschiderea fișierului fisier.txt
# Închiderea fișierului fisier.txt

"""
Cum funcționează exemplul de mai sus:
Când intrăm în blocul with, Python apelează metoda __enter__(), care deschide fișierul și îl returnează.
La ieșirea din blocul with, indiferent dacă execuția a fost finalizată cu succes sau dacă s-a aruncat o excepție, 
Python apelează metoda __exit__(), care închide fișierul.
Utilizarea decoratoarelor pentru context managers:
Există o altă modalitate de a crea context managers, mai ușoară și mai rapidă, folosind decoratori, în special 
funcția contextlib.contextmanager.
"""

# Exemplu cu decorator:

from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode):
    print(f"Deschiderea fișierului {filename}")
    file = open(filename, mode)
    try:
        yield file  # Punctul în care funcția suspendă și permite utilizarea resursei
    finally:
        print(f"Închiderea fișierului {filename}")
        file.close()


# Utilizarea context manager-ului
with file_manager('fisier.txt', 'w') as f:
    f.write("Exemplu folosind contextlib pentru context managers.")

"""
Cum funcționează decoratoarele pentru context managers:
@contextmanager transformă funcția într-un context manager.
yield împarte funcția în două părți: tot ce este înainte de yield reprezintă ceea ce se întâmplă când intrăm în blocul 
with, iar codul de după yield este ceea ce se execută când ieșim din blocul with.
Avantajele context managers:
Gestionarea automată a resurselor: Nu mai este nevoie să ne amintim să închidem manual fișiere sau să eliberăm alte 
resurse. Context managers fac asta automat.
Cod mai curat: Codul devine mai ușor de citit și gestionat, eliminând nevoia de blocuri try/finally pentru curățare.
Tratarea corectă a excepțiilor: Context managers asigură eliberarea resurselor chiar și în caz de eroare, evitând 
scurgerile de memorie sau blocajele.
Alte exemple de utilizare:
Lock-uri de sincronizare pentru gestionarea accesului concurent la resurse partajate.
Conexiuni la baze de date care trebuie deschise și închise corect.
Lucrul cu fișiere temporare sau alte resurse care trebuie create și distruse la momentul potrivit.
Context managers sunt o parte esențială a limbajului Python și sunt folosiți pe scară largă pentru a face gestionarea 
resurselor mai sigură și mai eficientă.
"""
