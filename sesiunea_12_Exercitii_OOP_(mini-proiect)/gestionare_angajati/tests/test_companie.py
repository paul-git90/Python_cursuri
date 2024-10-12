"""
Acesta va conține testele pentru funcționalitatea companiei și angajaților.
"""


import unittest
from informatii_angajati.angajat import Angajat
from companie.companie import Companie
from departament.departament_hr import DepartamentHR


class TestCompanie(unittest.TestCase):
    def test_angajat(self):
        angajat = Angajat('Ion', 'Popescu', 5000)
        self.assertEqual(angajat.nume_complet(), 'Ion Popescu')
        self.assertEqual(angajat.salariu_anual(), 60000)

    def test_departament(self):
        departament_hr = DepartamentHR()
        angajat = Angajat('Ana', 'Ionescu', 4500)
        departament_hr.adauga_angajat(angajat)
        self.assertEqual(len(departament_hr.angajati), 1)

    def test_companie(self):
        companie = Companie("TechCorp")
        departament_hr = DepartamentHR()
        companie.adauga_departament(departament_hr)
        self.assertEqual(len(companie.departamente), 1)


if __name__ == '__main__':
    unittest.main()
