"""
Cum funcționează with statement?
Când folosim with open(...) as file:, Python gestionează automat deschiderea și închiderea fișierului.
După ce execuția blocului with se termină, fișierul este închis automat, ceea ce asigură că nu vom avea
fișiere deschise neînchise corect.
"""


def scriere_in_fisier_txt(calea_fisier, informatii_as_list):
    """Scrie date într-un fișier text folosind 'with' pentru a închide fișierul automat."""
    with open(calea_fisier, mode="w") as file:
        file.writelines(informatii_as_list)  # Scrie fiecare linie din listă în fișier


def citire_din_fisier_txt(calea_fisier):
    """Citește date dintr-un fișier text folosind 'with' pentru a gestiona automat resursele."""
    with open(calea_fisier, mode='r') as file:
        return file.readlines()  # Returnează o listă cu toate liniile din fișier


# Apelarea funcțiilor
informatii = ["Linia 1\n", "Linia 2\n", "Linia 3\n"]
scriere_in_fisier_txt("dummy.txt", informatii)

# Citirea fișierului pentru a vedea ce conține
linii = citire_din_fisier_txt("dummy.txt")
print("Conținutul fișierului:")
for linie in linii:
    print(linie.strip())  # Afișăm fiecare linie fără caracterele de salt de linie

"""
Explorarea modului de deschidere append (mode="a")
Modul "a" (append) ne permite să deschidem un fișier pentru a adăuga noi informații la finalul său, 
fără a șterge conținutul existent. Este util atunci când vrem să păstrăm istoricul 
sau să adăugăm linii noi într-un fișier existent.
"""


def adaugare_in_fisier_txt(calea_fisier, informatii_as_list):
    """Adaugă informații la sfârșitul unui fișier text fără a șterge conținutul existent."""
    with open(calea_fisier, mode="a") as file:
        file.writelines(informatii_as_list)  # Adaugă liniile noi la finalul fișierului


# Apelarea funcției pentru a adăuga informații
informatii_noi = ["Linia 4\n", "Linia 5\n"]
adaugare_in_fisier_txt("dummy.txt", informatii_noi)

# Citim din nou fișierul pentru a verifica conținutul
linii = citire_din_fisier_txt("dummy.txt")
print("Conținut actualizat al fișierului:")
for linie in linii:
    print(linie.strip())

"""
Metode suplimentare de citire
a) read(size)
Această metodă permite citirea unui anumit număr de caractere specificate de parametru size. 
Dacă nu specificăm nimic, metoda va citi întregul fișier.
"""
with open("dummy.txt", mode="r") as file:
    continut_partial = file.read(10)  # Citim doar primele 10 caractere
    print(continut_partial)
"""
b) readline()
Aceasta citește o singură linie la fiecare apelare. 
Este utilă pentru a procesa fișiere linie cu linie.
"""
with open("dummy.txt", mode="r") as file:
    while True:
        linie = file.readline()
        if not linie:
            break
        print(linie.strip())
