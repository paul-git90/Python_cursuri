# 📌 Factory Method este un pattern de design creational care se concentrează pe crearea de obiecte. 
Acesta permite unei clase să-și lase instanțierea subclaselor să decidă care obiect să fie creat. 
Iată o explicație detaliată a acestui pattern, împreună cu exemple de cod de diferite complexități.
## 📌 Principii Logice de Funcționare
Separația Creării Obiectelor: 
Factory Method separă procesul de instanțiere al obiectelor de logica de 
utilizare a acestora. Acest lucru permite o mai bună organizare a codului și o flexibilitate crescută.
Substituibilitate: 
Factory Method permite substituirea tipurilor de obiecte fără a schimba codul clientului. 
Poți crea tipuri diferite de obiecte prin extensie.
Îmbunătățirea Testabilității: 
Prin separarea creării obiectelor, poți folosi mock-uri sau stub-uri în timpul testării, 
ceea ce facilitează testarea unităților de cod.
## 📌 Când se Folosește
Crearea de Obiecte Complexe: 
Când instanțierea unui obiect implică mai mulți pași sau condiții.
Când trebuie să schimbi tipurile de obiecte: 
Dacă ai o aplicație care poate folosi mai multe tipuri de obiecte în funcție de configurări externe, 
Factory Method este o alegere bună.
## 📌 Domenii: Este frecvent folosit în domeniul dezvoltării software, cum ar fi jocuri, aplicații desktop, aplicații web, etc.
Exemple de Cod
1. ## 📌 Exemplu cu Complexitate Foarte Mică
Acesta este un exemplu simplu care ilustrează cum funcționează Factory Method.
```python
class Product:
    def use(self):
        return "Using product"

class Factory:
    def create_product(self):
        return Product()

# Client Code
factory = Factory()
product = factory.create_product()
print(product.use())  # Output: Using product
```
2. ## 📌 Exemplu cu Complexitate Medie
Acest exemplu arată cum putem crea diferite tipuri de produse folosind Factory Method.
```python
class Shape:
    def draw(self):
        raise NotImplementedError("You should implement this method!")

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")

# Client Code
factory = ShapeFactory()
shapes = [factory.create_shape("circle"), factory.create_shape("square")]

for shape in shapes:
    print(shape.draw())
# Output:
# Drawing a Circle
# Drawing a Square
```
3. ## 📌 Exemplu cu Complexitate Mare
Acest exemplu ilustrează un sistem de gestionare a diferitelor tipuri de notificări (e-mail, SMS, etc.) folosind Factory Method.
```python
class Notification:
    def send(self, message):
        raise NotImplementedError("You should implement this method!")

class EmailNotification(Notification):
    def send(self, message):
        return f"Sending Email: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"Sending Push Notification: {message}"

class NotificationFactory:
    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")

# Client Code
factory = NotificationFactory()
notifications = [
    factory.create_notification("email"),
    factory.create_notification("sms"),
    factory.create_notification("push"),
]

for notification in notifications:
    print(notification.send("Hello, this is a test message!"))
# Output:
# Sending Email: Hello, this is a test message!
# Sending SMS: Hello, this is a test message!
# Sending Push Notification: Hello, this is a test message!
```
## 📌 Concluzie
Factory Method este un pattern de design util pentru gestionarea complexității în crearea obiectelor. 
Acesta oferă o structură flexibilă, care permite extensibilitate și ușurință în testare. 
Folosirea acestui pattern este foarte benefică în aplicațiile mari, unde trebuie să gestionăm diverse 
tipuri de obiecte, fără a încărca codul clientului cu logica de instanțiere.