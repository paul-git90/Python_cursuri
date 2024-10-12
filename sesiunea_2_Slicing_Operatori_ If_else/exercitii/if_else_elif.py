"""
 If...else if ... else
"""
# exemplu
# robotelul telefonic
optiune = int(input('alege o optiune'))
if optiune == 0:
    print('meniul anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print('ati ales eng')
else:
    print('Nu am identificat optiunea, mai incearca.')
"""
EX13: Citeste de la tastatura varsta utilizatorului si afiseaza categoria
de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
"""
# Citirea varstei utilizatorului de la tastatura
varsta = int(input("Introduceți vârsta dvs.: "))
# Verificarea categoriei de varsta
if 0 <= varsta < 18:
    print("Minor")
elif 18 <= varsta <= 65:
    print("Adult")
elif varsta > 65:
    print("Senior")
else:
    print("Vârsta introdusă nu este validă.")
"""
EX14: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
cosul de cumparaturi, in functie de totalul cosului de cumparaturi
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
dupa aplicarea reducerii.
"""
# Citirea totalului cosului de cumparaturi de la tastatura
total_cos = float(input("Introduceți totalul coșului de cumpărături: "))
# Calcularea pretului dupa aplicarea reducerii
if 100 <= total_cos < 200:
    reducere = 10 / 100
elif 200 <= total_cos < 300:
    reducere = 15 / 100
elif 300 <= total_cos < 400:
    reducere = 20 / 100
elif total_cos >= 400:
    reducere = 30 / 100
else:
    reducere = 0
pret_final = total_cos * (1 - reducere)
# Afisarea pretului final
print(f"Prețul final după aplicarea reducerii este: {pret_final:.2f} lei")
