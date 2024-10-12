# Sesiunea 14: Interactiunea cu fisiere, JSON, Python Packages
## 📝 OBIECTIVE
- Interactiunea cu fisiere: citire, scriere in fisiere
- Manipulare fisiere txt, json, csv
- JSON
- Python Packages
- Virtual environments 

## 📌 Interactiunea cu fisiere

###  🔷 Deschiderea fisierului - functia open()
- functie folosita pentru a deschide un fisier
- cand apelam functia open, putem specifica valori pentru mai multi parametri
  - parametru obligatoriu: file (calea catre fisierul cu care dorim sa interactionam, sub forma de string)
  - parametri optionali: mode, encoding etc.
- ne returneaza un obiect (un file handler), prin care
putem interactiona cu fisierul deschis (citire, scriere etc.)

#### 🔹 Parametrul mode
- string care reprezinta modul in care dorim sa deschidem fisierul
- 3 moduri principale in care putem deschide un fisier:
  - "r" - read mode -> il folosim cand dorim sa deschidem un fisier pentru a citi informatiile
  din acesta
  - "w" - write mode -> il folosim cand dorim sa scriem informatii intr-un fisier
    - daca fisierul nu exista, aceasta se va crea
    - daca fisierul exista, indiferent daca acesta are continut, continutul va fi suprascris cu
    noile informatii
  - "a" - append mode -> il folosim cand dorim sa scriem informatii intr-un fisier
    - daca fisierul nu exista, aceasta se va crea
    - daca fisierul exista si are continut, noile informatii vor fi adaugate la final

### 🔷 Inchiderea fisierului - metoda close()
- Dupa ce am terminat de interactionat cu un fisier,
acesta trebuie inchis, apeland metoda close() pe obiectul
returnat de functia open()


## 📌 Interactiunea cu fisiere txt

```python
# crearea unui fisier txt
fisier_nou = open(file="fisiere/dummy.txt", mode="w")

# adaugare continut in fisierul text deschis in write-mode
fisier_nou.write("hello")
fisier_nou.write("hello\nworld\n")

fisier_nou.writelines(["hello\n", "again\n"])

# inchidem fisierul
fisier_nou.close()
```
- Daca uitam sa apelam functia close() pentru a inchide fisierul,
acesta va ramane deschis, si astfel datele vor fii vulnerabile
- Pentru a nu avea aceasta problema si pentru ca inchiderea
fisierului sa se faca in mod automat, ne putem folosi de
un with statement.
```python
def scriere_in_fisier_txt(calea_fisier, informatii_as_list):
    with open(calea_fisier, mode="w") as file:
        file.writelines(informatii_as_list)
```

```python
def citire_din_fisier_txt(calea_catre_fisier_txt):
    with open(calea_catre_fisier_txt, 'r') as file:
        return file.readlines()

citire_din_fisier_txt("dummy.txt")
citire_din_fisier_txt("fisiere_text/dogs.txt")

# TODO: exploreaza si alte metode de citire disponibile

# TODO: Ce se intampla daca deschidem un fisier in modul read,
# si scriem informatii in acesta?

# TODO: Exploreaza si modul de deschidere append (mode="a")
```

## 📌 JSON
- JSON = Javascript Object Notation
- Este un format tip text pentru stocare si transportare de date
- El este independent de orice limbaj de programare, toate il folosesc
- Suporta tipurile de date uzuale (str, int, float, list, dict)
- Arata si se comporta in cele mai multe cazuri ca un dictionar/lista

## 📌 Interactiunea cu fisiere JSON
```python
import json

def citire_din_fisier_json(cale_fisier):
    with open(cale_fisier, 'r') as file:
        return json.load(file)

print(citire_din_fisier_json("quiz.json"))
print(type(citire_din_fisier_json("quiz.json")))
```

```python
import json

def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    with open(cale_fisier, 'w') as file:
        json.dump(randuri_informatii, file)
```

