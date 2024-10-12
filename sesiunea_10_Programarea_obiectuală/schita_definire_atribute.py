"""
Exemple de modele si situatii diferite de definire a atributelor in clasa
si analiza de posibilitati in manipularea atributelor si metodelor
"""


# fara a folosi un constructor

class Car:
    # definim atributele/fild-urile clasei
    make = "Dacia"
    model = None
    year = 2022
    color = None

    # definim metode
    def accelerate(self):
        print("Vruum!")

    def __str__(self):  # metoda pentru a afisa in output atributele, altfel primeam output cu adresa memoriei stocate
        return (f"Car(make={self.make}, model={self.model}, year={self.year}, color={self.color})"
                f"\nMasina: {self.make}, {self.model}, {self.year}, {self.color}\n")

    def __repr__(self):  # metoda pentru a afisa in output atributele, altfel primeam output cu adresa memoriei stocate
        return f"Car(make={self.make}, model={self.model}, year={self.year}, color={self.color})"


car1 = Car()  # inițializăm obiectul de tip Car
car2 = Car()  # car2 este o altă instanță a clasei

# avem acces la atribute și metode, le definim aici separat deoarece nu avem constructor, apoi vom folosi print
car1.model = "BYD"  # putem suprascrie valori
car1.year = 2024
car1.color = "red"

car2.make = "Tesla"
car2.year = 2025
car2.color = "alb"

print(car1, car2)  # __repr__() este folosit pentru a furniza o reprezentare „oficială” a obiectului, o lista
# De obicei pentru debugging.
# Dacă nu implementezi __str__() Python va folosi implicit __repr__() atunci când încerci să afișezi obiectul.

car1.accelerate()
car2.accelerate()

print("\n")

# alta metoda de afisare, output prin apelare atribute
print(f"Masina 1: {car1.make}, {car1.model}, {car1.year}, {car1.color}")
print(f"Masina 2: {car2.make}, {car2.model}, {car2.year}, {car2.color}")

print("\n")

cars = [car1, car2]  # testare pentru repr care este util pentru debugging
print(cars)

print("\nfin exemplul nr. 1\n")

# folosim constructor


class Car2:
    # Atribute ale clasei (împărtășite de toate instanțele)
    # make = "Dacia"  # nu mai este necesar sa definim aici atributele, ele vor fi in constructor
    # year = 2022

    # Constructorul __init__ pentru a inițializa atributele de instanță
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model  # Atributul de instanță 'model'
        self.year = year
        self.color = color  # Atributul de instanță 'color'

    # Metoda pentru a accelera masina
    def accelerate(self):
        print("Vruum ppppmmm!")

    def parcare_automata(self):
        print("Am parcat!")


car1 = Car2("Duster", "Maro", 2019, "Albastru")  # acum atributele sunt completate cu parametrii
car3 = Car2("Sandero", "Rosu", 2020, "Negru")  # intr-o singura linie de cod

print(car1)  # nu avem definit metoda specială __str__() sau __repr__() astfel primim la output adresa memoriei
print(car3)

print(f"Masina 1: {car1.make}, {car1.model}, {car1.year}, {car1.color}")
print(f"Masina 3: {car3.make}, {car3.model}, {car3.year}, {car3.color}")

cars = [car1, car3]  # nu afișează decat adresa memoriei deoarece nu avem function special __repr__
print(cars)

car1.accelerate()
car3.accelerate()

car1.parcare_automata()
car3.parcare_automata()

car2.parcare_automata()  # instanta car2 nu are metoda .parcare_automata() definita in clasa Car, astfel avem eroare
