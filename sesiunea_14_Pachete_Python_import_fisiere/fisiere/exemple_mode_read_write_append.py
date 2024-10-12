"""
1. Scrierea unui fișier nou (write)
Pentru a crea și scrie în fișierul dummy.txt, folosești modul "w".
"""
# Crearea unui fisier nou si scrierea in el
fisier_nou = open(file="dummy.txt", mode="w")

# Scrierea de continut in fisier
fisier_nou.write("hello\n")
fisier_nou.write("world\n")

# Adaugam mai multe linii folosind writelines
fisier_nou.writelines(["line 1\n", "line 2\n", "line 3\n"])

# Inchidem fisierul dupa ce terminam
fisier_nou.close()
"""
2. Citirea unui fișier existent (read)
Pentru a citi conținutul unui fișier, folosești modul "r".
"""
# Deschidem fisierul in modul citire (read)
fisier_nou = open(file="dummy.txt", mode="r")

# Citim tot continutul fisierului
continut = fisier_nou.read()
print("Continutul fisierului este:")
print(continut)

# Inchidem fisierul dupa citire
fisier_nou.close()
"""
3. Citirea pe linii (readline și readlines)
Pentru a citi fișierul linie cu linie:
"""
# Deschidem fisierul pentru citirea liniilor
fisier_nou = open(file="dummy.txt", mode="r")

# Citim fiecare linie in mod individual
prima_linie = fisier_nou.readline()
a_doua_linie = fisier_nou.readline()

print(f"Prima linie: {prima_linie.strip()}")
print(f"A doua linie: {a_doua_linie.strip()}")

# Sau putem citi toate liniile deodata
toate_liniile = fisier_nou.readlines()
print("Toate liniile ramase sunt:")
for linie in toate_liniile:
    print(linie.strip())

# Inchidem fisierul
fisier_nou.close()
"""
4. Adăugarea de conținut la un fișier existent (append)
Dacă vrei să adaugi conținut într-un fișier deja existent, folosești modul "a".
"""
# Deschidem fisierul in modul append (adaugare)
fisier_nou = open(file="dummy.txt", mode="a")

# Adaugam noi linii la fisier
fisier_nou.write("This is a new line.\n")
fisier_nou.write("Appending another line.\n")

# Inchidem fisierul
fisier_nou.close()
"""
5. Citirea fiecărei a doua linie
Pentru a citi doar liniile impare (1, 3, 5, etc.), poți citi toate liniile și le procesezi cu un for-loop:
"""
# Deschidem fisierul pentru citire
fisier_nou = open(file="dummy.txt", mode="r")

# Citim toate liniile si afisam doar cele impare
liniile = fisier_nou.readlines()

print("Liniile impare din fisier:")
for i, linie in enumerate(liniile):
    if i % 2 == 0:  # indecsi 0, 2, 4 sunt liniile impare
        print(linie.strip())

# Inchidem fisierul
fisier_nou.close()

"""
Explicație:
write - suprascrie întreg conținutul fișierului.
append - adaugă conținut nou la finalul fișierului existent fără să suprascrie ce era deja în fișier.
read - citește întreg conținutul fișierului.
readline - citește fișierul linie cu linie.
readlines - citește toate liniile și le returnează ca o listă de stringuri.
"""