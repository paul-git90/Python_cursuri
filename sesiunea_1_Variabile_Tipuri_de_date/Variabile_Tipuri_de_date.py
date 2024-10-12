"""
Obiective Sesiune_1.1 - Fisiere Python, Variabile, Tipuri de date:
Sa avem toti setup functional
Sa intelegem cum functioneaza programarea
Primul program
Sa stim si sa putem explica altora ce e o variabila si de ce avem nevoie de ea
Sa intelegem cele mai uzuale tipuri de date
Sa intelegem ce este type casting si de ce e util
Sa intelegem cum functioneaza print statement
Sa stim cum luam date de la tastatura (user input)
Sa înțelegem cum punem comentarii in cod
"""
print('Hello Word') # primul nostru program

print("Info functia print()")
# print() =>> functia care ne ajuta sa afisam informatii in consola, este polimorfica pt ca poate primi diferite tipuri de argumente și nu da eroare, se comporta corespunzator
print('Hello Word')
print("Hello Word")
print("Mc'Donald")
print(10)
print(34.6)
print(True)
print("paste", "supa")
print("paste", "\n24")  #\n - il folosim cand vrem sa mergem pe randul urmator, asadar 24 va fi afisat pe randul urmator
print("paste", "supa", sep="?") # sep este un argument al functiei print() si ne ajuta sa separam cele 2 obiecte afisate in consola
# print("salata", end="") # end este un argument al functiei print() si ne ajuta sa specificam ce vrem sa afisam dupa ofictul afisat

#variabile = are nume unic, reprez adresa din memorie care stocheaza valori
clasa_mate_into = "a X-a B" # declaram si initializam variabila clasa
elev = "George"  # declaram si initializam variabila elev
fizica = mate = chimie = 9 # declaram si initializam variabilele fizica, mate, chimie one line si toate aceste variabile vor primi aceeasi valoare, care reprez nota primita
romana, istorie = 7, 8 # declaram si initializam variabilele romana si istorie one line separate prin virgula, iar  aceste variabile vor primi valoari diferite, care reprez nota primita
#CONSTANTE =  tot adrese din memorie, le folosim cand dorim sa pastram date si nu dorim sa facem modificari
PATH_DATABASE = "gradinite.db"  # folosim constanta atunci cand vrem sa salvam numele bazei de date

#TIPURI DE DATE = string, int, float, bool

#declaram si initializam variabile de tip string - sir de caractere
fast_food = "Mc'Donald"  # folosim ghilimele duble cand in cadrul stringului avem ghilimele simple si invers
produs = 'Big Mac'  # folosim ghilimele simple
bautura = "Fanta"  # folosim ghilimele duble

#declaram si initializam variabile de tip int - numar intreg
cantitate = 3
nr_angajati = 10

#declaram si initializam variabile de tip float - numar zecimal
pret_meniu = 14.5
gramaj_meniu = 1.25

#declaram si initializam variabile de tip bool - True sau False
program_weekend = False
deschis = True

#CONCATENAREA STRINGRURILOR = rerezinta unirea datelor de tip string
#important nu putem uni date de tip string cu date de tip int/ float sau bool
#varianta 1 = folosim semnul +
forma = "cerc"
culoare = "roz"
forma_geometrica = forma + culoare # in variabila forma_geometrica salvam datele rezultate din concatenarea celor 2 stringuri - datele din cele 2 variabile forma si culoare
print(forma + culoare)
print(forma_geometrica)
print("Detalii forma geometrica " + forma + culoare)

#varianta 2 = folosim f-string
print(f"detalii forma geometrica {forma} {culoare}")
print(f"detalii forma geometrica {forma, culoare}")
print(f"detalii forma geometrica {forma + culoare}")

diametru = 16
#print("Diametrul cercului este de " + diametru)# va da eroare pt ca avem date diferite
print(f"Diametrul cercului este de {diametru}")
print("Diametrul cercului este de ", diametru)
print(f"Avem un {forma} de culoare {culoare} cu diametrul {diametru}cm. ")


