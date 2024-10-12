# Citirea totalului cosului de cumparaturi de la tastatura
total_cos = float(input("Introduceți totalul coșului de cumpărături: "))

# Calcularea pretului dupa aplicarea reducerii
if 100 <= total_cos < 200:
    reducere = 10 / 100
    print(f'Reducerea este de 10%')
elif 200 <= total_cos < 300:
    reducere = 15 / 100
    print(f'Reducerea este de 15%')
elif 300 <= total_cos < 400:
    reducere = 20 / 100
    print(f'Reducerea este de 20%')
elif total_cos >= 400:
    reducere = 30 / 100
    print(f'Reducerea este de 30%')
else:
    reducere = 0
    print(f'Fara reducere.')

pret_final = total_cos * (1 - reducere)
# Afisarea pretului final
print(f"Prețul final după aplicarea reducerii este: {pret_final:.3f} lei")
