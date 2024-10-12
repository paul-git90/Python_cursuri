"""
exemple de cod cu apelare sau input
"""


class TonomatCafea:
    def __init__(self, tip, cantitate, intensitate):  # Constructor cu parametrii inițiali
        self.tip = tip
        self.cantitate = cantitate
        self.intensitate = intensitate

    # Metodă pentru prepararea cafelei
    def prepara(self):
        print(f"Se prepară o cafea {self.tip} de cantitate {self.cantitate} "
              f"cu intensitate {self.intensitate}. Vă rugăm să așteptați.")


# Crearea instanțelor
lunga = TonomatCafea("Lunga", "Mare", "Medie")
scurta = TonomatCafea("Scurta", "Mică", "Intensă")

# Apelarea metodei pentru fiecare instanță
lunga.prepara()
scurta.prepara()


class TonomatCafea:
    def __init__(self):  # Constructor cu doar tipul de cafea
        self.tip = None
        self.cantitate = None
        self.intensitate = None

    # Metodă pentru interogarea userului asupra cantității și intensității
    def interogare(self):
        self.tip = input("Introduceți tipul de cafea: ")  # Interogăm utilizatorul pentru tipul de cafea
        self.cantitate = input("Selectați cantitatea: ")
        self.intensitate = input("Selectați intensitatea: ")

    # Metodă pentru prepararea cafelei
    def prepara(self):
        print(f"Se prepară o cafea {self.tip} de cantitate {self.cantitate} "
              f"cu intensitate {self.intensitate}. Vă rugăm să așteptați.")


# Cod principal
def ruleaza_tonomat():
    tonomat = TonomatCafea()  # Creăm un obiect TonomatCafea cu tipul ales
    tonomat.interogare()  # Interogăm utilizatorul pentru cantitate și intensitate
    tonomat.prepara()  # Preparăm cafeaua


# Rulăm programul
ruleaza_tonomat()
