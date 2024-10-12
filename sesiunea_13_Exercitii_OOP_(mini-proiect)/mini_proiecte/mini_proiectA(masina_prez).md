# Proiect: Clasa Mașină - OOP în Python

## Descriere Generală
Acest proiect implementează clasa `Masina`, care reprezintă o mașină produsă de o fabrică. Obiectele instanțiate din această clasă au diverse atribute (marca, model, viteza maximă, viteza actuală, culoare, etc.) și metode care definesc comportamentul unei mașini (accelerare, frânare, vopsire, etc.).

### Atribute:
- **marca**: Numele mărcii mașinii. Fabrica produce o singură marcă de mașini (de exemplu, `Toyota`).
- **model**: Modelul specific al mașinii (de exemplu, `Corolla`).
- **viteza_maxima**: Viteza maximă pe care o poate atinge mașina (de exemplu, `180 km/h`).
- **viteza_actuala**: Viteza curentă a mașinii. Inițial, este setată la `0 km/h`, adică mașina este oprită.
- **culoare**: Culoarea curentă a mașinii. Toate mașinile ies din fabrică în culoarea `gri`.
- **culori_disponibile**: Set de culori disponibile pentru vopsirea mașinii. De exemplu, `{'rosu', 'albastru', 'verde', 'negru', 'alb', 'gri'}`.
- **inmatriculata**: Boolean care indică dacă mașina este înmatriculată. Inițial, mașina nu este înmatriculată (`False`).
- 
### Clasa:
```python
class Masina:
    # Atribute de clasă
    marca = "Toyota"  # Exemplu de marcă - fabrica produce o singură marcă
    culori_disponibile = {"rosu", "albastru", "verde", "negru", "alb", "gri"}  # Set de culori disponibile
```

### Constructor:
```python
def __init__(self, model, viteza_maxima):
    self.model = model
    self.viteza_maxima = viteza_maxima
    self.viteza_actuala = 0
    self.culoare = 'gri'
    self.inmatriculata = False
```
- **Constructorul** inițializează modelul și viteza maximă, iar celelalte atribute sunt setate cu valori implicite la crearea unui obiect de tip Masina.

### Metode:
- **1. descrie() 
Metoda afișează toate atributele mașinii, cu excepția culorilor disponibile.**
```python
def descrie(self):
    print(f"Marca: {self.marca}")
    print(f"Model: {self.model}")
    print(f"Viteza maximă: {self.viteza_maxima} km/h")
    print(f"Viteza actuală: {self.viteza_actuala} km/h")
    print(f"Culoare: {self.culoare}")
    print(f"Înmatriculată: {'Da' if self.inmatriculata else 'Nu'}")
```
- **2. inmatriculare() 
Această metodă marchează mașina ca fiind înmatriculată prin schimbarea atributului inmatriculata la True.**
```python
def inmatriculare(self):
    self.inmatriculata = True
    print("Mașina a fost înmatriculată.")
```
- **3. vopseste(culoare_noua) 
Metoda schimbă culoarea mașinii, dar doar dacă culoarea nouă este inclusă în setul de culori disponibile.**
```python
def vopseste(self, culoare_noua):
    if culoare_noua in self.culori_disponibile:
        self.culoare = culoare_noua
        print(f"Mașina a fost vopsită în culoarea {culoare_noua}.")
    else:
        print(f"Eroare: Culoarea {culoare_noua} nu este disponibilă. Alegeți din: {self.culori_disponibile}")
```
- **4. accelereaza(viteza)
Metoda accelerează mașina la o anumită viteză, având grijă să nu depășească viteza maximă. Dacă viteza introdusă este negativă, se afișează o eroare.**
````python
def accelereaza(self, viteza):
    if viteza < 0:
        print("Eroare: Viteza nu poate fi negativă.")
    elif viteza > self.viteza_maxima:
        self.viteza_actuala = self.viteza_maxima
        print(f"Mașina a accelerat până la viteza maximă: {self.viteza_maxima} km/h.")
    else:
        self.viteza_actuala = viteza
        print(f"Mașina a accelerat până la {self.viteza_actuala} km/h.")
````
- **5. franeaza()
Această metodă setează viteza actuală a mașinii la 0, simulând frânarea.**
````python
def franeaza(self):
    self.viteza_actuala = 0
    print("Mașina a frânat și s-a oprit.")
````
### Testare completă a clasei `Masina`

class Masina:
pass

```python
# Creăm un obiect de tip Masina
masina_mea = Masina(model="Corolla", viteza_maxima=180)

# Descriem mașina
masina_mea.descrie()

# Vopsim mașina într-o culoare disponibilă
masina_mea.vopseste("albastru")

# Încercăm să vopsim mașina într-o culoare indisponibilă
masina_mea.vopseste("roz")

# Accelerăm mașina
masina_mea.accelereaza(150)

# Frânăm mașina
masina_mea.franeaza()

# Înmatriculăm mașina
masina_mea.inmatriculare()

# Descriem din nou pentru a vedea modificările
masina_mea.descrie()
````
**Concluzie
Acest proiect demonstrează utilizarea principiilor programării orientate pe obiecte (OOP) în Python pentru a crea o clasă Masina. Atributele și metodele clasei sunt concepute pentru a simula funcționalitățile unei mașini reale, iar testarea finală ilustrează modul în care clasa poate fi utilizată pentru a crea și manipula obiecte de tip Masina.**

Acest fișier **.md** include:
- Explicațiile tuturor atributelor și metodelor clasei `Masina`.
- Exemple clare de testare și utilizare a fiecărei metode.
- O concluzie care rezumă utilizarea principiilor OOP.


