"""
model simplu fara constructor
"""


class Car:  # definim clasa

    # definim atributele/fild-urile clasei
    make = "Dacia"
    model = None
    year = 2022
    color = None

    # definim metode
    def accelerate(self):
        print("Vruum!")


car1 = Car()  # initializam obiectul de tip Car
car2 = Car()  # car2 este instanta clasei

# dupa . avem acces la atribute si metodele
car1.model = "Duster"  # putem suprascrie valori
car1.accelerate()

"""
model cu constructor
"""


class Car:
    # fields (attributes)
    make = 'Dacia'
    year = 2022

    def __init__(self, model, color):
        self.model = model
        self.color = color


car1 = Car('Duster', 'white')
car3 = Car('Logan', 'blue')

print(car1.make)
print(car1.model)
print(car1.color)

"""
alt model
"""


class Cafea:  # definim clasa Cafea

    def __init__(self, tip, intensitate, aroma, cantitate):  # definim constructorul clasei
        self.tip = tip
        self.intensitate = intensitate
        self.aroma = aroma
        self.cantitate = cantitate

    def prepara(self):  # definim metoda prepara() metoda fara param
        print(f"Prepar cafea {self.tip} cu intensitatea {self.intensitate} și aroma {self.aroma}.")

    def adauga_lapte(self, cantitate_lapte):  # definim adauga_lapte() metoda cu param
        print(f"Am adăugat {cantitate_lapte}ml de lapte la cafeaua {self.tip}.")
        spuma_lapte(cantitate_lapte)  # aici apelez functia spuma_lapte() creata in afara clasei

    def adauga_zahar(self, cantitate_zahar):  # definim adauga_zahar() metoda cu param
        print(f"Am adăugat {cantitate_zahar}g de zahăr la cafeaua {self.tip}.")

    def schimba_aroma(self, noua_aroma):  # definim metoda schimba_aroma() metoda cu param
        print(f"Am schimbat aroma cafelei {self.tip} cu {noua_aroma}.")


# diferenta dintre functii si metode este data de faptul ca functiile sunt independente
# iar metodele sunt create in interiorul clasei

def spuma_lapte(cantitate_lapte):  # definim functia spuma_lapte() care va avea un param
    print(f"Am făcut spumă de lapte cu {cantitate_lapte}ml.")

# obiect - este reprez reala a unui tipar de clasa si se mai numeste si o instanta a clasei


cafea_espresso = Cafea("Espresso", "tare", "intensa", 30)  # am creat obiectul folosindu-ma de class Cafea
cafea_cu_lapte = Cafea("Cafea cu lapte", "tare", "vanilie", 120)  # am creat obiectul folosindu-ma de class Cafea
cafea_simpla1 = Cafea("Cafea simpla", "normala", "caramel sarat", 250)
cafea_simpla2 = Cafea(tip="Cafea simpla", intensitate="normala", aroma="caramel sarat", cantitate=250)
cafea_simpla3 = Cafea(tip="Cafea simpla", intensitate="normala", aroma="cioco", cantitate=120)
cafea_simpla4 = Cafea("Cafea simpla", "normala", "vanilie", 300)


aroma = "carmel"
cafea_cu_lapte.schimba_aroma(aroma)  # apelez pe obiectul creat cafea_cu_lapte metoda schimba_aroma()
cafea_cu_lapte.adauga_lapte(50)  # care va avea ca atribut "caramel sarat
cafea_cu_lapte.prepara()

cafea_espresso.prepara()  # apelez metoda prepara() din clasa Cafea pe obiectul creat
cafea_espresso.adauga_lapte(20)  # apelez metoda adauga_lapte() din clasa Cafea pe obiectul creat si voi da valoare
cafea_espresso.adauga_zahar(10)  # apelez metoda adauga_zahar() din clasa Cafea pe obiectul creat si voi da valoare
