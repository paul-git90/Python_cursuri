"""
OOP

Implementati urmatoarele clase, folosind notiuni OOP

1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
●	descrie_cerc() - va PRINTA culoarea și raza
●	aria() - va RETURNA aria
●	diametru()
●	circumferinta()

2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
●	descrie()
●	aria()
●	perimetrul()
●	schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va
suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza de {self.raza} și culoarea {self.culoare}")

    def aria(self):
        # Formula ariei cercului: A = pi * r^2
        return 3.14 * (self.raza ** 2)

    def diametru(self):
        # Formula diametrului: D = 2 * r
        return 2 * self.raza

    def circumferinta(self):
        # Formula circumferinței: C = 2 * pi * r
        return 2 * 3.14 * self.raza


# Exemplu de utilizare:
cerc1 = Cerc(5, "roșu")
cerc1.descrie_cerc()
print(f"Aria cercului: {cerc1.aria()}")
print(f"Diametrul cercului: {cerc1.diametru()}")
print(f"Circumferința cercului: {cerc1.circumferinta()}")


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, lățimea de {self.latime}, și culoarea {self.culoare}")

    def aria(self):
        # Formula ariei dreptunghiului: A = lungime * latime
        return self.lungime * self.latime

    def perimetrul(self):
        # Formula perimetrului dreptunghiului: P = 2 * (lungime + latime)
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        # Schimbă culoarea dreptunghiului
        self.culoare = noua_culoare


# Exemplu de utilizare:
dreptunghi1 = Dreptunghi(10, 5, "albastru")
dreptunghi1.descrie()
print(f"Aria dreptunghiului: {dreptunghi1.aria()}")
print(f"Perimetrul dreptunghiului: {dreptunghi1.perimetrul()}")

# Schimbăm culoarea dreptunghiului și verificăm modificarea
dreptunghi1.schimba_culoarea("verde")
dreptunghi1.descrie()
