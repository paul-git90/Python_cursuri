# Curs: String Slicing, metode string, Operatori, conditionale si Assert
## 📝 OBIECTIVE
1. String slicing - sa intelegem ce este și cum se face
2. String Methods - sa stim sa lucram cu ele
3. Tipuri de Operatori
Sa cunoastem tipurile principale de operatori
- De atribuire
- Artimetici
- De comparare
- Logici
4. Conditionalul if else (flow control)
Sa intelegem cum functioneaza if statement
- If simplu
- If/else
- If/elif/else

## 📌 String slicing 
- Putem accesa "felii" din string, folosind sintaxa
**my_str[start_pos:end_pos:pas]**
- Practic, extragem o parte dintr-un string, specificand indexul de la care sa pornim
si indexul final.
- start_pos = indexul de inceput (inclusiv); daca lipseste, este inceputul
string-ului (0)
- end_pos = indexul de final (EXCLUSIV)
- ❗ ATENTIE: Caracterul de la indexul final nu se va lua in considerare.
Practic vom extrage un string care va include ca ultimul caracter, cel aflat la **end_pos** - 1.
- pas = este optional - pasul cu care se merge; daca lipseste, valoarea lui
este 1
- daca pasul este negativ, se merge invers (de la final la inceput)
```python
info = 'Afara sunt 2 grade'

# Extragem string-ul care incepe cu index-ul 0 pana la index-ul 1, inclusiv
print(info[0:2]) # => 'Af'

# Extragem string-ul care incepe cu index-ul 0 pana la indexul 4, inclusiv
print(info[0:5]) # => 'Afara'

# Daca nu specificam end_pos, se va extrage string-ul
# pana la ultimul caracter, inclusiv
print(info[6:])  # => 'sunt 2 grade'

# Daca nu specificam start_pos, se va extrage string-ul
# incepand cu primul caracter.
print(info[:5])  # => 'Afara'

## Inversare string
print(info[::-1]) # => 'edarg 2 tnus arafA'
```

```python
"""
EX1: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""
```
## 📌 Tipul string - metode disponibile

### 🔸 Index(pozitie)
- String-ul este format din unul sau mai multe caractere.
- Fiecare caracter dintr-un string are un numar asociat/pozitie asociata, numit index.
- ❗ ATENTIE: indexul incepe de la 0.
- Exemplu:
```python
info = 'Afara sunt 2 grade'
print(info[0]) # => 'A' (primul caracter din string se afla la indexul 0)
print(info[1]) # => 'f'
print(info[5]) # => ' ' (la indexul 5 avem un spatiu gol)
```
- Cum aflam ce caracter avem la ultima pozitie din string?
```python
info = 'Afara sunt 2 grade'
# prima varianta - e o modalitate dar NU e indicata - DE CE?
print(info[17]) # => e

# a doua varianta (PREFERATA)
print(info[-1]) # => e
```

```python
"""
EX2: Se da variabila prop1 = 'Andy este prescurtarea de la Andrei"
a. Afiseaza primul caracter.
b. Afiseaza al 4-lea caracter.
c. Afiseaza ultimul caracter.
"""
```

### 🔸 Lungimea unui string
- Functia len() ne spune cate caractere are string-ul.
```python
info = 'Afara sunt 2 grade'

# afisam lungimea string-ului info
print(len(info)) # => 18
```

```python
"""
EX3: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""
```


### 🔸 Metode ajutatoare string
- Daca dupa my_str punem. ajungem la functiile ajutatoare.
- Exemple: upper, lower, replace, count etc.
- Accesam descrierea acestora apasand CTRL + Click pe numele lor

```python
str1 = 'banana'
print(str1.upper()) # => 'BANANA' (tot cu litere mari)
```

```python
"""
EX4: Se da string-ul my_str = 'vacanta'.
a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.
c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.
d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
"""
```

```python
"""
EX5: Exploreaza urmatoarele metode ajutatoare ale string-ului:
a. endswith()
b. index()
c. lower()
d. replace()
e. strip()
"""
```



## 📌 Operatori aritmetici

| Operator | Name           | Example |
|----------|----------------|---------|
| +        | Addition       | x + y   |
| -        | Substraction   | x - y   |
| *        | Multiplication | x * y   |
| /        | Division       | x / y   |
| %        | Modulus        | x % y   |
| **       | Exponentiation | x ** y  |
| //       | Floor division | x // 2  |

```python
x = 2
y = 3

# # adunarea
print(x + y) # 5
# # scaderea
print(y - x) # 1
# # inmultirea
print(x * y) # 6
# # impartirea
print(y / x) # 1.5
# # restul impartirii
print(y % x) # 1
# # ridicarea la putere
print(x ** y) # 2 la puterea 3 -> 8
# # floor division
print(y // x) # 3 // 2; 1.5 => 1

# inmultirea pe string-uri
my_str = 'a'

# vreau sa afisez mesajul 'aaa'
print(my_str + my_str + my_str)
print(my_str * 3)
```

### 🔸 Floor division: // operator
- Rotunjeste rezultatul fata de cel mai apropiat intreg

```python
x = 17
y = 2

# daca ambele numere sunt int -> rezultatul va fi int
print (x // y) # 8.5 -> rezultatul este 8

x = 17.8
y = 2

# daca cel putin unul din numere este float -> rezultatul va fi float 
print(x // y) # 8.9 -> rezultatul este 8.0


x = -17
y = 2
print(x // y) # -8.5 -> rezultatul este -9
```

