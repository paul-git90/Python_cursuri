"""
Acest modul este specific pentru departamentul de vânzări.
"""


from departament.departament import Departament


class DepartamentVanzari(Departament):
    def __init__(self):
        super().__init__('Vânzări')
