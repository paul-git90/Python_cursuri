## 📌 Interactiunea cu fisiere csv
- CSV = Coma Separated Values
- Fisierele CSV sunt fisiere structurate sub forma tabelara
  (excel), unde valorile coloanelor sunt separate prin virgula.

```python
import csv

with open("csv/path_to_csv_file.csv", "w") as file:
  writer = csv.writer(file)

  writer.writerow(['id', 'nume'])  # cream header-ul
  writer.writerow([1, 'Paula'])
  writer.writerow([2, 'Ana'])
```

```python
import csv

with open("csv/path_to_csv_file.csv", "r") as file:
  reader = csv.reader(file)

  # read a row at a time
  row = next(reader)

  # read the next rows using a for loop
  for row in reader:
    print(row)
```

```python
import csv

with open('csv/path_to_csv_file.csv', 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row)
```