```python
"""
EX6: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""
```

#### ❔ Pe ce principiu se rotunjeste?
Intregul catre care se orienteaza trebuie sa indeplineasca urmatoarea conditie: Rezultat rotunjit <= intregul rezultatului

## 📌 Operatori de atribuire
| Operator | Example | Same as   |
|----------|---------|-----------|
| =        | x = 5   | x = 5     |
| +=       | x += 3  | x = x + 3 |
| -=       | x -= 3  | x = x - 3 |
| *=       | x *= 3  | x = x * 3 |
| /=       | x /= 3  | x = x / 3 |


## 📌 Operatori logici

| Operator | Description                                            | Example               |
|----------|--------------------------------------------------------|-----------------------|
| and      | Returns True if both statements are true               | x < 5 and x < 10      |
| or       | Returns True if one of the statements is true          | x < 5 or x < 4        |
| not      | reverse the result, return False if the result is True | not(x < 5 and x < 10) |

```python
"""
EX7: Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu
rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand
si ruleaza exemplele si verifica output-ul.
"""

# Exemplul 1:
a = True
b = False
# print(not(a))
# print(not(b))

# Exemplul 2:
a = True
b = False
# x = not(a)
# y = not(b)
# print(a or b)
# print(x or y)
# print(a or x)
# print(x or b)

# Exemplul 3:
a = False
b = False
# x = not(a)
# y = not(b)
# print(a and b)
# print(a and x)
# print(y and b)
# print(x and y)
```

## 📌 Operatori de comparare

| Operator | Name                       | Example |
|----------|----------------------------|---------|
| ==       | Equal                      | x == y  |
| !=       | Not equal                  | x != y  |
| &gt;     | Greater than               | x > y   |
| &lt;     | Less than                  | x < y   |
| &gt;=    | Greater than or equal than | x >= y  |
| <=       | Less than or equal to      | x <= y  |

```python
"""
EX8: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""
```

## 📌 If...
- If este o declaratie/ un statement in cod prin care ghidam programul nostru sa execute o bucata de cod in functie de un criteriu/o conditie.
- Codul se executa doar daca conditia data la if este evaluata ca True/Adevarata.
- In engleza acest principiu se numeste ‘flow control’ - controlam pe unde curge codul.
- Un if simplu e ca o usa: daca usa e deschisa (true), se va executa codul din spate. Daca usa (conditia) e inchisa (false), python nu va afla ce e in spatele usii. Pentru Python, acea zona de cod e inaccesibila, nu exista.
- Cum definim un if?
```python
x = 5
if x == 5:
    print("x este egal cu 5") # indentare cod
```
 
- Dupa cele : ale unei ramuri, cand apasam ‘Enter’ se vor pune automat 4 spatii sau un TAB
- Acest lucru se numeste indentare. Indentarea are scopul de a-i transmite la python de unde pana unde tine blocul de cod corespunzator acelei conditii. (Sau altfel spus, marcheaza peretii camerei din spatele usii)

```python
nota_de_trecere = 4.5
nota = float(input('alege nota'))
if nota >= nota_de_trecere:
    print(f'Ai luat nota {nota}')
    print('Felicitari, ai trecut examenul!')
```

- E ok logica codului?

```python
"""
EX9: Verifica daca varsta introdusa de utilizator este mai mare
decat 18 ani.
"""
```

```python
"""
EX10: Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
"""
```


## 📌 If...else
- Daca conditia scrisa la if nu se indeplineste (este evaluata ca fiind False), vrem sa spunem programului ce sa faca.
- Are tot timpul fix 2 ramuri
- If are conditie urmata de :
- Else nu mai are nevoie de conditie.
- Ex: Un numar daca nu e par, e automat impar

```python
# constanta = are o valoare stabila, nu ne dorim sa o schimbe nimeni
# standardul este sa o scriem cu litere mari
NOTA_DE_TRECERE = 4.5
nota = float(input('Alege nota'))
if nota >= NOTA_DE_TRECERE:
    print(f'Ai luat nota {nota}')
    print('Felicitari ai trecut examenul')
else:
    print(f'Ai luat doar nota {nota}')
    print('Ne vedem la vara! Ai picat examenul')
```

```python
"""
EX11:
a. Citeste un numar de la tastatura.
b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
"""
```

```python
"""
EX12:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
"""
```

## 📌 If...else if ... else
- Se foloseste cand avem mai mult de 2 situatii posibile
- Conditiile se evalueaza de sus in jos
- Se executa codul aferent primei conditii adevarate
- Dupa ce s-a gasit un true, nu se mai verifica ce a mai ramas mai jos

```python
# robotelul telefonic
optiune = int(input('alege o optiune'))
if optiune == 0:
    print('meniul anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print('ati ales eng')
else:
    print('Nu am identificat optiunea, mai incearca.')
```

- Un singur if la inceput
- Oricate elif-uri sunt necesare
- Un singur else la final
- Daca nu gaseste nici un true mai sus, else se va executa automat (e ca un default)

```python
"""
EX13: Citeste de la tastatura varsta utilizatorului si afiseaza categoria
de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
"""
```

```python
"""
EX14: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
cosul de cumparaturi, in functie de totalul cosului de cumparaturi
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
dupa aplicarea reducerii.
"""
```


