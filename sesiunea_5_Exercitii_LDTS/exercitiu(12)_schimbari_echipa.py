"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

●	Declară o Listă cu 5 jucători
●	Schimbari_efectuate = te joci tu cu valori diferite
●	Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
-	Efectuează schimbarea
-	Șterge jucătorul scos din listă
-	Adaugă jucătorul intrat
-	Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
-	Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
-	Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori
"""
# Declarăm lista cu 5 jucători
jucatori = ["jucator1", "jucator2", "jucator3", "jucator4", "jucator5"]

# Setăm valorile pentru schimbările efectuate și schimbările maxime
schimbari_efectuate = 0
schimbari_max = 3


def efectueaza_schimbare(jucatori, jucator_scos, jucator_intrat, schimbari_efectuate, schimbari_max):
    if schimbari_efectuate < schimbari_max:
        if jucator_scos in jucatori:
            jucatori.remove(jucator_scos)
            jucatori.append(jucator_intrat)
            schimbari_efectuate += 1
            print(f"A intrat {jucator_intrat}, a ieșit {jucator_scos}, mai ai {schimbari_max - schimbari_efectuate} schimbări.")
        else:
            print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator_scos} nu e în teren.")
            print(f"Mai ai {schimbari_max - schimbari_efectuate} schimbări.")
    else:
        print("Nu mai ai schimbări disponibile.")

    return schimbari_efectuate


# Testăm funcția cu diferite valori
schimbari_efectuate = efectueaza_schimbare(jucatori, "jucator1", "jucator6", schimbari_efectuate, schimbari_max)
schimbari_efectuate = efectueaza_schimbare(jucatori, "jucator2", "jucator7", schimbari_efectuate, schimbari_max)
schimbari_efectuate = efectueaza_schimbare(jucatori, "jucator10", "jucator8", schimbari_efectuate, schimbari_max)
schimbari_efectuate = efectueaza_schimbare(jucatori, "jucator3", "jucator9", schimbari_efectuate, schimbari_max)

# Afișăm lista finală de jucători
print("Lista finală de jucători:", jucatori)
