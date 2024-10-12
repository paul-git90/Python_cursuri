import time
from datetime import datetime
# todo: cifrele apar doar pe jumatate, trebuie corectat


def formateaza_ora(ora, minute, secunde):
    # Mapa pentru cifrele ce vor fi afișate
    digit_map = {
        '0': ["  _  ", " | | ", " |_| "],
        '1': ["     ", "   | ", "   | "],
        '2': ["  _  ", "  _| ", " |_  "],
        '3': ["  _  ", "  _| ", "  _| "],
        '4': ["     ", " | | ", " |_| "],
        '5': ["  _  ", " |_  ", "  _| "],
        '6': ["  _  ", " |_  ", " |_| "],
        '7': ["  _  ", "   | ", "   | "],
        '8': ["  _  ", " |_| ", " |_| "],
        '9': ["  _  ", " |_| ", "  _| "],
        ':': ["     ", "  o  ", "     "]  # Separator
    }

    lines = ["", "", ""]  # Trei linii pentru a forma fiecare cifră

    for digit in f"{ora:02}:{minute:02}:{secunde:02}":
        if digit in digit_map:  # Verifică dacă digitul există în digit_map
            for i in range(3):
                lines[i] += digit_map[digit][i] + " "  # Adaugă cifrele formatate
        else:
            # Adaugă un spațiu gol pentru digituri care nu sunt în digit_map
            for i in range(3):
                lines[i] += "     "  # Cifre nevalide

    return "\n".join(lines)


def afiseaza_ceas():
    while True:
        now = datetime.now()  # Obține ora curentă
        ora = (now.hour + 3) % 24  # Ora București (UTC+3), asigură că e între 0-23
        minute = now.minute
        secunde = now.second

        # Formatează ora pentru afișare
        afisaj = formateaza_ora(ora, minute, secunde)

        # Afișează ora
        print(afisaj, end='\r')

        # Așteaptă 1 secundă
        time.sleep(1)


if __name__ == "__main__":
    afiseaza_ceas()
