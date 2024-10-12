"""
Context Managers

EX5: Implementeaza un context manager care va masura si va afisa
durata de executie a codului executat.
"""
import time


class DurataDeExecuteCM:
    def __enter__(self):
        self.moment_de_start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        moment_de_final = time.time()
        durata = moment_de_final - self.moment_de_start
        print(f"Durata de executie este: {durata}")


with DurataDeExecuteCM():
    for number in range(1, 500):
        print(number)
