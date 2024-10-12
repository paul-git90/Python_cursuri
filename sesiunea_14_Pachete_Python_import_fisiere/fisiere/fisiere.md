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