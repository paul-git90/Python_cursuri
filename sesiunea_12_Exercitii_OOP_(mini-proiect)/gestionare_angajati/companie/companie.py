"""
Acesta va gestiona funcționalitățile legate de companie (angajați, departamente, etc).
"""


class Companie:
    def __init__(self, nume):
        self.nume = nume
        self.departamente = []

    def adauga_departament(self, departament):
        self.departamente.append(departament)

    def descriere(self):
        print(f"Compania {self.nume} are următoarele departamente:")
        for dep in self.departamente:
            print(f"- {dep.nume_departament}")
