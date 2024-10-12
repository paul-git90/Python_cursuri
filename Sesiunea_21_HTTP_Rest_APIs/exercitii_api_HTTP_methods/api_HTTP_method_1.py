"""
1. Alege un user din lista de useri predefiniti. Pentru acesta, lanseaza requesturile necesare pentru a afișa 
următoarele informații: 
-> lista de posts
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații despre 
primele 3 obiecte, iar apoi afiseaza "+x more posts/", unde x este numărul de obiecte rămase.
"""
import requests

# Metoda HTTP GET - o folosim cand vrem sa solicitam date
# vom lua toate posts pentru userID=1
# folosim Endpoint-ul https://jsonplaceholder.typicode.com

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

'''
Explicații:
Corecții aduse numărului de postări rămase:

În loc de len(post), se folosește len(posts) pentru a determina numărul total de postări. post reprezintă 
doar un obiect individual din lista de postări, dar ai nevoie de lungimea listei posts.
Verificare cod de status:

Am adăugat o verificare simplă pentru a ne asigura că cererea HTTP a fost de succes (codul de status 200). 
Dacă cererea eșuează, vei primi un mesaj de eroare cu codul respectiv.
Afișarea corectă a postărilor rămase:

Se afișează mesajul doar dacă sunt mai mult de 3 postări. Astfel, dacă utilizatorul are exact 3 postări sau 
mai puține, nu va apărea mesajul de postări rămase.
În acest exemplu, codul va afișa primele 3 postări, iar apoi va menționa că sunt încă 7 postări.
'''
