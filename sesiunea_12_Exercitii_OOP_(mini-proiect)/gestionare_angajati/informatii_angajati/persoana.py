"""
Acesta va reprezenta clasa de bază pentru o persoană.
"""


class Persoana:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"
