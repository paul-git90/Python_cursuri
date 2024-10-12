"""
1.	Creeaza următoarele variabile: o lista, o tupla, un string. Itereaza prin fiecare dintre ele, prima data
folosind un o bucla for, iar apoi folosind un iterator (ne vom folosi de metodele iter și next):

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(f’Primul element: {next(my_iterator)}’)
print(fAl doilea element: {next(my_iterator)}’)
print(f’Al treilea element: {next(my_iterator)}’)
print(f’Aici va da eroare: {next(my_iterator)}’)
"""
# Pasul 1: Crearea variabilelor

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_string = "Hello"

# Pasul 2: Iterarea prin fiecare variabilă folosind o buclă for

# Iterarea prin lista
print("Iterare prin lista:")
for item in my_list:
    print(item)

# Iterarea prin tuplă
print("\nIterare prin tuplă:")
for item in my_tuple:
    print(item)

# Iterarea prin string
print("\nIterare prin string:")
for char in my_string:
    print(char)

# Pasul 3: Iterarea folosind un iterator cu iter() și next()

# Iterarea prin lista folosind un iterator
print("\nIterare prin lista folosind un iterator:")
my_iterator = iter(my_list)
print(f'Primul element: {next(my_iterator)}')
print(f'Al doilea element: {next(my_iterator)}')
print(f'Al treilea element: {next(my_iterator)}')

try:
    print(f'Aici va da eroare: {next(my_iterator)}')
except StopIteration:
    print("Aici a apărut o eroare: iteratorul a atins sfârșitul.")

# Iterarea prin tuplă folosind un iterator
print("\nIterare prin tuplă folosind un iterator:")
my_iterator = iter(my_tuple)
print(f'Primul element: {next(my_iterator)}')
print(f'Al doilea element: {next(my_iterator)}')
print(f'Al treilea element: {next(my_iterator)}')

try:
    print(f'Aici va da eroare: {next(my_iterator)}')
except StopIteration:
    print("Aici a apărut o eroare: iteratorul a atins sfârșitul.")

# Iterarea prin string folosind un iterator
print("\nIterare prin string folosind un iterator:")
my_iterator = iter(my_string)
print(f'Primul caracter: {next(my_iterator)}')
print(f'Al doilea caracter: {next(my_iterator)}')
print(f'Al treilea caracter: {next(my_iterator)}')

try:
    print(f'Aici va da eroare: {next(my_iterator)}')
except StopIteration:
    print("Aici a apărut o eroare: iteratorul a atins sfârșitul.")

"""
Rezumat
Acest cod va crea o listă, o tuplă și un string, va itera prin fiecare dintre ele folosind o buclă for, iar apoi 
va folosi un iterator cu iter() și next() pentru a accesa fiecare element. La final, va prinde excepția StopIteration 
pentru a gestiona cazul în care iteratorul ajunge la sfârșitul colecției.
"""