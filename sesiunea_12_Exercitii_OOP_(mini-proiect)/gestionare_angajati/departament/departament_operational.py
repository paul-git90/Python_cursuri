"""
Acest modul este specific pentru departamentul operațional.
"""


from departament.departament import Departament


class DepartamentOperational(Departament):
    def __init__(self):
        super().__init__('Operațional')
