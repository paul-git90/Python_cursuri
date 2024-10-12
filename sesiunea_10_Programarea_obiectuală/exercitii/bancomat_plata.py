from abc import ABC, abstractmethod

"""
aplicatie bancara
"""


class Plata(ABC):
    @abstractmethod
    def efectueaza_plata(self, suma):
        pass


class PlataCard(Plata):
    def efectueaza_plata(self, suma):
        print(f"Plata cu cardul de {suma} lei a fost efectuată.")


class PlataPayPal(Plata):
    def efectueaza_plata(self, suma):
        print(f"Plata cu PayPal de {suma} lei a fost efectuată.")


class PlataBitcoin(Plata):
    def efectueaza_plata(self, suma):
        print(f"Plata cu Bitcoin de {suma} lei a fost efectuată.")


def proces_plata(plata, suma):
    plata.efectueaza_plata(suma)


# Apeluri polimorfe
proces_plata(PlataCard(), 100)
proces_plata(PlataPayPal(), 200)
proces_plata(PlataBitcoin(), 300)
