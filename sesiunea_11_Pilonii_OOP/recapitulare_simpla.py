# variabile si tipuri de date

nume_variabila1 = True
nume_variabila2 = "Nume", "O'Shea"
nume_variabila3 = 20, 3.14
nume_variabila4 = None

lista = ["Mihai", "Florin", "Popescu", "Mircea", 3.21, 900, True, None]
tuple = (None, 22.3456, 32.23456, 12, 32, 76, 90, "Arad", "Cluj", "Constanta", False)
set = {"Florin", 23, "Sergiu", 11, "Popescu", True, 3.14, None}
dict = {
    "Nume": "Ion",
    "Prenume": "Popescu",
    "Nascut": {"Varsta": 45, "Oras": "Brasov"},
    "Ocupație": {"Manager", "Coordonator", "Instructor"},
    "Companie": {"Nume": "Hyperfine", "Locatie": "Bucuresti"},
    "Inventar": ("carti", "scaune", "birou", "rafturi", "cafetiera"),
    "Salariu": {1200: "euro"},
    None: True
}

print(dict)

# cicluri repetitive

i = 0
while i > 10:
    print(i)
    i += 1

for i in range(8):
    print(i)

for element in lista:
    print(element)

for i in range(len(tuple)):
    print(i)
    print(tuple[i])


# functii


def nume_functie():
    print("Text")


def numefunctie(text):
    print(text)


nume_functie()
numefunctie("Ion")


# clase si OOP


class ClasaPython:
    atribut_clasa = 10

    def __init__(self,atribut_obiect):
        self.atribut_obiect = atribut_obiect

    def metoda(self):
        print(f"python class")

    def metoda_param(self, param):
        print(f"python {param}")


obiect1 = ClasaPython(14)
obiect1.metoda()
obiect1.atribut_clasa = 15
obiect1.metoda_param(16)


class ClasaJava:
    pass

    def code(self):
        print("java")

    def code_param(self, param):
        print(f"java {param}")


obiect_java = ClasaJava()
obiect_java.code()
obiect_java.code_param('CODE')
