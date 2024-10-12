import json
import csv

lista_randuri = []
with open("Docs/elevi.csv", "r") as csv_file:
    dict_reader = csv.DictReader(csv_file)
    for rand in dict_reader:
        lista_randuri.append(rand)
    print(lista_randuri)

with open("Docs/elevi.json", "w") as json_file:
    json.dump(lista_randuri, json_file, indent=4)
