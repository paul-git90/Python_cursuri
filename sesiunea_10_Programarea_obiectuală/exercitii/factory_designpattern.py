from abc import ABC, abstractmethod


class Vehicul(ABC):
    @abstractmethod
    def descrie(self):
        pass


class Masina(Vehicul):
    def descrie(self):
        return "Acesta este o mașină."


class Bicicleta(Vehicul):
    def descrie(self):
        return "Acesta este o bicicletă."


# Factory pentru crearea vehiculelor
class VehiculFactory:
    def creeaza_vehicul(self, tip_vehicul):
        if tip_vehicul == "masina":
            return Masina()
        elif tip_vehicul == "bicicleta":
            return Bicicleta()
        else:
            raise ValueError("Tipul de vehicul necunoscut.")


# Cod principal
factory = VehiculFactory()

vehicul1 = factory.creeaza_vehicul("masina")
vehicul2 = factory.creeaza_vehicul("bicicleta")

print(vehicul1.descrie())  # Acesta este o mașină.
print(vehicul2.descrie())  # Acesta este o bicicletă.
