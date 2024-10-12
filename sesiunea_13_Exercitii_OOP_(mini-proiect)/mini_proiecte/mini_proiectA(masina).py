class Masina:
    # Atribute de clasă
    marca = "Toyota"  # Exemplu de marcă - fabrica produce o singură marcă
    culori_disponibile = {"rosu", "albastru", "verde", "negru", "alb", "gri"}  # Set de culori disponibile

    def __init__(self, model, viteza_maxima):
        # Atribute de instanță
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0  # La început, toate mașinile stau pe loc
        self.culoare = "gri"  # Toate mașinile ies din fabrică în culoarea gri
        self.inmatriculata = False  # Inițial, mașinile nu sunt înmatriculate

    def descrie(self):
        # Metodă care afișează toate informațiile despre mașină, cu excepția culorilor disponibile
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Viteza maximă: {self.viteza_maxima} km/h")
        print(f"Viteza actuală: {self.viteza_actuala} km/h")
        print(f"Culoare: {self.culoare}")
        print(f"Înmatriculată: {'Da' if self.inmatriculata else 'Nu'}")

    def inmatriculare(self):
        # Metodă care schimbă statusul înmatriculării la True
        self.inmatriculata = True
        print("Mașina a fost înmatriculată.")

    def vopseste(self, culoare_noua):
        # Metodă care vopsește mașina într-o culoare nouă, dacă este disponibilă
        if culoare_noua in self.culori_disponibile:
            self.culoare = culoare_noua
            print(f"Mașina a fost vopsită în culoarea {culoare_noua}.")
        else:
            print(f"Eroare: Culoarea {culoare_noua} nu este disponibilă. Alegeți din: {self.culori_disponibile}")

    def accelereaza(self, viteza):
        # Metodă care accelerează mașina la o anumită viteză, dacă viteza e validă
        if viteza < 0:
            print("Eroare: Viteza nu poate fi negativă.")
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f"Mașina a accelerat până la viteza maximă: {self.viteza_maxima} km/h.")
        else:
            self.viteza_actuala = viteza
            print(f"Mașina a accelerat până la {self.viteza_actuala} km/h.")

    def franeaza(self):
        # Metodă care oprește mașina (viteza devine 0)
        self.viteza_actuala = 0
        print("Mașina a frânat și s-a oprit.")

# Testare


# Creăm un obiect de tip Masina
masina_mea = Masina(model="Corolla", viteza_maxima=180)

# Descriem mașina
masina_mea.descrie()

# Încercăm să vopsim mașina într-o culoare disponibilă
masina_mea.vopseste("albastru")

# Încercăm să vopsim mașina într-o culoare indisponibilă
masina_mea.vopseste("roz")

# Accelerăm mașina la o viteză permisă
masina_mea.accelereaza(120)

# Accelerăm mașina peste viteza maximă
masina_mea.accelereaza(200)

# Frânăm mașina
masina_mea.franeaza()

# Înmatriculăm mașina
masina_mea.inmatriculare()

# Descriem din nou pentru a vedea modificările
masina_mea.descrie()
