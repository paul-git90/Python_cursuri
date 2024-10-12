import csv
import json

"""
Exercitii cu trainer sesiunea 15: Pachete python. Fisiere.
"""

# todo Exercițiul 1: Citirea unui fișier CSV și afișarea ca tabel

"""
Exercițiul 1: Citirea unui fișier CSV și afișarea ca tabel
Cerință:
Trebuie să creăm un fișier CSV numit students.csv, să adăugăm informațiile date și să le citim 
folosind biblioteca standard csv. Apoi trebuie să le afișăm într-un format tabelar.

Explicație:
Fișierele CSV (Comma Separated Values) sunt fișiere text ce conțin date separate prin virgule. 
Biblioteca csv din Python permite manipularea ușoară a acestor tipuri de fișiere.

Pași:
Creare fișier CSV: Vom crea un fișier CSV și vom scrie datele în el.
Citirea fișierului CSV: Vom citi fișierul folosind csv.reader() și vom afișa datele într-un format tabelar.
"""

# import csv

# 1. Creăm fișierul CSV și adăugăm datele
with open("students.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "fname", "lname", "age", "grade"])
    writer.writerow([1, "Maria", "Popescu", 31, 7.5])
    writer.writerow([2, "Andrei", "Ionescu", 26, 8.0])
    writer.writerow([3, "Adriana", "Marinescu", 21, 7.5])
    writer.writerow([4, "Matei", "Gheorghescu", 42, 8.5])
    writer.writerow([5, "Eusebiu", "Pop", 33, 9.5])
    writer.writerow([6, "Ioana", "Popa", 29, 9.0])

# 2. Citim fișierul CSV și afișăm conținutul într-un format tabelar
with open("students.csv", mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Citim header-ul
    print(f"{'id':<4}{'fname':<12}{'lname':<15}{'age':<5}{'grade':<5}")
    print("-" * 50)

    for row in reader:
        print(f"{row[0]:<4}{row[1]:<12}{row[2]:<15}{row[3]:<5}{row[4]:<5}")

"""
Explicație logica:
csv.writer(): Permite scrierea rândurilor în fișierul CSV.
Formatarea: Folosim string formatting pentru a alinia textul în coloane.
"""

# todo Exercițiul 2: Conversia CSV în JSON

"""
Cerință:
Citirea fișierului CSV din Exercițiul 1 și scrierea unui nou fișier JSON numit students.json.

Explicație:
CSV este un format tabular, iar JSON este un format ce folosește perechi cheie-valoare, deci fiecare rând din CSV 
va deveni un obiect în format JSON.
Vom folosi biblioteca standard json pentru a crea un fișier JSON din datele citite din CSV.
"""

# import csv
# import json

# 1. Citim datele din fișierul CSV și le stocăm într-o listă de dicționare
students = []
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "id": int(row["id"]),
            "fname": row["fname"],
            "lname": row["lname"],
            "age": int(row["age"]),
            "grade": float(row["grade"])
        })

# 2. Scriem lista de dicționare într-un fișier JSON
with open("students.json", mode="w") as json_file:
    json.dump(students, json_file, indent=4)

"""
Explicație logică:
csv.DictReader(): Citim CSV-ul sub forma unei liste de dicționare.
json.dump(): Scriem lista de dicționare într-un fișier JSON.
"""

# todo Exercițiul 3: Crearea unei clase Student și gestionarea fișierului JSON

"""
Cerință:
Crearea unei clase Student, citirea datelor din fișierul JSON și adăugarea de noi obiecte Student. Scrierea acestor 
obiecte într-un nou fișier JSON.

Explicație:
O clasă Student reprezintă un model pentru datele din fișierul JSON.
Vom crea obiecte Student din datele citite din JSON, vom adăuga noi obiecte și apoi vom scrie totul într-un alt 
fișier JSON.
"""

# import json


# Definim clasa Student
class Student:
    def __init__(self, id, fname, lname, age, grade):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "age": self.age,
            "grade": self.grade
        }


# 1. Citim datele din fișierul JSON
with open("students.json", "r") as file:
    data = json.load(file)

# 2. Creăm o listă de obiecte Student
students = [Student(**student) for student in data]

# 3. Adăugăm noi obiecte Student
students.append(Student(7, "John", "Doe", 30, 8.7))
students.append(Student(8, "Jane", "Doe", 28, 9.1))

# 4. Scriem lista de obiecte Student într-un nou fișier JSON
with open("students_updated.json", "w") as file:
    json.dump([student.to_dict() for student in students], file, indent=4)

"""
Explicație logică:
Clasa Student: Modelăm un student și oferim o metodă to_dict pentru conversie în dicționar.
Citire și scriere JSON: Citim din fișierul JSON, creăm obiecte Student și adăugăm noi obiecte 
înainte de a rescrie fișierul JSON.
"""

# todo Exercițiul 4: Proiect PyCharm și gestionarea unui mediu virtual

"""
Cerință:
Crearea unui nou proiect PyCharm, configurarea unui mediu virtual, instalarea pachetelor din PYPI și verificarea 
instalării lor.

Explicație:
Crearea unui mediu virtual permite izolarea dependențelor proiectului față de restul sistemului.
Fișierul requirements.txt ajută la gestionarea pachetelor necesare.
Pași:
Creăm un nou proiect și un mediu virtual folosind venv.
Instalăm pachetele menționate și generăm fișierul requirements.txt.
"""

# todo bash Terminal

# Crearea unui mediu virtual

# python -m venv venv

# Activarea mediului virtual

# source venv/bin/activate  # (pentru Linux/MacOS)

# venv\Scripts\activate  # (pentru Windows)

# Instalarea pachetelor

# pip install behave behave-html-formatter requests selenium webdriver-manager

# Generarea fișierului requirements.txt

# pip freeze > requirements.txt


# todo test

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Test simplu: Introducem text și trimitem formularul
text_box = driver.find_element("name", "my-text")
text_box.send_keys("Selenium")
submit_button = driver.find_element("tag name", "button")
submit_button.click()

driver.quit()

"""
Acest exercițiu implică dezvoltarea individuală a unui mini-proiect și colaborarea în echipă pentru a compara soluțiile. 
Proiectele trebuie încărcate pe GitHub, unde fiecare membru poate revizui și testa soluțiile celorlalți.
"""