"""
4.	Declara trei liste: una cu oameni, una cu salarii, si una cu meserii  (important: trebuie sa aiba acelasi număr
de elemente). Apoi foloseste functia zip, care primeste ca si parametru un numar de colectii si returneaza un
iterator pentru a afisa:
Pe mine ma cheama X, sunt de profesie Y, si castig Z ron pe luna
"""
# 1. Declarația listelor
oameni = ["Maria", "Andrei", "Ioana", "Matei", "Eusebiu"]
salarii = [3000, 4000, 3500, 5000, 4500]
meserii = ["programator", "medic", "profesor", "inginer", "artist"]

# 2. Utilizarea funcției zip pentru a itera prin listele corespunzătoare
print("Informații despre oameni:")
for nume, salariu, meserie in zip(oameni, salarii, meserii):
    print(f"Pe mine mă cheamă {nume}, sunt de profesie {meserie}, și câștig {salariu} RON pe lună.")

"""
Explicația codului:
Declarația listelor: Am definit trei liste:

oameni: conține numele persoanelor,
salarii: conține salariile lor (asigurându-ne că fiecare persoană are un salariu corespunzător),
meserii: conține meseriile corespunzătoare fiecărei persoane.
Este important ca toate cele trei liste să aibă același număr de elemente.

Funcția zip(): Aceasta combină cele trei liste într-un iterator care produce tupluri, fiecare tuplu 
conținând un element din fiecare listă.

Afișarea informațiilor: Folosim un for pentru a itera prin iteratorul returnat de zip(), iar pentru 
fiecare iterație, afișăm un mesaj care include numele, meseria și salariul corespunzător.
"""
