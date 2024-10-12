"""
3.	Declara un string care contine toate literele alfabetului. Folosind functia enumerate, care primește
ca si parametru o colecție (lista, tupla, string) si returnează un iterator, afișează pentru fiecare litera în parte:
`Pe mine ma cheama X si sunt a n-a litera din alfabet`
Nu uite sa gestionezi cazurile speciale (prima litera etc)
"""
# 1. Declarația unui string cu toate literele alfabetului
alfabet = "abcdefghijklmnopqrstuvwxyz"

# 2. Iterația prin litere folosind enumerate
print("Iterarea prin literele alfabetului:")
for index, letter in enumerate(alfabet, start=1):
    # Determinăm cazul special pentru prima literă
    if index == 1:
        print(f"Pe mine mă cheamă {letter} și sunt prima literă din alfabet.")
    else:
        print(f"Pe mine mă cheamă {letter} și sunt a {index}-a literă din alfabet.")


"""
Explicația codului:
Declarația stringului: Am definit un string alfabet care conține toate literele mici ale alfabetului englez.
Funcția enumerate(): Această funcție este utilizată pentru a itera prin stringul de litere. enumerate() 
returnează un iterator care oferă atât indexul (începând de la 1) cât și litera corespunzătoare din string.
Gestionarea cazurilor speciale: Am inclus o verificare pentru a vedea dacă indexul este 1. Dacă da, se afișează 
un mesaj special pentru prima literă; pentru celelalte litere, se afișează un mesaj standard.
"""