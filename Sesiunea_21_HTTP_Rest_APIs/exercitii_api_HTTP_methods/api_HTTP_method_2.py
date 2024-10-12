"""
2. Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.
"""
import requests

'''
Pentru a rezolva acest exercițiu în Python, vom folosi API-ul de la jsonplaceholder.typicode.com. Acesta ne oferă 
endpoint-uri pentru postări, comentarii, albume și poze. Vom alege un post pentru a afișa comentariile asociate 
și un album pentru a afișa lista de fotografii.
'''

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

'''
Explicația codului:
Alegem un post și afișăm lista de comentarii:

Folosim GET pe endpoint-ul pentru comentarii asociat unui post specific: 
https://jsonplaceholder.typicode.com/posts/{post_id}/comments.
După ce primim răspunsul, verificăm dacă statusul este 200 (succes) și apoi parcurgem 
lista de comentarii pentru acel post, afișând informațiile relevante (ID-ul comentariului, 
numele persoanei care a comentat, emailul și conținutul comentariului).
Alegem un album și afișăm lista de poze:

La fel, folosim GET pe endpoint-ul pentru fotografii asociat unui album: 
https://jsonplaceholder.typicode.com/albums/{album_id}/photos.
După ce primim răspunsul, verificăm dacă statusul este 200 și afișăm informații despre fiecare 
fotografie (ID-ul pozei, titlul și URL-ul).

Observații:
Poți schimba valorile pentru post_id și album_id pentru a selecta alte postări și albume.
API-ul returnează date fictive, așa că poți explora cu ușurință diferite informații 
fără să-ți faci griji pentru date reale.
'''
