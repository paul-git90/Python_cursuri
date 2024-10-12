from datetime import date


class Angajat:
    # Constructor care initializeaza numele, prenumele si salariul
    def __init__(self, nume, prenume, salariu):
        self.nume = nume  # Atributul pentru numele de familie
        self.prenume = prenume  # Atributul pentru prenumele
        self.salariu = salariu  # Atributul pentru salariu lunar

    # Metoda care descrie angajatul, afisand toate atributele
    def descrie(self):
        print(f"Angajat: {self.nume_complet()}, Salariu lunar: {self.salariu}")

    # Metoda care returneaza numele complet
    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    # Metoda care returneaza salariul lunar
    def salariu_lunar(self):
        return self.salariu

    # Metoda care returneaza salariul anual (12 luni)
    def salariu_anual(self):
        return self.salariu * 12

    # Metoda care aplica o marire de salariu, dupa un procent dat
    def marire_salariu(self, procent):
        marire = self.salariu * (procent / 100)
        self.salariu += marire
        print(f"Salariul a fost marit cu {procent}%. Noul salariu este {self.salariu}.")


class Factura:
    # Seria este constantă pentru toate facturile
    SERIA = "F2024"

    # Constructor pentru inițializarea numărului, numelui produsului, cantității și prețului
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    # Metoda pentru schimbarea cantității
    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    # Metoda pentru schimbarea prețului
    def schimba_pretul(self, pret):
        self.pret_buc = pret

    # Metoda pentru schimbarea numelui produsului
    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    # Metoda care generează și afișează factura
    def genereaza_factura(self):
        total = self.cantitate * self.pret_buc
        data_curenta = date.today()

        # Format tabelar pentru factura
        print(f"Factura seria {self.SERIA} număr {self.numar}")
        print(f"Data: {data_curenta}")
        print(f"{'Produs':<15} | {'Cantitate':<10} | {'Preț buc':<10} | {'Total':<10}")
        print(f"{self.nume_produs:<15} | {self.cantitate:<10} | {self.pret_buc:<10} | {total:<10}")


factura1 = Factura(101, "Telefon", 7, 700)
factura1.genereaza_factura()

factura1.schimba_cantitatea(10)
factura1.schimba_pretul(750)
factura1.genereaza_factura()
