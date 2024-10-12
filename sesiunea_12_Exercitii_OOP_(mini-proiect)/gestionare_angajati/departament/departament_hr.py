"""
Acest modul este specific pentru departamentul de resurse umane.
"""


from departament.departament import Departament


class DepartamentHR(Departament):
    def __init__(self):
        super().__init__('Resurse Umane')