## 📌 Interactiunea cu fisiere csv
- CSV = Coma Separated Values
- Fisierele CSV sunt fisiere structurate sub forma tabelara
  (excel), unde valorile coloanelor sunt separate prin virgula.

```python
import csv

with open("csv/path_to_csv_file.csv", "w") as file:
  writer = csv.writer(file)

  writer.writerow(['id', 'nume'])  # cream header-ul
  writer.writerow([1, 'Paula'])
  writer.writerow([2, 'Ana'])
```

```python
import csv

with open("csv/path_to_csv_file.csv", "r") as file:
  reader = csv.reader(file)

  # read a row at a time
  row = next(reader)

  # read the next rows using a for loop
  for row in reader:
    print(row)
```

```python
import csv

with open('csv/path_to_csv_file.csv', 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row)
```

```python
# EXERCITII BONUS FISIERE

"""
EX1:
1. Copierea continutului dintr-un fisier in alt fisier.
- creeaza un fisier sursa.txt (din cod) si pune continut in el
(continutul e la alegerea ta)
- copiaza continutul din fisierul sursa.txt intr-un fisier nou,
numit destinatie.txt.
Afiseaza apoi contintul din fisierul destinatie.txt
"""

"""
EX2: Numararea cuvintelor
- creeaza o functie care sa ia ca si parametru un cuvant si un fisier txt,
si afiseaza de cate ori apare acel cuvant in fisierul text.
"""

"""
EX3: Creeaza un fisier CSV, numit produse.csv cu urmatorul continut:
- coloane: id, nume_produs, pret, cantitate.
Adauga 4 randuri in fisierul csv cu detalii despre 4 produse.

Citeste informatiile din fisierul csv folosind DictReader si
pune informatiile citite intr-un fisier json, numit "produse.json".
"""
```

## 📌 Python Packages
- Python Standard Library - putem face import fara sa instalam
librarii. Exemple: math, random
- Python Packages - este necesar sa facem instalarea pachetului
inainte sa il utilizam si astfel putem folosi functiile/metodele
astfel incat sa ne optimizam codul. Exemple: behave, SQLAlchemy etc.
- Pentru pachete extra, facute de alti developeri, avem PYPI:
https://pypi.org si folosim comanda pip pentru instalarea lor.
- Link-uri de studiat:
1. https://packaging.python.org/tutorials/installing-packages/
2. https://packaging.python.org/tutorials/packaging-projects/


## 📌 Virtual environments
- Este folosit pentru a gestiona python packages pentru diferite
proiecte.
- Avantaje:
  - putem descarca pachete in proiectul nostru fara privilegii de administrator
  - putem crea un pachet cu aplicatia noastra si ulterior o putem partaja cu alti programatori
  - putem crea cu usurinta o lista de dependinte si subdependinte intr-un fisier
, ceea ce face mai usor pentru alti programatori sa reproduca/dezvolte
si sa instaleze toate dependintele utilizate de noi in virtual environment
- Instalare virtualenv (adica programul care ne ajuta sa cream si sa folosim un virtual env)
  - putem folosi comanda: ```pip install virtualenv```
- Avem 3 parti importante in folosirea lui:
1. CREARE: ```python -m venv <nume_folder_venv>``` - aici de obicei
folosim env/venv/myenv pentru acel nume de folder, sa zicem de exemplu
ca il numim myenv. Crearea se face o singura data!
2. ACTIVARE: trebuie sa il activam ori de cate ori avem nevoie
sa rulam proiectul, sa instalam o librarie; comanda de activare e diferita in functie
de sistemul de operare:
- OSX: ```source myenv/bin/activate```
- Windows Powershell: ```myenv/Scripts/Activate.ps1```
- Windows cmd/Pycharm Terminal: ```myenv/Scripts/activate.bat```
3. DEZACTIVARE: asta o putem face cand vrem in acelasi terminal sa trecem
sa lucram la un alt proiect, comanda e: ```deactivate```
