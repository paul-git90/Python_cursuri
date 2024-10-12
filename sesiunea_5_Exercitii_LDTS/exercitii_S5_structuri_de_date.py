"""
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""
"""
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
   Găsește 2 variante să le unești într-o singură listă. 
"""
# Declarăm cele două liste
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# Metoda 1: Folosind operatorul de concatenare +
lista_unita1 = lista1 + lista2
print("Lista unită folosind operatorul +:", lista_unita1)
# Metoda 2: Folosind metoda extend()
lista_unita2 = lista1.copy()  # Facem o copie a primei liste pentru a nu o modifica direct
lista_unita2.extend(lista2)
print("Lista unită folosind metoda extend():", lista_unita2)
"""
4.
●	Sortează și afișează lista generată la exercițiul anterior.
●	Sortează numărul 0 folosind o funcție.
●	Afișaza iar lista.
"""
# Declarăm cele două liste
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# Unim cele două liste folosind operatorul +
lista_unita = lista1 + lista2
print("Lista unită:", lista_unita)
# Sortăm și afișăm lista unita
lista_unita.sort()
print("Lista unită sortată:", lista_unita)
# Funcție pentru a muta numărul 0 la începutul listei
def muta_zero_la_inceput(lista):
    if 0 in lista:
        lista.remove(0)  # Scoatem 0 din listă
        print(lista)
        lista.insert(0, 0)  # Inserăm 0 la începutul listei
        print(lista)
    return lista
# Mutăm numărul 0 la începutul listei folosind funcția
lista_unita = muta_zero_la_inceput(lista_unita)
print("Lista după mutarea numărului 0 la început:", lista_unita)
"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
●	Lista este goală.
●	Lista nu este goală.
"""
# Declarăm cele două liste
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# Unim cele două liste folosind operatorul +
lista_unita = lista1 + lista2
print("Lista unită:", lista_unita)
# Verificăm dacă lista este goală sau nu folosind un if
if not lista_unita:
    print("Lista este goală.")
else:
    print("Lista nu este goală.")
"""
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
"""
# Declarăm cele două liste
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# Unim cele două liste folosind operatorul +
lista_unita = lista1 + lista2
print("Lista unită înainte de ștergere:", lista_unita)
# Definim o funcție care să șteargă conținutul unei liste
def sterge_lista(lista):
    lista.clear()
# Folosim funcția pentru a șterge lista unita
sterge_lista(lista_unita)
print("Lista unită după ștergere:", lista_unita)
"""
7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
"""
if not lista_unita:
    print("Lista este goală.")
else:
    print("Lista nu este goală.")
"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
"""
# Dicționarul dat
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# Definim funcția pentru a afișa cheile dicționarului
def afiseaza_elevi(dictionar):
    chei = dictionar.keys()
    for elev in chei:
        print(elev)
# Apelăm funcția cu dicționarul dat
afiseaza_elevi(dict1)
"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""
# Dicționarul dat
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# Iterăm prin cheile dicționarului și afișăm numele elevilor și notele lor
for elev, nota in dict1.items():
    print(f"{elev} a luat nota {nota}")
"""
10. Dorel a făcut contestație și a primit 6
●	Modifică nota lui Dorel în 6
●	Printează nota după modificare
"""
# Dicționarul dat
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# Modificăm nota lui Dorel în 6
dict1['Dorel'] = 6
# Printăm nota lui Dorel după modificare
print(f"Nota lui Dorel după modificare este: {dict1['Dorel']}")
"""
11. Gigel se transferă din clasă
●	Căuta o funcție care să îl șteargă
●	Vine un coleg nou. Adaugă Ionică, cu nota 9
●	Printează noii elevi
"""
# Dicționarul dat
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# 1. Ștergem pe Gigel din dicționar
dict1.pop('Gigel', None)
# 2. Adăugăm pe Ionică cu nota 9
dict1.update({'Ionică': 9})
# Printăm noii elevi
print("Noii elevi sunt:", list(dict1.keys()))
"""
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
●	Adaugă în zilele_sapt ‘luni’
●	Afișează zile_sapt
"""
# Seturile date
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# Adăugăm 'luni' în zile_sapt
zile_sapt.add('luni')
# Afișăm zile_sapt după adăugare
print("Zilele săptămânii după adăugare:", zile_sapt)
"""
14.Folosește un if și verifică dacă:
●	Weekend este un subset al zilelor din săptămânii.
●	Weekend nu este un subset al zilelor din săptămânii.
"""
# Seturile date
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# Verificăm dacă weekend este subset al zilelor din săptămână
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămână.")
else:
    print("Weekend nu este un subset al zilelor din săptămână.")
"""
15. Afișează diferențele dintre aceste 2 seturi.
"""
# Seturile date
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# Afișăm diferența dintre zile_sapt și weekend
diferenta = zile_sapt - weekend
print("Diferența dintre zile_sapt și weekend este:", diferenta)
# Alternativ, putem folosi metoda difference()
diferenta_alt = zile_sapt.difference(weekend)
print("Diferența folosind metoda difference():", diferenta_alt)
"""
16. Afișează intersecția elementelor din aceste 2 seturi.
"""
# Seturile date
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# Afișăm intersecția dintre zile_sapt și weekend
intersectie = zile_sapt & weekend
print("Intersecția dintre zile_sapt și weekend este:", intersectie)
# Alternativ, putem folosi metoda intersection()
intersectie_alt = zile_sapt.intersection(weekend)
print("Intersecția folosind metoda intersection():", intersectie_alt)