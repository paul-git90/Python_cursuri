"""
Recapitulare sesiunea 1 si 2
Operatori, condiționale
"""
"""
1. Citește de la tastatură:
-	lungimea;
-	lățimea.
   Afișează: 'Aria dreptunghiului este x'.
"""
# citirea de la tastatura
lungimea = float(input("Introduceti lungimea dreptunghiului: "))
latimea = float(input("Introduceti latimea dreptunghiului: "))
# calcularea ariei
aria_dreptunghi = lungimea * latimea
# afisarea
print(f"Aria dreptunghiului este: {aria_dreptunghi:.2f} unitati patrate")
"""
2. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
-	afișează de câte ori apare cuvântul 'the';
"""
# Definirea stringului
text = 'Coral is either the stupidest animal or the smartest rock'
# Numărarea aparițiilor cuvântului 'the'
count_the = text.count('the')
# Afișarea rezultatului
print(f"Cuvântul 'the' apare de {count_the} ori în text.")
"""
3. Același string:
●	Afișează de câte ori apare cuvântul 'the';
●	Printează rezultatul.
"""
count_the = text.count(' the ')
print(f"Cuvântul 'the' apare de {count_the} ori în text.")
"""
print(f"Cuvântul 'the' apare de {count_the} ori în text.")
"""
"""
4. Același string:
●	Folosește un assert ca să verifici dacă acest string conține doar numere.
"""
# Definirea stringului
text = '6789'
# Verificarea dacă stringul conține doar numere
assert text.isdigit(), "Stringul nu conține doar numere."
# Dacă assert nu ridică o excepție, afișăm un mesaj de confirmare
print("Stringul conține doar numere.")
"""
5. Exercițiu:
-	citește de la tastatură un string de dimensiune impară;
-	afișează caracterul din mijloc.
"""
# Citirea unui string de la tastatură
text = input("Introduceți un string de dimensiune impară: ")
# Verificarea dacă lungimea stringului este impară
assert len(text) % 2 == 1, "Stringul nu are dimensiune impară."
# Calcularea poziției caracterului din mijloc
mijloc = len(text) // 2
# Afișarea caracterului din mijloc
print(f"Caracterul din mijloc este: '{text[mijloc]}'")
"""
6. Folosind o singură linie de cod :
-	citește un string de la tastatură (ex: 'alabala portocala');
-	salvează fiecare cuvânt într-o variabilă;
-	printează ambele variabile pentru verificare.
"""
cuvant1, cuvant2 = (input("Introduceți un string cu două cuvinte separate printr-un spațiu: ")
                    .split()); print(cuvant1, cuvant2)
"""
7. Exercițiu:
-	citește un string de la tastatură (ex: alabala portocala);
-	salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
-	capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
"""
# Citirea unui string de la tastatură
text = input("Introduceți un string: ")
# Salvarea primului caracter într-o variabilă
primul_caracter = text[0]
# Înlocuirea tuturor aparițiilor primului caracter cu varianta sa capitalizată,
# exceptând primul și ultimul caracter
text_modificat = (primul_caracter +
                  text[1:-1].replace(primul_caracter, primul_caracter.upper()) +
                  text[-1])
# Afișarea stringului modificat
print(text_modificat)
"""
8.Exercițiu:
-	citește un user de la tastatură;
-	citește o parolă;
-	afișează: 'Parola pt user x este ***** și are x caractere';
-	***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****
"""
# Citirea numelui de utilizator de la tastatură
user = input("Introduceți numele de utilizator: ")
# Citirea parolei de la tastatură
parola = input("Introduceți parola: ")
# Crearea măștii parolei
masca_parola = '*' * len(parola)
# Afișarea mesajului
print(f"Parola pt user {user} este {masca_parola} și are {len(parola)} caractere")
