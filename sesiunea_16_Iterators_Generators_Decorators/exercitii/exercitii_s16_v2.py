"""
2.	Atunci cand nu mai contine elemente, un iterator va arunca o excepție de tipul StopIteration. Folosește un bloc
try except pe codul de mai sus pentru a gestiona aceasta excepție si pentru a te asigura ca programul tău ajunge la
final cu un exit code de succes (adica 0).
"""
import sys

# 1. Definirea variabilelor
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_string = "abcdef"

# 2. Iterația prin listă folosind for
print("Iterarea prin lista:")
for item in my_list:
    print(item)

# 3. Iterația prin listă folosind un iterator
print("\nIterarea prin lista folosind un iterator:")
my_iterator = iter(my_list)

try:
    print(f'Primul element: {next(my_iterator)}')
    print(f'Al doilea element: {next(my_iterator)}')
    print(f'Al treilea element: {next(my_iterator)}')
    print(f'Aici va da eroare: {next(my_iterator)}')  # Aici va arunca StopIteration
except StopIteration:
    print("Iteratorul a ajuns la final.")

# 4. Iterația prin tupla folosind for
print("\nIterarea prin tupla:")
for item in my_tuple:
    print(item)

# 5. Iterația prin tupla folosind un iterator
print("\nIterarea prin tupla folosind un iterator:")
my_tuple_iterator = iter(my_tuple)

try:
    print(f'Primul element: {next(my_tuple_iterator)}')
    print(f'Al doilea element: {next(my_tuple_iterator)}')
    print(f'Al treilea element: {next(my_tuple_iterator)}')
    print(f'Aici va da eroare: {next(my_tuple_iterator)}')  # Aici va arunca StopIteration
except StopIteration:
    print("Iteratorul tupla a ajuns la final.")

# 6. Iterația prin string folosind for
print("\nIterarea prin string:")
for char in my_string:
    print(char)

# 7. Iterația prin string folosind un iterator
print("\nIterarea prin string folosind un iterator:")
my_string_iterator = iter(my_string)

try:
    print(f'Primul caracter: {next(my_string_iterator)}')
    print(f'Al doilea caracter: {next(my_string_iterator)}')
    print(f'Al treilea caracter: {next(my_string_iterator)}')
    print(f'Aici va da eroare: {next(my_string_iterator)}')  # Aici va arunca StopIteration
except StopIteration:
    print("Iteratorul string a ajuns la final.")

# 8. Finalizare cu un exit code de succes
# import sys
# sys.exit(0)

"""
Explicația codului:
Definirea variabilelor: Am creat o listă, o tuplă și un string.
Iterația prin listă folosind for: Am folosit o buclă for pentru a itera prin lista my_list.
Iterația prin listă folosind un iterator: Am folosit iter() pentru a crea un iterator și next() pentru a 
obține elementele.
Am inclus un bloc try-except pentru a gestiona excepția StopIteration. Dacă iteratorul nu mai are elemente, 
se va prinde excepția și se va afișa un mesaj corespunzător.
Iterația prin tuplă și string: Am repetat aceleași etape pentru tuplă și string, asigurându-ne că gestionăm 
excepția pentru fiecare iterator.
Exit code: Am folosit sys.exit(0) pentru a ieși din program cu un cod de succes.
Executare
Poți rula acest cod într-un mediu Python și ar trebui să gestioneze excepțiile corect, arătând mesajele 
corespunzătoare atunci când iteratorii ajung la final.
"""

sys.exit(0)

