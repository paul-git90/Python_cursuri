from abc import ABC, abstractmethod

# ABSTRACTION
# Clasa abstractă FormaGeometrica


class FormaGeometrica(ABC):
    PI = 3.14  # Constanta PI

    @abstractmethod
    def aria(self):
        """Metoda abstractă pentru calcularea ariei"""
        pass

    @classmethod
    def descrie(cls):
        """Descriere generală a formelor geometrice"""
        print("Cel mai probabil am colturi")


# INHERITANCE
# Clasa Pătrat moștenește FormaGeometrica
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        # ENCAPSULATION
        # Latura este un atribut privat
        self.__latura = latura

    # ENCAPSULATION - Getters, Setters, Deleters
    @property
    def latura(self):
        """Getter pentru latură"""
        return self.__latura

    @latura.setter
    def latura(self, latura):
        """Setter pentru latură"""
        self.__latura = latura

    @latura.deleter
    def latura(self):
        """Deleter pentru latură"""
        del self.__latura

    # Implementarea metodei abstracte aria
    def aria(self):
        """Calcularea ariei pătratului"""
        return self.__latura ** 2

    def descrie(self):
        """Descriere specifică pentru pătrat"""
        print(f"Eu sunt un pătrat cu latura de {self.__latura}.")


# Clasa Cerc moștenește FormaGeometrica
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        # ENCAPSULATION
        # Raza este un atribut privat
        self.__raza = raza

    # ENCAPSULATION - Getters, Setters, Deleters
    @property
    def raza(self):
        """Getter pentru rază"""
        return self.__raza

    @raza.setter
    def raza(self, raza):
        """Setter pentru rază"""
        self.__raza = raza

    @raza.deleter
    def raza(self):
        """Deleter pentru rază"""
        del self.__raza

    # Implementarea metodei abstracte aria
    def aria(self):
        """Calcularea ariei cercului"""
        return self.PI * (self.__raza ** 2)

    # POLYMORPHISM
    def descrie(self):
        """Descriere specifică pentru cerc"""
        print("Eu nu am colturi")


# EXEMPLIFICARE OOP:

# Crearea unui obiect de tip Patrat
print("===== Obiect Patrat =====")
patrat = Patrat(4)

# Folosirea getter-ului
print(f"Latura pătratului: {patrat.latura}")

# Calcularea ariei pătratului
print(f"Aria pătratului: {patrat.aria()}")

# Folosirea setter-ului pentru a schimba latura
patrat.latura = 5
print(f"Noua latură a pătratului: {patrat.latura}")
print(f"Noua arie a pătratului: {patrat.aria()}")

# Folosirea metodei descrie (polimorfism)
patrat.descrie()

# Folosirea deleter-ului
del patrat.latura
# print(patrat.latura)  # Aceasta linie ar da eroare deoarece latura a fost ștearsă


# Crearea unui obiect de tip Cerc
print("\n===== Obiect Cerc =====")
cerc = Cerc(3)

# Folosirea getter-ului
print(f"Raza cercului: {cerc.raza}")

# Calcularea ariei cercului
print(f"Aria cercului: {cerc.aria()}")

# Folosirea setter-ului pentru a schimba raza
cerc.raza = 4
print(f"Noua rază a cercului: {cerc.raza}")
print(f"Noua arie a cercului: {cerc.aria()}")

# Folosirea metodei descrie (polimorfism)
cerc.descrie()

# Folosirea deleter-ului
del cerc.raza
# print(cerc.raza)  # Aceasta linie ar da eroare deoarece raza a fost ștearsă

# POLYMORPHISM in action
print("\n===== Polimorfism =====")
forme = [Patrat(6), Cerc(7)]

for forma in forme:
    forma.descrie()