print("Info functia type()")
#type() =>> functia care ne ajuta sa stim ce tipul de date salvat in variabila
anotimp = "vara" #declaram si initializam variabila anotimp in care salvam date de tip string
print(type(anotimp)) # ne folosim de functia type() pentru a afla tipul de date salvat in variabila anotimp si afisam mesajul cu ajutorul functiei print()

print("Info type casting")
#type casting =>> ne ajuta sa convertim datele
# type casting =>> convertim date de tip int in date de tip string  =>> ne folosim de functia int()
lungime1 = 15
lungime2 = "15"
#verificam tipul de date cu ajutorul functiei type() si afisam rezultatul cu ajutorul functiei print()
print(type(lungime1)) #avem date de tip int =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
print(type(lungime2)) # avem date de tip string =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
lungime2 = int(lungime2) # am suprascris datele in variabila lungime2, acum avem date de tip int deoarece am facut un typecasting cu ajutorul functiei int()
print(type(lungime2)) # avem date de tip int

# type casting  =>> convertim date de tip string in date de tip int =>> ne folosim de functia int()
varsta1 = 20
varsta2 = "20"
#verificam tipul de date cu ajutorul functiei type() si afisam rezultatul cu ajutorul functiei print()
print(type(varsta1)) #avem date de tip int =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
print(type(varsta2)) # avem date de tip string =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
varsta1 = str(varsta1) # am suprascris datele in varsta1, acum avem date de tip string deoarece am facut un typecasting cu ajutorul functiei str()
print(type(varsta1)) # avem date de tip string

# type casting  =>> convertim date de tip int in date de tip float =>> ne folosim de functia float()
pret1 = 10
#verificam tipul de date cu ajutorul functiei type() si afisam rezultatul cu ajutorul functiei print()
print(type(pret1)) #avem date de tip int =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
pret1 = float(pret1) # am suprascris datele in pret1, acum avem date de tip float deoarece am facut un typecasting cu ajutorul functiei float()
print(type(pret1)) # avem date de tip float

# type casting  =>> convertim date de tip float in date de tip int =>> ne folosim de functia int()
pret2 = 10.0
#verificam tipul de date cu ajutorul functiei type() si afisam rezultatul cu ajutorul functiei print()
print(type(pret2)) #avem date de tip int =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
pret2 = int(pret2) # am suprascris datele in pret2, acum avem date de tip int deoarece am facut un typecasting cu ajutorul functiei int()
print(type(pret2)) # avem date de tip int

# type casting  =>> convertim date de tip int in date de tip bool =>> ne folosim de functia bool()
open1 = 1
open2 = 0
#verificam tipul de date cu ajutorul functiei type() si afisam rezultatul cu ajutorul functiei print()
print(type(open1))  #avem date de tip int =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
print(type(open2))  #avem date de tip int =>>  verificam acest lucru cu ajutorul functiei type() si afisam mesajul cu ajutorul functiei print()
open1 = bool(open1)  # am suprascris datele in open1, acum avem date de tip int deoarece am facut un typecasting cu ajutorul functiei bool()
print(type(open1))  # avem date de tip bool
print(open1)  # afisam cu ajutorul functiei print() datele din variabila open1
open2 = bool(open2) # am suprascris datele in open2, acum avem date de tip int deoarece am facut un typecasting cu ajutorul functiei bool()
print(type(open2))  # avem date de tip bool
print(open2)  # afisam cu ajutorul functiei print() datele din variabila open2


print("Info functia input()")
#input() =>> functia care ne ajuta sa preluam date de la tastura/de la utilizator
#datele preluate default sunt date de tip string
vanzator = input("Cum te numesti? ")
tip_imobil = input("Ce tip de imobil vrei sa vinzi? ")  # in variabila tip_imobil salvam datele preluate de la tastatura cu ajutorul functiei input(), aceste date vor fi de tip string
pret_vanzare = int(input("Care este pretul de vanzare? \n"))  # in variabila pret_vanzare salvam datele preluate de la tastatura cu ajutorul functiei input(), iar cu ajutorul functiei int() facem un type casting - modificam datele de tip string in date de tip int

print(f'{vanzator} are de vanzare un imobil de tip: {tip_imobil} si are pretul de vanzare {pret_vanzare} euro negociabil')



