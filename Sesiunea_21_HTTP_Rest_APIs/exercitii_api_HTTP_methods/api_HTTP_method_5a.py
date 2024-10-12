"""
5. Folosind query parameters, filtrează lista de todos pentru userul ales astfel incat
sa afisezi doar todos care nu sunt completed.
"""
import requests

'''
Pentru a rezolva acest exercițiu, vom folosi query parameters pentru a obține lista de todos care nu au fost încă 
finalizate (completed = False) pentru un anumit utilizator (de exemplu, userId = 1). Vom folosi un request de tip 
GET cu parametrul de filtrare corespunzător.
'''

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
if response.status_code == 200:
    todos_incomplete = response.json()

    # Afișăm primele 3 todos nefinalizate
    for todo in todos_incomplete[:3]:
        print(f"ID Todo: {todo['id']}, Titlu: {todo['title']}, Completat: {todo['completed']}")

    # Calculăm și afișăm câte todos nefinalizate rămân
    total_todos = len(todos_incomplete)
    if total_todos > 3:
        print(f"+{total_todos - 3} more todos incomplete.")
else:
    print(f"Error: {response.status_code}")

'''
Explicația codului:
URL-ul de bază: Folosim https://jsonplaceholder.typicode.com/todos, care este endpoint-ul pentru lista de todos.
Query parameters: Specificăm userId=1 pentru a filtra todos pentru un anumit utilizator, și completed=False pentru 
a obține doar cele care nu au fost finalizate.

Verificarea răspunsului: Verificăm dacă răspunsul de la server este corect (status_code == 200). Dacă da, parcurgem 
primele 3 todos și le afișăm.

Afișarea restului: Dacă există mai multe todos incomplete decât cele afișate (primele 3), afișăm câte todos rămân 
nefinalizate.

Concluzie:
Codul afișează primele 3 todos nefinalizate pentru utilizatorul selectat și, dacă există mai multe, 
arată câte todos rămân. Utilizarea query parameters permite filtrarea eficientă a datelor din API.
'''
