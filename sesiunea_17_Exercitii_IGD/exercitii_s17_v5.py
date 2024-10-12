"""
5.	Decorators extra
Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator
`@require_login`
– o metoda logout, fara params, care delogheaza userul.

Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""


def require_login(func):
    def wrapper(self, *args, **kwargs):
        if not self.logged_in:
            print("Acces refuzat: utilizatorul nu este logat.")
            return None
        return func(self, *args, **kwargs)
    return wrapper


class User:
    def __init__(self, name, email, password, birthdate):
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.logged_in = False

    def login(self, email, password):
        if email == self.email and password == self.password:
            self.logged_in = True
            print(f"{self.name} s-a logat cu succes.")
        else:
            print("Email sau parolă incorectă.")

    @require_login
    def get_info(self):
        return {
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate
        }

    def logout(self):
        self.logged_in = False
        print(f"{self.name} s-a delogat cu succes.")

# Testare


# Crearea unui utilizator
user = User("Paul", "paul@example.com", "password123", "1990-01-01")

# Apelarea metodei get_info înainte de logare
print(user.get_info())  # Ar trebui să afișeze un mesaj de acces refuzat

# Logarea utilizatorului
user.login("paul@example.com", "password123")

# Apelarea metodei get_info după logare
info = user.get_info()
print(info)  # Ar trebui să afișeze informațiile despre utilizator

# Delogarea utilizatorului
user.logout()

# Apelarea metodei get_info după delogare
print(user.get_info())  # Ar trebui să afișeze un mesaj de acces refuzat

# Logarea utilizatorului din nou
user.login("paul@example.com", "password123")

# Apelarea metodei get_info după logare din nou
info = user.get_info()
print(info)  # Ar trebui să afișeze informațiile despre utilizator

"""
Explicație:
Decoratorul require_login:

Decoratorul primește funcția pe care o va decora (în acest caz, metoda get_info).
Verifică dacă utilizatorul este logat (prin atributul self.logged_in).
Dacă utilizatorul nu este logat, afișează un mesaj de acces refuzat și returnează None, 
împiedicând astfel executarea funcției decorate.
Dacă utilizatorul este logat, funcția decorată este apelată.
Clasa User:

Constructorul (__init__) inițializează atributele pentru nume, email, parolă, data nașterii și 
starea de logare (logged_in).
Metoda login primește email și parolă și verifică dacă acestea sunt corecte. Dacă da, setează 
logged_in la True.
Metoda get_info este decorată cu @require_login, ceea ce înseamnă că va permite accesul la 
informațiile utilizatorului doar dacă acesta este logat.
Metoda logout setează logged_in la False, indicând că utilizatorul s-a delogat.
Testare:

Se testează funcționalitatea prin apelarea metodei get_info înainte și după logare, și după 
delogare. Mesajele afișate confirmă funcționalitatea corectă a decoratorului și a metodelor clasei User.
"""
