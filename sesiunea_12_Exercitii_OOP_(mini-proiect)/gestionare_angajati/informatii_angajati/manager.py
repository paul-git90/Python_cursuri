"""
Acesta va conține clasa Manager, care extinde clasa Angajat.
"""


from informatii_angajati.angajat import Angajat


class Manager(Angajat):
    def __init__(self, nume, prenume, salariu, echipa=[]):
        super().__init__(nume, prenume, salariu)
        self.echipa = echipa

    def descrie(self):
        super().descrie()
        print(f"Managerul are {len(self.echipa)} angajați în echipă.")
