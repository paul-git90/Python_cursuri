# 📌 Adapter Design Pattern
Adapter Design Pattern este un pattern structural care permite interacțiunea între două interfețe incompatibile. 
Acesta acționează ca un adaptor, convertind interfața unei clase într-o interfață care este acceptată de clientul 
care utilizează un obiect. Adapter-ul facilitează colaborarea între clase care, în mod normal, nu ar putea funcționa 
împreună din cauza diferențelor în interfețele lor.

## 📌 Principii Logice de Funcționare
Compatibilitate între Interfețe: Adapter permite ca clasele cu interfețe incompatibile să colaboreze, făcându-le să 
comunice între ele fără a schimba codul existent.

Separarea Implementării: Adapter-ul acționează ca un intermediar, astfel încât modificările în implementarea unei 
clase să nu afecteze utilizatorii care depind de o interfață specifică.

Ușurința în Extensibilitate: Datorită modului în care sunt structurate clasele, este simplu să se adauge noi clase 
sau să se modifice cele existente fără a afecta codul clientului.

## 📌 Când se Folosește
Integrarea de Biblioteci Externe: Când integrezi o bibliotecă terță parte care nu respectă interfețele tale.
Refactorizarea Codului: Dacă ai clase vechi care trebuie să fie utilizate cu noi clase care au interfețe diferite.
Domenii: Acest pattern este frecvent utilizat în dezvoltarea de software pentru a facilita colaborarea între diferite componente, cum ar fi în aplicațiile web, software-ul de afaceri și aplicațiile mobile.
Exemple de Cod
1. ## 📌 Exemplu cu Complexitate Foarte Mică
Acesta este un exemplu simplu care arată cum funcționează Adapter-ul.
```python
class Target:
    def request(self):
        return "Default target request"

class Adaptee:
    def specific_request(self):
        return "Specific request from Adaptee"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request()

# Client Code
adaptee = Adaptee()
adapter = Adapter(adaptee)

print(adapter.request())  # Output: Specific request from Adaptee
```
2. ## 📌 Exemplu cu Complexitate Medie
Acest exemplu ilustrează cum putem adapta diferite tipuri de aplicații de plată pentru a le face să lucreze cu un 
sistem existent.
```python
class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError("You should implement this method!")

class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

# Legacy class with incompatible interface
class OldPaymentSystem:
    def make_payment(self, amount):
        return f"Payment of {amount} processed through Old System"

# Adapter for OldPaymentSystem
class OldPaymentAdapter(PaymentProcessor):
    def __init__(self, old_payment_system):
        self.old_payment_system = old_payment_system

    def pay(self, amount):
        return self.old_payment_system.make_payment(amount)

# Client Code
paypal = PayPalPayment()
credit_card = CreditCardPayment()
old_payment_system = OldPaymentSystem()
adapter = OldPaymentAdapter(old_payment_system)

print(paypal.pay(100))  # Output: Paid 100 using PayPal
print(credit_card.pay(200))  # Output: Paid 200 using Credit Card
print(adapter.pay(300))  # Output: Payment of 300 processed through Old System
```
3. ## 📌 Exemplu cu Complexitate Mare
Acest exemplu arată cum putem adapta diferite tipuri de medii de comunicare pentru a le integra într-o aplicație care 
le folosește.
```python
class EmailService:
    def send_email(self, message):
        return f"Email sent with message: {message}"

class SMSService:
    def send_sms(self, message):
        return f"SMS sent with message: {message}"

class NotificationService:
    def notify(self, message):
        raise NotImplementedError("You should implement this method!")

# Adapter for EmailService
class EmailAdapter(NotificationService):
    def __init__(self, email_service):
        self.email_service = email_service

    def notify(self, message):
        return self.email_service.send_email(message)

# Adapter for SMSService
class SMSAdapter(NotificationService):
    def __init__(self, sms_service):
        self.sms_service = sms_service

    def notify(self, message):
        return self.sms_service.send_sms(message)

# Client Code
email_service = EmailService()
sms_service = SMSService()

email_adapter = EmailAdapter(email_service)
sms_adapter = SMSAdapter(sms_service)

print(email_adapter.notify("Hello via Email!"))  # Output: Email sent with message: Hello via Email!
print(sms_adapter.notify("Hello via SMS!"))  # Output: SMS sent with message: Hello via SMS!
```
## 📌 Concluzie
Adapter Design Pattern este un instrument foarte util pentru a face interfețele incompatibile să colaboreze între ele. 
Prin utilizarea acestui pattern, dezvoltatorii pot îmbunătăți modularitatea, extinderea și testabilitatea codului. 
Acesta este esențial în aplicațiile care necesită integrarea diverselor componente sau biblioteci externe care nu se 
potrivesc în mod natural.
