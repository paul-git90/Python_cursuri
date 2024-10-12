"""
HTTP, Rest APIs, Requests  - Exercitii practice
"""

import requests

# folosim https://jsonplaceholder.typicode.com

"""
1. Alege un user din lista de useri predefiniti. Pentru acesta, lanseaza requesturile necesare pentru a afișa 
următoarele informații: 
-> lista de posts
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații despre 
primele 3 obiecte, iar apoi afiseaza "+x more posts/", unde x este numărul de obiecte rămase.
"""

# Metoda HTTP GET - o folosim cand vrem sa solicitam date
# vom lua toate posts pentru userID=1

# import requests

response = requests.get(url="https://jsonplaceholder.typicode.com/users/1/posts")
print(response.status_code)  # afiseaza codul de status
if response.status_code == 200:
    posts = response.json()  # parseaza raspunsul JSON

    # Afiseaza primele 3 postari
    for post in posts[0:3]:
        print(f"UserID: {post['userId']}, ID postare: {post['id']}, titlul postarii: {post['title']}, "
              f"continutul postarii: {post['body']}")

    # Calculeaza si afiseaza cate postari raman
    postari_ramase = len(posts) - 3
    if postari_ramase > 0:
        print(f"+{postari_ramase} more posts.")
else:
    print(f"Request failed with status code: {response.status_code}")

"""
2. Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.
"""
# import requests

# Endpoint-ul pentru postări și comentarii
post_id = 1  # Alege un post cu ID-ul 1 (poți schimba acest ID)
comments_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
response_comments = requests.get(comments_url)

if response_comments.status_code == 200:
    comments = response_comments.json()
    print(f"Comentarii pentru post-ul cu ID {post_id}:")
    for comment in comments:
        print(f"Comentariu ID: {comment['id']}, Nume: {comment['name']}, Email: {comment['email']}, "
              f"Continut: {comment['body']}")
else:
    print(f"Nu s-au putut obține comentariile pentru post-ul cu ID {post_id}.")

# Endpoint-ul pentru albume și poze
album_id = 1  # Alege un album cu ID-ul 1 (poți schimba acest ID)
photos_url = f"https://jsonplaceholder.typicode.com/albums/{album_id}/photos"
response_photos = requests.get(photos_url)

if response_photos.status_code == 200:
    photos = response_photos.json()
    print(f"\nFotografii din albumul cu ID {album_id}:")
    for photo in photos:
        print(f"Fotografie ID: {photo['id']}, Titlu: {photo['title']}, URL: {photo['url']}")
else:
    print(f"Nu s-au putut obține fotografiile pentru albumul cu ID {album_id}.")

"""
3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea 
cum ar arata în viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
"""
# import requests

# Endpoint pentru crearea unui post nou
url = "https://jsonplaceholder.typicode.com/posts"

# Creăm un nou post fără să specificăm un id (id-ul ar trebui să fie generat automat)
new_post_data = {
    "title": "Un titlu nou",
    "body": "Acesta este conținutul postului meu.",
    "userId": 1
}

# Facem cererea POST pentru a crea postarea fără ID
response_without_id = requests.post(url, json=new_post_data)

# Afisam răspunsul pentru postarea fără ID
print("Răspuns pentru crearea unui post fără ID:")
print("Status code:", response_without_id.status_code)
print("Răspuns JSON:", response_without_id.json())

# Creăm un nou post specificând un id
new_post_with_id_data = {
    "id": 101,  # Adăugăm un ID manual (API-ul nu folosește un ID deja existent)
    "title": "Un titlu nou cu ID",
    "body": "Acesta este conținutul postului meu cu ID specificat.",
    "userId": 1
}

# Facem cererea POST pentru a crea postarea cu ID
response_with_id = requests.post(url, json=new_post_with_id_data)

# Afisam răspunsul pentru postarea cu ID
print("\nRăspuns pentru crearea unui post cu ID:")
print("Status code:", response_with_id.status_code)
print("Răspuns JSON:", response_with_id.json())

"""
4. Alege un post existent și realizează operațiunile de PUT si PATCH (atentie, modificările NU vor fi salvate, 
analizăm doar răspunsul). Ce observi ca este diferit între cele 2 metode?
"""
# import requests

# URL pentru un post existent (de exemplu, post cu id 1)
url = "https://jsonplaceholder.typicode.com/posts/1"

# Datele noi pentru PUT (înlocuirea completă a postării)
updated_post_data_put = {
    "id": 1,  # Menținem același ID
    "title": "Titlul nou complet (PUT)",
    "body": "Acesta este conținutul postării complet înlocuit folosind PUT.",
    "userId": 1
}

# Facem cererea PUT (înlocuirea completă a resursei)
response_put = requests.put(url, json=updated_post_data_put)

# Afisam răspunsul pentru cererea PUT
print("Răspuns pentru cererea PUT:")
print("Status code:", response_put.status_code)
print("Răspuns JSON:", response_put.json())

# Datele pentru PATCH (actualizare parțială)
updated_post_data_patch = {
    "title": "Titlu parțial modificat (PATCH)"
}

# Facem cererea PATCH (actualizare parțială)
response_patch = requests.patch(url, json=updated_post_data_patch)

# Afisam răspunsul pentru cererea PATCH
print("\nRăspuns pentru cererea PATCH:")
print("Status code:", response_patch.status_code)
print("Răspuns JSON:", response_patch.json())

"""
5. Folosind query parameters, filtrează lista de todos pentru userul ales astfel incat 
sa afisezi doar todos care nu sunt completed.
"""
# import requests

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
