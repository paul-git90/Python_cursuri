"""
Reprezentare exemplu OOP sub forma unei schite detaliat explicate
"""


# Definim o clasa "Masina" - Aceasta este clasa noastra, un șablon pentru crearea obiectelor
class Masina:

    # Constructorul __init__ este folosit pentru a inițializa atributele unui obiect atunci când este creat
    def __init__(self, marca, model, anul_fabricatiei):
        # Atribute - Acestea sunt date care aparțin fiecărei instanțe a clasei
        self.marca = marca
        self.model = model
        self.anul_fabricatiei = anul_fabricatiei
        self.viteza = 0  # Un atribut implicit, viteza e setată inițial la 0

    # O metodă pentru a accelera masina (aceasta e o funcție a clasei)
    def accelereaza(self, valoare):
        self.viteza += valoare  # Crește viteza mașinii cu valoarea dată
        print(f"{self.marca} {self.model} accelereaza cu {valoare} km/h. Viteza curenta: {self.viteza} km/h")

    # O metodă pentru a opri masina
    def opreste(self):
        self.viteza = 0  # Setează viteza la 0
        print(f"{self.marca} {self.model} s-a oprit. Viteza curenta: {self.viteza} km/h")


# Creăm o instanță a clasei Masina - acesta este un obiect numit "masina_mea"
masina_mea = Masina("Dacia", "Duster", 2022)

# Folosim metodele pe obiect
masina_mea.accelereaza(50)  # Accelerează mașina cu 50 km/h
masina_mea.opreste()  # Oprește mașina

# Creăm o altă instanță a clasei Masina
alta_masina = Masina("Tesla", "Model 3", 2023)

# Aceasta mașină accelerează independent
alta_masina.accelereaza(100)


"""
Explicația fiecărui element:
Clasa (class):

Clasa Masina este un șablon care definește structura și comportamentul obiectelor de tip „mașină”.
Cuvântul cheie class este utilizat pentru a defini o clasă.
Constructorul (__init__):

Metoda specială __init__ este constructorul clasei. Ea este apelată automat de fiecare dată când o nouă instanță a 
clasei este creată.
Parametrii marca, model, anul_fabricatiei sunt transmiși constructorului pentru a inițializa atributele instanței.
Atributele (self.marca, self.model, self.anul_fabricatiei, self.viteza):

Acestea sunt variabile care aparțin fiecărei instanțe a clasei. În cazul nostru, atributele sunt marca, model, 
anul_fabricatiei, și viteza.
self este o referință la instanța curentă a clasei și este folosit pentru a accesa atributele și metodele.
Metodele (accelereaza, opreste):

Acestea sunt funcții care definesc comportamentul unei clase. Metoda accelereaza modifică atributul viteza, iar metoda 
opreste setează viteza la 0.
Instanța (Obiectul):

Instanța este un obiect specific creat dintr-o clasă. În codul nostru, masina_mea și alta_masina sunt două instanțe ale 
clasei Masina.
Fiecare instanță își păstrează propriile atribute și poate apela metodele definite în clasă.
self:

self este o referință la instanța curentă a clasei și trebuie inclus ca prim argument în toate metodele unei clase.
Este folosit pentru a accesa și modifica atributele și metodele instanței.

Clasa        : Masina
Atribute     : self.marca, self.model, self.anul_fabricatiei, self.viteza
Metode       : accelereaza(self, valoare), opreste(self)
Constructor  : __init__(self, marca, model, anul_fabricatiei)
Instante     : masina_mea, alta_masina
self         : Referință la instanța curentă (ex. masina_mea sau alta_masina)
"""
