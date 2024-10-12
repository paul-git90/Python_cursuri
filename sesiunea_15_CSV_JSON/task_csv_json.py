import csv
import json

"""
EXERCITII BONUS FISIERE
"""

# todo EX 1: Copierea conținutului dintr-un fișier în alt fișier

"""
Cerinta: Trebuie să creăm un fișier sursa.txt, să adăugăm conținut în el, apoi să copiem acest conținut 
într-un alt fișier numit destinatie.txt.

Soluție și logică:
1. Scrierea în fișierul sursa.txt:
Deschidem fișierul sursa.txt în modul write și scriem conținutul dorit.
Logica: open("sursa.txt", "w") creează fișierul (dacă nu există deja) și permite scrierea de conținut în el.
2. Citirea din sursa.txt și scrierea în destinatie.txt:
Deschidem fișierul sursa.txt în modul read, citim conținutul.
Deschidem fișierul destinatie.txt în modul write și scriem conținutul copiat din sursa.txt.
3. Afișarea conținutului din destinatie.txt:
Deschidem destinatie.txt în modul read și afișăm conținutul.
"""


# EX1
def copie_fisier():
    # Creăm fisierul sursa.txt și scriem conținutul în el
    with open("sursa.txt", "w", encoding="utf-8") as sursa:
        sursa.write("Acesta este un exemplu de text.\n")
        sursa.write("Liniile vor fi copiate în alt fișier.\n")

    # Citim din sursa.txt
    with open("sursa.txt", "r", encoding="utf-8") as sursa:
        continut = sursa.read()

    # Scriem în destinatie.txt
    with open("destinatie.txt", "w", encoding="utf-8") as destinatie:
        destinatie.write(continut)

    # Citim din destinatie.txt și afișăm conținutul
    with open("destinatie.txt", "r", encoding="utf-8") as destinatie:
        print("Conținutul fișierului destinatie.txt:")
        print(destinatie.read())


copie_fisier()


# todo EX 2: Numararea cuvintelor într-un fișier

"""
Cerinta: Să creăm o funcție care primește un cuvânt și un fișier text, și afișează de câte ori apare acel cuvânt 
în fișier.

Soluție și logică:
1. Deschiderea fișierului: Folosim open() pentru a deschide fișierul în modul read.
2. Citirea conținutului: Citim tot conținutul fișierului într-un string.
3. Numărarea cuvântului: Folosim metoda count() pentru a număra de câte ori apare cuvântul în text.
"""


# EX2
def numarare_cuvinte_in_fisier(cuvant, fisier_txt):
    with open(fisier_txt, "r", encoding="utf-8") as file:
        continut = file.read()

    # Numărăm de câte ori apare cuvântul
    numar_aparitii = continut.lower().count(cuvant.lower())
    print(f"Cuvântul '{cuvant}' apare de {numar_aparitii} ori în {fisier_txt}.")


"""
Explicație:

Fișierul este citit ca un string complet.
Pentru a evita problemele cu majusculele și minusculele, am folosit lower() pentru a transforma tot textul în 
litere mici.
Metoda count() numără toate aparițiile cuvântului specificat.
"""

# todo EX 3: Crearea și citirea unui fișier CSV, apoi scrierea în JSON

"""
Cerinta: Trebuie să creăm un fișier CSV cu 4 produse și să scriem informațiile din acest fișier într-un fișier JSON.

Soluție și logică:
1. Crearea unui fișier CSV:
Folosim csv.writer() pentru a scrie în CSV.
Structura fișierului va conține 4 coloane: id, nume_produs, pret, cantitate.
2. Citirea fișierului CSV cu csv.DictReader:
DictReader citește rândurile și le transformă în dicționare, unde cheile sunt numele coloanelor.
3. Scrierea în fișierul JSON:
Folosim json.dump() pentru a scrie conținutul din CSV într-un fișier JSON.
"""

# EX3
# import csv
# import json


def creeaza_fisier_csv():
    with open("produse.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Scriem header-ul
        writer.writerow(['id', 'nume_produs', 'pret', 'cantitate'])
        # Scriem produsele
        writer.writerow([1, 'Laptop', 3000, 5])
        writer.writerow([2, 'Mouse', 50, 10])
        writer.writerow([3, 'Tastatura', 150, 8])
        writer.writerow([4, 'Monitor', 700, 3])


def citeste_csv_si_scrie_in_json():
    produse = []

    # Citim din CSV
    with open("produse.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            produse.append(row)

    # Scriem în JSON
    with open("produse.json", "w", encoding="utf-8") as file_json:
        json.dump(produse, file_json, indent=4)

    # Afișăm conținutul fișierului JSON pentru verificare
    with open("produse.json", "r", encoding="utf-8") as file_json:
        continut_json = json.load(file_json)
        print(json.dumps(continut_json, indent=4))


# Apelăm funcțiile
creeaza_fisier_csv()
citeste_csv_si_scrie_in_json()

"""
Explicație:

Am folosit csv.writer() pentru a crea fișierul CSV și a adăuga produsele.
csv.DictReader() ne permite să citim fișierul CSV într-o structură ușor de utilizat, unde fiecare rând devine 
un dicționar.
json.dump() scrie o listă de dicționare în format JSON.
"""
# TODO encoding="utf-8" - ERROR
"""
În cazul tău, ai folosit diacritice în textul „Liniile vor fi copiate în alt fișier”, unde apare caracterul ș (\u0219), 
ceea ce a cauzat eroarea.

Soluția
Pentru a evita astfel de erori, este necesar să specifici encoding-ul corect, cum ar fi utf-8, atunci când lucrezi cu 
fișiere text care conțin caractere speciale.

Corectarea codului:
Modifică funcțiile unde se scriu și se citesc fișiere pentru a specifica encoding="utf-8" în apelurile funcției open().

encoding="utf-8": Specificarea explicită a acestui encoding rezolvă problema scrierii și citirii caracterelor Unicode 
(de exemplu, diacriticele din limba română) într-un mod corect și fără erori.
UnicodeEncodeError, și apare atunci când scrii sau citești caractere speciale (cum ar fi diacriticele din limba română) 
fără să specifici encoding-ul corect. Windows, în mod implicit, folosește encoding-ul cp1252, care nu suportă toate 
caracterele Unicode.
"""