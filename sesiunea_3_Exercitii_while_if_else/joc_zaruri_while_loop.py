"""
loop - while
"""
import random

while True:
    # Generarea unui număr aleatoriu între 1 și 6 (simulând aruncarea unui zar)
    dice_roll = random.randint(1, 6)
    # Citirea numărului ghicit de la utilizator
    numar_ghicit = int(input("Ghicește numărul aruncat de zar (între 1 și 6): "))
    # Verificarea și afișarea rezultatului
    if numar_ghicit < dice_roll:
        print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
    elif numar_ghicit > dice_roll:
        print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
    else:
        print(f"Ai ghicit. Felicitări! Ai ales {numar_ghicit} și zarul a fost {dice_roll}.")

    # Verificăm dacă jucătorul dorește să continue sau să încheie jocul
    raspuns = input("Dorești să reiei jocul? (da/nu): ")
    if raspuns.lower() != 'da':
        print("La revedere! Mulțumim pentru joc.")
        break

"""
Varianta care restrictioneaza gresirea intervalului si scrierea gresita: 
loop while in alt loop while
Această implementare asigură că utilizatorul poate introduce doar răspunsuri valide 
și cere reîncercarea în cazul în care un răspuns incorect este introdus.
"""
import random

while True:
    # Generarea unui număr aleatoriu între 1 și 6 (simulând aruncarea unui zar)
    dice_roll = random.randint(1, 6)

    # Citirea și validarea numărului ghicit de la utilizator
    while True:
        numar_ghicit = input("Ghicește numărul aruncat de zar (între 1 și 6): ")
        if numar_ghicit.isdigit() and 1 <= int(numar_ghicit) <= 6:
            numar_ghicit = int(numar_ghicit)
            break
        else:
            print("Te rog să introduci un număr valid între 1 și 6.")

    # Verificarea și afișarea rezultatului
    if numar_ghicit < dice_roll:
        print(f"Ai pierdut. Ai ales un număr mai mic. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
    elif numar_ghicit > dice_roll:
        print(f"Ai pierdut. Ai ales un număr mai mare. Ai ales {numar_ghicit} dar a fost {dice_roll}.")
    else:
        print(f"Ai ghicit. Felicitări! Ai ales {numar_ghicit} și zarul a fost {dice_roll}.")

    # Validarea răspunsului pentru continuarea jocului
    while True:
        raspuns = input("Dorești să reiei jocul? (da/nu): ").lower()
        if raspuns in {'da', 'nu'}:
            break
        else:
            print("Te rog să răspunzi cu 'da' sau 'nu'.")

    # Verificăm dacă jucătorul dorește să continue sau să încheie jocul
    if raspuns == 'nu':
        print("La revedere! Mulțumim pentru joc.")
        break
