"""
Decoratorii în Python sunt un mod elegant de a adăuga funcționalități suplimentare funcțiilor sau metodelor existente,
fără a modifica codul lor original. Aceștia reprezintă un design pattern care permite "decorarea" unei funcții cu un
comportament suplimentar, într-o manieră flexibilă și reutilizabilă.

Cum funcționează decoratorii?
Un decorator este o funcție care primește o funcție ca argument și returnează o nouă funcție, adăugând comportament
suplimentar la funcția originală. Aceasta permite extensia comportamentului unei funcții existente, fără a modifica
corpul său.

Sintaxa decoratorilor:
În Python, decorarea unei funcții se face folosind simbolul @ urmat de numele decoratorului, plasat deasupra definiției
funcției.
"""
"""
@decorator_function
def some_function():
    pass
"""
# Aceasta este echivalentă cu:
"""
def some_function():
    pass

some_function = decorator_function(some_function)
"""
"""
Exemple simple:
Un exemplu clasic de decorator este cel care loghează apelurile unei funcții.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Funcția {func.__name__} a fost apelată cu argumentele {args} și {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@logger
def adunare(a, b):
    return a + b

# Testare
print(adunare(2, 3))

"""
Explicație:
logger(func): Acesta este decoratorul. Primește funcția adunare ca argument.
wrapper(*args, **kwargs): O funcție internă care va înlocui funcția originală. Aici putem adăuga comportament 
suplimentar (în acest caz, logarea).
func(*args, **kwargs): Aceasta apelează funcția originală cu toate argumentele primite.
@logger: Aplică decoratorul logger funcției adunare.
Atunci când apelăm funcția adunare(2, 3), rezultatul este următorul:
"""
"""
Decoratori pentru metode din clase:
Decoratorii pot fi folosiți și pentru metode în clase, iar @staticmethod și @classmethod sunt exemple clasice de 
decoratori în Python.
"""


class MyClass:
    @staticmethod
    def my_static_method():
        print("Aceasta este o metodă statică")

# Apelare
MyClass.my_static_method()

"""
Decoratori cu parametri:
Decoratorii pot primi, la rândul lor, parametri, ceea ce face posibilă personalizarea lor.

Exemplu de decorator cu parametri:
"""


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def salut():
    print("Salut!")


# Testare
salut()

# Acest decorator repeat(n) apelează funcția salut de 3 ori:

"""
Utilizări comune ale decoratorilor:
Logare: Decoratorii pot fi folosiți pentru a loga informații despre apelurile funcțiilor.
Validare: Pot verifica dacă argumentele unei funcții sunt valide.
Cache/ Memorare: Pot salva rezultatele unor funcții costisitoare în cache, pentru a evita calcule repetitive.
Autentificare: Decoratorii sunt folosiți frecvent pentru verificarea autentificării în aplicațiile web.
Decoratorii în Python intern:
Python vine deja cu câțiva decoratori built-in foarte utili, cum ar fi:

@staticmethod: Definirea unei metode static în clase, care nu necesită o instanță a clasei.
@classmethod: Definește o metodă de clasă, care primește ca prim argument clasa însăși în loc de o instanță.
@property: Folosit pentru a crea atribute calculabile din metode.

Exemplu cu @property:
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2


# Testare
c = Circle(5)
print(c.area)  # Afișează aria cercului fără a apela ca o funcție

"""
Decoratorii profită de faptul că în Python, funcțiile sunt obiecte de primă clasă, ceea ce înseamnă că pot fi 
pasate ca argumente și returnate din alte funcții. Decoratorul în sine este o funcție care returnează o altă funcție 
(wrapper-ul) ce înlocuiește funcția originală. Wrapper-ul poate executa cod suplimentar înainte și după apelarea 
funcției originale.

Avantajele decoratorilor:
Reutilizare a codului: Funcționalitățile comune (cum ar fi logarea sau autentificarea) pot fi centralizate și aplicate 
ușor la mai multe funcții.
Modificare fără alterare: Permit adăugarea de noi funcționalități la o funcție fără a modifica codul acesteia.
Cod mai curat: Separă preocupările (concerns), menținând funcțiile clare și focalizate pe ceea ce trebuie să facă.
"""