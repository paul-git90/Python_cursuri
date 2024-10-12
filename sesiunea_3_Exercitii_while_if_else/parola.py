"""
Input parola fara a se vedea
"""
import getpass
# Citirea numelui de utilizator de la tastatură
user = input("Introduceți numele de utilizator: ")
# Citirea parolei de la tastatură folosind getpass pentru a ascunde caracterele introduse
parola = getpass.getpass("Introduceți parola: ")
# Crearea măștii parolei
masca_parola = '*' * len(parola)
# Afișarea mesajului
print(f"Parola pt user {user} este {masca_parola} și are {len(parola)} caractere")
