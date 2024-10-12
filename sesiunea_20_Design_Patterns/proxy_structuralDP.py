"""
Proxy DP = pattern care controleaza si administreaza accesul la obiectele pe care le protejeaza
"""

from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def drive(self):
        pass


class Car(AbstractCar):
    def drive(self):
        print("You are driving the car.")


class Driver:
    def __init__(self, age):
        self.age = age


class ProxyCar(AbstractCar):
    def __init__(self, driver: Driver):
        self.car = Car()
        self.driver = driver

    def drive(self):
        if self.driver.age < 18:
            print("Sorry little driver, you are too young to drive.")
        else:
            self.car.drive()


driver = Driver(16)
print(driver.age)
# Daca instantiem direct clasa Car,
# nu avem constrangere asupra varstei
car = Car()
car.drive()

# Așa ca nu instantiem direct Car, ci instantiem ProxyCar,
# aceasta verificand varsta soferului
proxy_car = ProxyCar(driver)
proxy_car.drive()

new_driver = Driver(20)
proxy_car = ProxyCar(new_driver)
proxy_car.drive()
