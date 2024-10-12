"""
4.	Decorators
Implementați următorii decoratori:
-	timeit – decorator care măsoară timpul de execuție al unei funcții
-	logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
"""

"""
1. timeit – Măsoară timpul de execuție al unei funcții
Decoratorul timeit se folosește pentru a măsura timpul de execuție al unei funcții. Pentru a face asta, 
putem folosi modulul time din Python. Acesta ne permite să captăm momentul în care începe și se termină 
funcția, și să calculăm diferența.
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Începe măsurarea timpului
        result = func(*args, **kwargs)  # Execută funcția decorată
        end_time = time.time()  # Timpul după ce funcția s-a terminat
        elapsed_time = end_time - start_time  # Timpul total de execuție
        print(f"Funcția {func.__name__} a durat {elapsed_time:.4f} secunde.")
        return result
    return wrapper


# Testare cu o funcție care durează câteva secunde
@timeit
def slow_function():
    time.sleep(2)
    return "Funcția a fost executată."


print(slow_function())

"""
Explicație:
start_time: Înregistrează timpul la începutul execuției funcției.
end_time: Înregistrează timpul după terminarea funcției.
elapsed_time: Diferența dintre cele două momente reprezintă timpul total de execuție al funcției.
"""

"""
logger – Printează argumentele de intrare și rezultatul unei funcții
Acest decorator va intercepta apelurile funcției și va afișa argumentele 
cu care a fost apelată funcția și rezultatul returnat de aceasta.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Apelând funcția: {func.__name__}")
        print(f"Argumente: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)  # Execută funcția decorată
        print(f"Rezultatul funcției {func.__name__}: {result}")
        return result
    return wrapper


# Testare cu o funcție simplă
@logger
def add(a, b):
    return a + b


print(add(5, 3))

"""
Explicație:
Argumentele funcției sunt afișate folosind args și kwargs.
Rezultatul funcției este salvat în result și apoi afișat.
Decoratorul permite urmărirea detaliată a execuției funcției, 
inclusiv argumentele și rezultatul returnat.
"""

# Combinația celor doi decoratori:
# Putem folosi ambele decoratoare pe aceeași funcție, iar decoratoarele vor fi aplicate în ordine.


@logger
@timeit
def multiply(a, b):
    time.sleep(1)  # Simulează o întârziere
    return a * b


print(multiply(5, 7))

"""
Explicație:
Ordinea decoratoarelor: În acest caz, logger va intercepta apelul funcției multiply 
și va afișa argumentele și rezultatul, iar timeit va măsura cât timp durează execuția funcției.
"""
