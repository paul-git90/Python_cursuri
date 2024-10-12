# 📌 Chain of Responsibility Design Pattern
Chain of Responsibility este un pattern comportamental care permite trimiterea unei cereri printr-o serie de obiecte, 
fiecare având o oportunitate de a gestiona cererea. Fiecare obiect din lanț decide fie să proceseze cererea, fie să o 
transmită mai departe la următorul obiect din lanț. Acest pattern ajută la decuplarea emitentului cererii de obiectele 
care o prelucrează.

## 📌 Principii Logice de Funcționare
Decuplare: Emitentul cererii nu trebuie să știe cine va prelucra cererea. Acesta este decuplat de handlerii care pot 
procesa cererea.

Flexibilitate: Orice handler din lanț poate alege să proceseze cererea sau să o transmită mai departe. Aceasta permite 
adăugarea sau eliminarea de handleri fără a afecta restul sistemului.

Ordine de Procesare: Handlerii pot fi organizați într-un lanț, iar ordinea în care aceștia procesează cererea poate fi 
controlată.

## 📌 Când se Folosește
Tratarea Cererilor: Când un sistem trebuie să proceseze cereri de la utilizatori, iar cererile pot fi gestionate de mai 
multe clase diferite.
Evenimente: În aplicațiile GUI, unde evenimentele pot fi gestionate de diverse componente.
Domenii: Este utilizat frecvent în aplicațiile de tip server, gestionarea evenimentelor, și în procesele de business.
Exemple de Cod
1. ## 📌 Exemplu cu Complexitate Foarte Mică
Acest exemplu ilustrează conceptul de bază al pattern-ului Chain of Responsibility.
```python
class Handler:
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return f"Handler A processed request {request}"
        else:
            return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return f"Handler B processed request {request}"
        else:
            return super().handle(request)

# Client Code
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_a.set_next(handler_b)

print(handler_a.handle("A"))  # Output: Handler A processed request A
print(handler_a.handle("B"))  # Output: Handler B processed request B
print(handler_a.handle("C"))  # Output: None
```
2. ## 📌 Exemplu cu Complexitate Medie
Acest exemplu arată cum să tratăm diverse tipuri de cereri printr-un sistem de suport tehnic.
```python
class SupportHandler:
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)

class LevelOneSupport(SupportHandler):
    def handle(self, request):
        if request == "Basic issue":
            return "Level 1: Basic issue handled"
        else:
            return super().handle(request)

class LevelTwoSupport(SupportHandler):
    def handle(self, request):
        if request == "Intermediate issue":
            return "Level 2: Intermediate issue handled"
        else:
            return super().handle(request)

class LevelThreeSupport(SupportHandler):
    def handle(self, request):
        if request == "Complex issue":
            return "Level 3: Complex issue handled"
        else:
            return super().handle(request)

# Client Code
level_one = LevelOneSupport()
level_two = LevelTwoSupport()
level_three = LevelThreeSupport()

level_one.set_next(level_two).set_next(level_three)

print(level_one.handle("Basic issue"))  # Output: Level 1: Basic issue handled
print(level_one.handle("Intermediate issue"))  # Output: Level 2: Intermediate issue handled
print(level_one.handle("Complex issue"))  # Output: Level 3: Complex issue handled
print(level_one.handle("Unknown issue"))  # Output: None
```
3. ## 📌 Exemplu cu Complexitate Mare
Acest exemplu arată cum putem trata cererile de procesare a plăților prin diverse metode, 
cum ar fi cardul de credit sau PayPal.
```python
class PaymentHandler:
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)

class CreditCardHandler(PaymentHandler):
    def handle(self, request):
        if request['type'] == 'credit_card':
            return f"Processed payment of {request['amount']} using Credit Card"
        else:
            return super().handle(request)

class PayPalHandler(PaymentHandler):
    def handle(self, request):
        if request['type'] == 'paypal':
            return f"Processed payment of {request['amount']} using PayPal"
        else:
            return super().handle(request)

class BankTransferHandler(PaymentHandler):
    def handle(self, request):
        if request['type'] == 'bank_transfer':
            return f"Processed payment of {request['amount']} using Bank Transfer"
        else:
            return super().handle(request)

# Client Code
credit_card_handler = CreditCardHandler()
paypal_handler = PayPalHandler()
bank_transfer_handler = BankTransferHandler()

credit_card_handler.set_next(paypal_handler).set_next(bank_transfer_handler)

payment_requests = [
    {'type': 'credit_card', 'amount': 100},
    {'type': 'paypal', 'amount': 200},
    {'type': 'bank_transfer', 'amount': 300},
    {'type': 'unknown', 'amount': 400}
]

for request in payment_requests:
    print(credit_card_handler.handle(request))
```
## 📌 Concluzie
Chain of Responsibility Design Pattern este un instrument util pentru a gestiona cereri printr-un lanț de handleri, 
oferind flexibilitate și decuplare între emitentul cererii și handlerii care o procesează. Acesta este esențial în 
aplicațiile complexe, cum ar fi cele de gestionare a evenimentelor sau cele care necesită tratarea cererilor de la 
utilizatori.
