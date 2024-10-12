"""
3.	Context Managers
Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul,
folosind urmatoarele 2 metode:
-	try - finally
-	Fișierul se deschide înainte de try, folosind functia open
-	În interiorul try citim conținutul folosind functia read
-	În finally se închide fișierul
-	with (context manager)
-	Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context
managerul face asta pentru noi.
"""

"""
Metoda 1: Cu try-finally
În această metodă, deschidem fișierul cu funcția open(), citim conținutul și ne asigurăm 
că fișierul este închis corect, indiferent dacă apare sau nu o excepție, folosind blocul finally.

Pașii metodei try-finally:
Deschidem fișierul înainte de blocul try.
În blocul try, citim conținutul fișierului cu metoda read().
În blocul finally, închidem fișierul pentru a elibera resursele.
Codul pentru try-finally:
"""

# Metoda try-finally
try:
    # Deschidem fișierul
    f = open("hello.txt", "r")

    # Citim conținutul fișierului
    content = f.read()
    print(content)

finally:
    # Închidem fișierul în blocul finally
    f.close()

"""
Explicație:
Deschidere fișier (open): Deschidem fișierul hello.txt în modul de citire ("r").
Blocul try: În interiorul blocului, citim conținutul fișierului folosind metoda read().
Blocul finally: Indiferent dacă se întâmplă o eroare sau nu, în blocul finally închidem 
fișierul cu metoda close(), eliberând resursele.
"""

"""
Metoda 2: Cu with (Context Manager)
Această metodă utilizează un context manager (with), care are grijă să deschidă și să închidă fișierul automat. 
Când ieșim din blocul with, context managerul va închide fișierul pentru noi, fără să fie nevoie să apelăm 
explicit close().

Pașii metodei with:
Folosim with open() pentru a deschide fișierul.
În interiorul blocului with, citim fișierul folosind metoda read().
"""

# Metoda with (context manager)
with open("hello.txt", "r") as f:
    # Citim conținutul fișierului
    content = f.read()
    print(content)

"""
Explicație:
with open(): Deschide fișierul folosind un context manager. Când ieșim din blocul with, fișierul este închis automat.
Citirea fișierului (read()): În interiorul blocului with, citim conținutul fișierului la fel ca în prima metodă.
Fără închidere manuală: Nu mai este nevoie să apelăm close(), deoarece context managerul o face pentru noi.
"""

"""
Diferențele între cele două metode:
Control manual vs automat:

În metoda try-finally, este responsabilitatea noastră să închidem fișierul manual în blocul finally.
În metoda with, context managerul se ocupă de închiderea automată a fișierului.
Simplicitate:

Metoda with este mai simplă și mai concisă, deoarece elimină necesitatea unui bloc finally 
pentru închiderea fișierului.
De ce e preferat with?
Gestionarea automată a resurselor: Context managerul asigură eliberarea resurselor la sfârșitul 
blocului, chiar și în caz de excepție, reducând riscul de a uita să închidem un fișier.
"""
