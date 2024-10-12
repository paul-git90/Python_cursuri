def afiseaza_fotbalisti(**kwargs): # definim functia afiseaza_fotbalisti() cu parametri cheie: valoare indefiniti
    for key_echipa, value_echipa in kwargs.items(): # ne vom folosi de structura repetitiva for si de variabilele key_echipa, value_echipa pentru a prelua date din parametrii cheie: valoare definiti in momentul apelarii functiei. Vom itera prin param cu ajutorul functiei items()
        for key_jucator, value_jucator in value_echipa.items(): # ne vom folosi de structura repetitiva for si de variabilele key_jucator, value_jucator pentru a prelua date din value_echipa - care de fapt este un dict. Vom itera prin dict cu ajutorul functiei items()
            print(f"La echipa {key_echipa} joaca jucatorul: {key_jucator} ") #afisam pentru fiecare key_echipa mesajul notat in string, iar in cadrul mesajului accesam datele din variabilele key_echipa si key_jucator
            for key_detalii_jucator, value_detalii_jucator in value_jucator.items(): #ne vom folosi de structura repetitiva for si de variabilele key_detalii_jucator, value_detalii_jucator pentru a prelua date din value_jucator - care de fapt este un dict. Vom itera prin dict cu ajutorul functiei items()
                print("Detalii jucator:", f"{key_detalii_jucator}:{value_detalii_jucator}", end="; ")
                #print(f"Detalii jucator: {key_detalii_jucator}:{value_detalii_jucator}", end="; ") #afisam pentru fiecare key_jucator mesajul notat in string, iar in cadrul mesajului accesam datele din variabilele key_detalii_jucator si value_detalii_jucator
            print('\n---------')

fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": {
            "Nume": "Nicole Dica",
            "Numar Tricou": 10
        },
        "Micu": {
            "Nume": "Tudor Micu",
            "Numar Tricou": 9
        },
        "Toader": {
            "Nume": "Tot Toader",
            "Numar Tricou": 1
        }
    },
    "Madrid": {
        "Matei": {
            "Nume": "Matei Tudose",
            "Numar Tricou": 11
        },
        "Vlad": {
            "Nume": "Vlad George",
            "Numar Tricou": 7
        },
        "Ion": {
            "Nume": "Ioan Ion",
            "Numar Tricou": 8
        }
    }
}
afiseaza_fotbalisti(**fotbalisti_pe_echipe) #apelam functia afiseaza_fotbalistii() si vom da dictionarl fotbalisti_pe_echipe ca parametru a-l functiei, iar caracterele ** inseamna despachetarea dictionarului pentru scoaterea elementelor in interiorul lor

afiseaza_fotbalisti(**{"Bucuresti": {"Dica": {"Nume": "Nicole Dica", "Numar Tricou": 10}}})#apelam functia afiseaza_fotbalistii() si vom defini dictionarul direct ca parametru. Ne folosim de ** pentru a despacheta dictionarul astfel putem pentru scoaterea elementelor in interiorul lui

