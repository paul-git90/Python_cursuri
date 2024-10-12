# apometru.py

class CitireContor:
    def __init__(self):
        self.citiri = {}

    def adauga_citire(self, luna, an, apa_rea, apa_calda):
        luna = luna.lower()
        if luna in self.citiri:
            print("Eroare: Există deja o citire pentru luna respectivă.")
            return
        if len(self.citiri) > 0 and luna in self.citiri:
            # Verifică valoarea de pe luna precedentă
            if self.citiri[luna]['apa_rea'] > apa_rea or self.citiri[luna]['apa_calda'] > apa_calda:
                print("Eroare: Valorile contoarelor sunt invalide.")
                return

        self.citiri[luna] = {
            'an': an,
            'apa_rea': apa_rea,
            'apa_calda': apa_calda
        }
        print(f"Citire adăugată pentru {luna} {an}: Apa caldă {apa_calda}, Apă rece {apa_rea}")

    def sterge_citire(self, luna, an):
        luna = luna.lower()
        if luna not in self.citiri:
            print("Eroare: Nu există o citire pentru anul și luna introduse.")
            return
        del self.citiri[luna]
        print(f"Citire ștearsă pentru {luna} {an}.")

    def afiseaza_consum(self, luna, an):
        luna = luna.lower()
        if luna not in self.citiri:
            print("Eroare: Nu există o citire pentru anul și luna introduse.")
            return

        print(f"Valorile contoarelor pentru {luna} {an}:")
        if luna != 'ian' and (self.citiri.get(luna) and self.citiri.get(luna[:-1] + 'a')):
            luna_precedenta = luna[:-1] + 'a' if luna != 'dec' else 'ian'
            print(f"Apa caldă pe luna precedentă: {self.citiri[luna_precedenta]['apa_calda']}")
            print(f"Apă rece pe luna precedentă: {self.citiri[luna_precedenta]['apa_rea']}")
            consum_apa_calda = self.citiri[luna]['apa_calda'] - self.citiri[luna_precedenta]['apa_calda']
            consum_apa_rea = self.citiri[luna]['apa_rea'] - self.citiri[luna_precedenta]['apa_rea']
            print(f"Consum apă caldă: {consum_apa_calda}")
            print(f"Consum apă rece: {consum_apa_rea}")
        else:
            print(f"Apa caldă: {self.citiri[luna]['apa_calda']}")
            print(f"Apă rece: {self.citiri[luna]['apa_rea']}")


def main():
    contor = CitireContor()
    while True:
        print("\nAlegeti o optiune: ")
        print("1. Adauga citire")
        print("2. Sterge citire")
        print("3. Afiseaza consum")
        print("4. Iesire")
        optiune = input("> ")

        if optiune == "1":
            luna = input("Introduceti luna (ex: ian, feb, ...): ")
            an = input("Introduceti anul: ")
            apa_rea = float(input("Introduceti valoarea contorului de apa rece: "))
            apa_calda = float(input("Introduceti valoarea contorului de apa calda: "))
            contor.adauga_citire(luna, an, apa_rea, apa_calda)
        elif optiune == "2":
            luna = input("Introduceti luna (ex: ian, feb, ...): ")
            an = input("Introduceti anul: ")
            contor.sterge_citire(luna, an)
        elif optiune == "3":
            luna = input("Introduceti luna (ex: ian, feb, ...): ")
            an = input("Introduceti anul: ")
            contor.afiseaza_consum(luna, an)
        elif optiune == "4":
            print("Iesire din aplicatie.")
            break
        else:
            print("Optiune invalida!")


if __name__ == "__main__":
    main()
