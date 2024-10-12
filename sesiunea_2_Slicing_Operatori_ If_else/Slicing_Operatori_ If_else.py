# """
# Obiective Sesiunea_2.1_Slicing, Operatori,String methods si Structura Alternativa IF:
# Sa înțelegeți ce este string slicing și cum se face
# Sa știm sa lucram cu String methods
# Să știm care sunt operatorii principali și prioritatea lor
# Sa înțelegem cum funcționează structura alternativa if
# """
#
# #String slicing - sintexa este: string[start:stop:step]
print("Exemple: String slicing", end=" \n \n")

oras = "Cluj-Napoca, Oradea, Timisoara, Constanta, Iasi"
print(oras[0:4]) #Extrage primele 4 caractere: Cluj
print(oras[5:11]) #Extrage caracterele de la poziția 5 la 11: Napoca
print(oras[:4]) #Extrage primele 4 caractere (omiterea poziției de start): Cluj
print(oras[5:]) #Extrage ultimele caractere incepand de la pozitia 5 (omiterea poziției de final): Napoca
print(oras[::2]) #Extrage fiecare al doilea caracter din string: Cu-aoa, pasul este 2
print(oras[0:11:2]) #Extrage fiecare al doilea caracter din string: Cu-aoa, pasul este 2
print(oras[::-2]) #inverseaza întregul ștring, pasul este -2
print(oras[::-1]) #inverseaza întregul ștring, pasul este -1
print()
#String methods - pot fi accesate folosind carac '.' imediat dupa stringul nostru
print("Exemple: String methods")
judet = "constanta, Tulcea, iasi"
lungime_string = len(judet) # in variabila lungime_string salvam lunimea stringului judet pe care o aflam cu ajutorul functiei len()

# r = judet.replace("a","A",2)
# print(r)
print(judet.replace("t", "T", 2)) #functia care ne face inlocuirea carac dat cu noul caracter
print(judet.upper()) #functia care modifica toate caracterele din string cu litera mare
print(judet.lower()) #functia care modifica toate caracterele din string cu litera mic
print(judet.split(",")) #functia care imparte stringul in functie de caracterul dat
print(judet.index("T")) #functia care ne spune indexul caracterul dat
print(judet.islower()) #functia care ne spune daca caracterele din string sunt scrise cu litera mica
print(judet.capitalize()) #functia care modifica primul caracter din string, va fi litera mare
print(judet.count("a")) #functia care ne spune de cate ori gaseste caracterul a in stringul nostru

print()
#Operatori aritmetici - sunt folositi pentru operatii aritmetice
print("Exemple: Operatori atitmetici")
salar = 4000
x = 20
r = salar + x
print(r)
print(salar + x) # "+" pt operatii de adunare
print(salar - x) # "-" pt operatii de scadere
print(salar * x) # "*" pt operatii de inmultire
print(salar / x) # "/" pt operatii de impartire
print(salar % x) # "%" modulo pt operatii de impartire, ne retuneaza restul
print(salar ** 2) # "**" pt a ridica la putere
print(salar // 3) # "//" pt operatii de impartire si apoi taie zecimalele


print()
#Operatori de atribuire - sunt folositi pentru a aloca unui variabile o valoare
print("Exemple: Operatori atribuire")
salar = 4000
print(salar)
print("'+=' >> operator aritmetic: '+' si operatorul de atribuire '=' ")
salar += 1 #sau salar = salar + 1
print(salar)
print("'-=' >> operator aritmetic: '-' si operatorul de atribuire '=' ")
salar =- 1 #sau salar = salar - 1
print(salar)

print("'*=' >> operator aritmetic: '*' si operatorul de atribuire '=' ")
salar *= 2 #sau salar = salar * 2
print(salar)

print("'/=' >> operator aritmetic: '/' si operatorul de atribuire '=' ")
salar /= 2 #sau salar = salar / 2
print(salar)

print("'**=' >> operator aritmetic: '**' si operatorul de atribuire '=' ")
salar **= 2 #sau salar = salar ** 2
print(salar)

print()
#Operatori de comparare - sunt folositi pentru a evalua egalitatea dintre 2 valori, se gasesc in cicluri repetitive
print("Exemple: Operatori de comparare")
a = 100
b = 50
print(a == b) # retuneaza date de tip bool, verifica daca a este egal cu b
print(a != b) # retuneaza date de tip bool, verifica daca a este diferit de b
print(a <= b) # retuneaza date de tip bool, verifica daca a este mai mic sau egal cu b
print(a >= b) # retuneaza date de tip bool, verifica daca a este mai mare sau egal cu b
print(a < b) # retuneaza date de tip bool, verifica daca a este mai mic decat b
print(a > b) # retuneaza date de tip bool, verifica daca a este mai mare decat b


print()
#Operatori logici - sunt folositi pentru a crea conditii compuse
print("Exemple: Operatori logici")
angajat = True
salariu = 4000
an_nastere = 1995

print(angajat == True) #conditie simpla
print(angajat == True and salariu > 5000)
print(an_nastere > 2060 or angajat == False)
print(not(angajat == True))
print(not angajat)# instructiunea asta este varianta mai scurta a celei anterioare


print()
#Structura if
print("Exemple: Structura alternativa if - else")

x = 3
y = 3
if x > y:
 print(f"Numarul {x} este mai mare decat numarul {y}")
elif y > x:
 print(f"Numarul {y} este mai mare decat numarul {x}")
else:
 print("Numerele sunt egale")

print("Exemple: Structura alternativa if - else")