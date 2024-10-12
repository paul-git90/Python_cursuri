"""
CSV (Comma Separated Values) este un format de fișier text care stochează datele într-o structură tabelară,
în care fiecare rând reprezintă o linie din tabel, iar fiecare valoare dintr-o linie este separată de o virgulă
(sau alt delimitator). Fișierele CSV sunt folosite pe scară largă pentru importul și exportul de date din aplicații
precum Excel, baze de date sau alte programe care manipulează date structurate.
Format simplu: Fiecare rând reprezintă un rând dintr-un tabel, iar valorile sunt separate de un delimitator
(în mod implicit, virgula).
Compatibilitate ridicată: Fișierele CSV pot fi deschise și modificate cu o varietate de aplicații, inclusiv Excel,
Google Sheets, sau editori de text simpli.
Flexibilitate: Deși numele sugerează utilizarea virgulei ca delimitator, în unele cazuri sunt folosiți și alți
delimitatori, cum ar fi punctul și virgula (;) sau tabulatorul (\t).
Structură tabelară: Fiecare rând poate conține un set de valori, fiecare corespunzând unei coloane din tabel.
csv.writer(): pentru scrierea fișierelor CSV.
csv.reader() si
csv.DictReader(): pentru citirea fișierelor CSV.
"""

# 1. Scrierea într-un fișier CSV

import csv

with open("path_to_csv_file.csv", "w", newline='') as file:  # Deschidem fișierul CSV în modul de scriere
    writer = csv.writer(file)  # Inițializăm un obiect writer

    # Scriem un rând de header (titlurile coloanelor)
    writer.writerow(['id', 'nume'])

    # Scriem rânduri de date
    writer.writerow([1, 'Paula'])
    writer.writerow([2, 'Ana'])

# 2. Citirea unui fișier CSV

# import csv

with open("path_to_csv_file.csv", "r") as file:  # Deschidem fișierul CSV în modul de citire
    reader = csv.reader(file)  # Inițializăm un obiect reader

    # Citim un rând la un moment dat
    row = next(reader)  # Citim primul rând (header-ul)
    print(row)  # Afișăm header-ul

    # Citim restul rândurilor folosind un for-loop
    for row in reader:
        print(row)  # Afișăm fiecare rând de date

# 3. Citirea unui fișier CSV folosind csv.DictReader()

# import csv

with open('path_to_csv_file.csv', 'r') as file:  # Deschidem fișierul CSV în modul de citire
    reader = csv.DictReader(file)  # Inițializăm un obiect DictReader

    # Iterăm prin fiecare rând (care este un dicționar)
    for row in reader:
        print(row)  # Fiecare rând va fi un dicționar cu perechi cheie-valoare

# 4. Adăugarea de date într-un fișier CSV

# import csv

with open("path_to_csv_file.csv", "a", newline='') as file:  # Deschidem fișierul în modul append
    writer = csv.writer(file)

    # Adăugăm noi rânduri de date
    writer.writerow([3, 'Maria'])
    writer.writerow([4, 'Ioana'])

reader = csv.reader(file, delimiter=';')

# Concluzie
"""
Fișierele CSV sunt extrem de utile pentru stocarea datelor în formă tabelară și pentru schimbul de 
informații între aplicații. Modulul csv din Python oferă funcții simple și eficiente pentru citirea 
și scrierea acestor fișiere, fie că lucrăm cu liste simple sau cu dicționare.
"""