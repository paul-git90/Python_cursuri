## 📌 JSON
- JSON = Javascript Object Notation
- Este un format tip text pentru stocare si transportare de date
- El este independent de orice limbaj de programare, toate il folosesc
- Suporta tipurile de date uzuale (str, int, float, list, dict)
- Arata si se comporta in cele mai multe cazuri ca un dictionar/lista

## 📌 Interactiunea cu fisiere JSON
```python
import json

def citire_din_fisier_json(cale_fisier):
    with open(cale_fisier, 'r') as file:
        return json.load(file)

print(citire_din_fisier_json("quiz.json"))
print(type(citire_din_fisier_json("quiz.json")))
```

```python
import json

def scriere_in_fisier_json(cale_fisier, randuri_informatii):
    with open(cale_fisier, 'w') as file:
        json.dump(randuri_informatii, file)
```