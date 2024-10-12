"""
Acesta este un modul de bază pentru departamente.
"""


class Departament:
    def __init__(self, nume_departament):
        self.nume_departament = nume_departament
        self.angajati = []

    def adauga_angajat(self, angajat):
        self.angajati.append(angajat)

    def afiseaza_angajati(self):
        for angajat in self.angajati:
            angajat.descrie()
