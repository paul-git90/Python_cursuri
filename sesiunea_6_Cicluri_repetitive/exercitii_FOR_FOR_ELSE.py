"""
Exercitii din cursul Cicluri Repetitive
#  FOR/FOR ELSE - executam codul de un anumit numar de ori
"""

"""
EX3: Afiseaza toate numerele pare pana la 10.
"""
# Iterăm prin numerele de la 0 la 10

for numar in range(0, 11):
    # Verificăm dacă numărul este par
    if numar % 2 == 0:
        print(numar)

"""
EX4: Se da lista:
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
Afiseaza toate elementele din lista accesandu-le dupa index.
"""

# Lista de legume
legume = ['spanac', 'castraveti', 'conopida', 'ardei']

# Iterăm prin toți indexii listei folosind range(len(legume))

for i in range(len(legume)):
    # Afișăm elementul de la indexul i
    print(legume[i])
