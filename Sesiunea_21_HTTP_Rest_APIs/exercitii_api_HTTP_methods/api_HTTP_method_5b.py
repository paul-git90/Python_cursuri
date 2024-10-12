"""
Dacă primești doar mesajul Process finished with exit code 0 și nimic altceva,
acest lucru sugerează că programul s-a executat fără erori, dar nu a printat nimic
din cauza fie a unei probleme de conectare la API, fie pentru că lista de todos returnată este goală.

Hai să îți sugerez câteva posibile soluții pentru a înțelege ce se întâmplă:

1. Verifică conexiunea și status-ul răspunsului
Asigură-te că serverul returnează un răspuns valid. Poți începe prin a verifica dacă codul de
status al răspunsului este 200 (care indică un răspuns de succes).

2. Verifică datele efective returnate
Poate fi cazul ca răspunsul să fie gol sau incomplet. Să adăugăm câteva print-uri suplimentare
pentru a vedea exact ce returnează API-ul și dacă există vreo problemă cu datele.
"""

import requests

# URL-ul de bază pentru todos
url = "https://jsonplaceholder.typicode.com/todos"

# Parametrii de filtrare (todos incomplete pentru userId=1)
params = {
    "userId": 1,        # filtram pentru utilizatorul cu id 1
    "completed": False  # vrem doar todos care nu sunt completate
}

# Facem request-ul cu parametrii de query
response = requests.get(url, params=params)

# Verificăm statusul răspunsului
print(f"Status code: {response.status_code}")  # Adaugă acest print pentru a vedea codul de status

if response.status_code == 200:
    todos_incomplete = response.json()

    # Debug: afișăm toate "todos" nefinalizate returnate de API pentru a verifica datele
    print(f"Response content: {todos_incomplete}")  # Afișăm întreaga listă de todos

    if todos_incomplete:  # Verificăm dacă lista nu este goală
        # Afișăm primele 3 todos nefinalizate, dacă există
        for todo in todos_incomplete[:3]:
            print(f"ID Todo: {todo['id']}, Titlu: {todo['title']}, Completat: {todo['completed']}")

        # Calculăm și afișăm câte todos nefinalizate rămân
        total_todos = len(todos_incomplete)
        if total_todos > 3:
            print(f"+{total_todos - 3} more todos incomplete.")
    else:
        print("No incomplete todos found.")
else:
    print(f"Error: {response.status_code}, message: {response.text}")

'''
Pași pentru diagnosticare:
Verifică codul de status: Dacă nu este 200, API-ul nu răspunde corect.
Verifică conținutul răspunsului: Afișează ce returnează API-ul pentru a vedea dacă lista este goală.
Verifică dacă există todos nefinalizate: Codul actual verifică dacă sunt elemente în listă și afișează un 
mesaj dacă nu există nimic de afișat.

Dacă lista este goală:
Dacă todos_incomplete este gol (adică nu sunt todos nefinalizate pentru userId=1), atunci va trebui să 
alegi un alt userId care să aibă todos nefinalizate.

Rezultat așteptat:
Dacă lista conține elemente, ar trebui să primești un output cu primele 3 todos.
Dacă nu există todos incomplete pentru userId=1, vei primi mesajul "No incomplete todos found.".
Testând în acest mod, vom afla dacă problema este la API sau la cod.
'''
