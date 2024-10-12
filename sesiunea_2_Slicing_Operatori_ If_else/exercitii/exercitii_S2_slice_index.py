"""
Exercitii din curs
"""
"""
EX1: Se da string-ul prop3 = 'Concertul va avea loc maine.'
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""
prop3 = 'Concertul va avea loc maine.'
first_word = prop3[:9]
print(first_word)
first_char = prop3[:3]
print(first_char)
print(prop3[::-1])
"""
EX2: Se da variabila prop1 = 'Andy este prescurtarea de la Andrei.'
a. Afiseaza primul caracter.
b. Afiseaza al 4-lea caracter.
c. Afiseaza ultimul caracter.
"""
prop1 = 'Andy este prescurtarea de la Andrei.'
print(prop1[0:1])
print(prop1[3:4])
print(prop1[-1:])
"""
EX3: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""
prop2 = 'Masina e rosie.'
print(len(prop2))
"""
EX4: Se da string-ul my_str = 'vacanta'.
a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.
c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.
d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
"""
my_str = "vacanta"
print(my_str.find('a'))
print(my_str.count('a'))
print(my_str.capitalize())
print(my_str.upper())
"""
EX5: Exploreaza urmatoarele metode ajutatoare ale string-ului:
a. endswith()
b. index()
c. lower()
d. replace()
e. strip()
"""
print(my_str.endswith('a'))
print(my_str.index('n'))
print(my_str.lower())
print(my_str.strip('a'))
