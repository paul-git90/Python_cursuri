"""
Acesta va fi punctul de intrare în aplicație și va crea obiectele necesare
pentru companie, departamente și angajați.
"""


from companie.companie import Companie
from departament.departament_hr import DepartamentHR
from informatii_angajati.angajat import Angajat
from informatii_angajati.manager import Manager

# Creăm compania
companie = Companie("TechCorp")

# Creăm departamente
departament_hr = DepartamentHR()

# Creăm angajați
angajat1 = Angajat("Ion", "Popescu", 5000)
angajat2 = Angajat("Ana", "Ionescu", 4500)

# Creăm manager
manager = Manager("George", "Vasilescu", 7000, [angajat1, angajat2])

# Adăugăm angajați în departament
departament_hr.adauga_angajat(angajat1)
departament_hr.adauga_angajat(angajat2)

# Adăugăm manager
departament_hr.adauga_angajat(manager)

# Adăugăm departamentul în companie
companie.adauga_departament(departament_hr)

# Afișăm informații
companie.descriere()
departament_hr.afiseaza_angajati()
