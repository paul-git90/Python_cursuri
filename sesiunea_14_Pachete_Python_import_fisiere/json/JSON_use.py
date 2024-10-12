"""
JSON (JavaScript Object Notation) este un format ușor de citit și de scris pentru stocarea și transportarea datelor.
Deși are rădăcini în JavaScript, este un format de date independent de limbaj,
folosit pe scară largă în multe limbaje de programare, inclusiv Python.
În majoritatea cazurilor, un fișier JSON arată foarte asemănător cu un dicționar sau o listă Python.
Interacțiunea cu fișiere JSON este facilitată de modulul încorporat json,
care permite citirea și scrierea datelor în acest format cu ușurință.
Compatibilitate cu multe tehnologii:
JSON este adesea folosit în API-uri și pentru transmiterea datelor între aplicații web.
json.load(): citește date dintr-un fișier JSON și le transformă într-un obiect Python (dicționar sau o listă).
json.dump(): scrie date dintr-un obiect Python într-un fișier JSON.
"""

# 1. Citirea unui fișier JSON

import json


def citire_din_fisier_json(cale_fisier):
    """Citește date dintr-un fișier JSON și returnează conținutul sub forma unui obiect Python."""
    with open(cale_fisier, 'r') as file:  # Deschidem fișierul JSON în modul de citire
        return json.load(file)  # Încărcăm datele JSON și le transformăm într-un obiect Python


# Exemplu de apelare a funcției
date_json = citire_din_fisier_json("quiz.json")
print(date_json)  # Afișăm conținutul citit din fișierul JSON
print(type(date_json))  # Tipul obiectului returnat, de obicei un dicționar sau o listă

# 2. Scrierea într-un fișier JSON

# import json


def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    """Scrie datele dintr-un obiect Python într-un fișier JSON."""
    with open(cale_fisier, 'w') as file:  # Deschidem fișierul JSON în modul de scriere
        json.dump(randuri_informatii, file, indent=4)  # Scriem datele în fișier, cu indentare pentru lizibilitate


# Exemplu de date care vor fi scrise în fișierul JSON
date_de_scris = {
    "quiz": {
        "math": {
            "question": "What is 2+2?",
            "options": [2, 3, 4, 5],
            "answer": 4
        },
        "science": {
            "question": "What planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter"],
            "answer": "Mars"
        }
    }
}

# Scriem datele de mai sus într-un fișier JSON
scriere_in_fisier_json("quiz.json", date_de_scris)

# Funcții suplimentare

# json.loads(): Transformă un șir de caractere (string) JSON într-un obiect Python.
data = '{"name": "John", "age": 30}'
python_obj = json.loads(data)
print(python_obj)  # {'name': 'John', 'age': 30}

# json.dumps(): Transformă un obiect Python într-un șir JSON.
# Aceasta este utilă pentru a afișa sau trimite datele JSON fără a le salva într-un fișier.
dict_data = {"name": "John", "age": 30}
json_string = json.dumps(dict_data, indent=4)
print(json_string)

# Concluzie
"""
JSON este un format excelent pentru stocarea și transportarea datelor, ușor de folosit în 
Python prin modulul integrat json. Acesta permite conversia rapidă între structurile de date 
Python și formatul JSON și este esențial în lucrul cu API-uri sau alte servicii care comunică 
prin intermediul acestui format.

Utilizarea with pentru manipularea fișierelor JSON asigură o gestionare eficientă a resurselor, 
iar funcțiile de citire și scriere oferă o interfață intuitivă pentru dezvoltatori.
"""
