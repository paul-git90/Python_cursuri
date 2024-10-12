"""
22. Avand stringul '5132486790'
●	Afișează doar numerele pare
●	Afișează doar numerele impare
"""
# Pentru a afișa doar numerele pare și impare din șirul dat, putem utiliza o buclă for pentru a itera
# prin fiecare caracter din șir și apoi verifica dacă caracterul este un număr par sau impar.
sir = '5132486790'
# Afișarea numerelor pare:
numere_pare = [c for c in sir if int(c) % 2 == 0]
print("Numerele pare:", ''.join(numere_pare))
# Afișarea numerelor impare:
numere_impare = [c for c in sir if int(c) % 2 != 0]
print("Numerele impare:", ''.join(numere_impare))