import csv
import os

if not os.path.exists("Docs"):  # verifica directorul
    os.makedirs("Docs")  # creaza directoare

# todo Create a file de tip .csv
with open("Docs/elevi.csv", "w", newline="") as csv_file:
    rand = csv.writer(csv_file)
    rand.writerow(["id", "first_name", "second_name", "age", "grade"])
    rand.writerow(["1", "Maria", "Popescu", "25", "9"])
    rand.writerow(["2", "Sergiu", "Nicoara", "22", "8"])
    rand.writerow(["3", "Filip", "Marian", "24", "6.70"])
    rand.writerow(["4", "Barbuta", "Paul", "20", "9.90"])
    rand.writerow(["5", "Mihai", "Roxana", "19", "10"])
    rand.writerow(["6", "Mayer", "Veronica", "24", "8.50"])

with open("Docs/elevi.csv", "r") as csv_file:
    citim = csv.reader(csv_file)
    header = next(citim)
    print(f"{header[0]:4}{header[1]:12}{header[2]:14}{header[3]:6}{header[4]:0}")
    print("-----"*10)
    for rand in citim:
        print(f"{rand[0]:4}{rand[1]:12}{rand[2]:14}{rand[3]:6}{rand[4]:0}")
