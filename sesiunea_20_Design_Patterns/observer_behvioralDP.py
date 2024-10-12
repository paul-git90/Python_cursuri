"""
Pattern care permite definirea unui mecanism de observare intre obiecte, ce permite trimiterea de notificari
obiectelor "observator" (observer) despre evenimentele noi ale obiectlui "observabil" (observable)
"""


class ObservablePerson:
    name = "Default User"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f"I am {self.name}"

    def register_observer(self, observer):
        # inregistram un observer
        self._observers.append(observer)

    def notify_observers(self, message):
        # fiecare Observer este notificat
        # prin apelul functiei notify din clasa Observer
        for obs in self._observers:
            obs.notify(self, message)


class Observer:
    def __init__(self, name, observable):
        # in momentul instantierii Observerului, acesta este
        # inregistrat in lista de observeri ai obiectului Observable
        self.name = name
        observable.register_observer(self)

    def notify(self, observable, message):
        print(f"Observer: {self.name} Got message: {message}")
        print(f" from observable obj: {observable}")


subject = ObservablePerson()
observer_obj1 = Observer("obs1", subject)
observer_obj2 = Observer("obs2", subject)

# in momentul apelului ambele obiecte observer primesc notificare
subject.notify_observers("An event occured....")
