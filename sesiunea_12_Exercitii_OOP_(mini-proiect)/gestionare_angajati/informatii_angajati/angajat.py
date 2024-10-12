"""
Acesta va conține clasa Angajat, care extinde clasa Persoana.
"""


from informatii_angajati.persoana import Persoana


class Angajat(Persoana):
    def __init__(self, nume, prenume, salariu):
        super().__init__(nume, prenume)
        self.__salariu = salariu

    def descrie(self):
        print(f"Angajat: {self.nume_complet()}, Salariu: {self.__salariu}")

    def salariu_lunar(self):
        return self.__salariu

    def salariu_anual(self):
        return self.__salariu * 12

    def marire_salariu(self, procent):
        self.__salariu += self.__salariu * procent / 100
