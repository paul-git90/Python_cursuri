"""
Pattern care permite crearea unei singure instante a unei clase pe durata executiei programului.
Util in a limita accesul concurent la anumite resurse, creand un punct de acces global (ex: accesul la o baza de date)
"""

# Acest design pattern ne permite crearea unei singure instante a unei clase


class SingletonClass:
    __instance = None
    sector = "IT"

    def __init__(self, name):
        # initializam attribute,
        # chemat in momentul instantei obiectului
        self.name = name

    def __new__(cls, *args):
        # initializam clasa, metoda magica __new__
        # se apeleaza inaintea __init__
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


obj1 = SingletonClass("JavaScript")
print(obj1.name)
print(obj1.sector)
print(obj1)
print(id(obj1))

obj2 = SingletonClass("Python")
print(obj2.name)
print(obj2.sector)
print(obj2)
print(id(obj2))

print(obj1.name)
print(obj1 == obj2)
print(obj1 is obj2)

obj3 = SingletonClass("Assembly")
print(obj1.name)
print(obj2.name)
print(obj3.name)
