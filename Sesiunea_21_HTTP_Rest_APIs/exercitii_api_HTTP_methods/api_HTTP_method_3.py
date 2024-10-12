"""
3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea
cum ar arata în viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
"""
import requests

'''
Pentru a rezolva acest exercițiu, vom folosi metoda HTTP POST pentru a crea un nou post prin 
API-ul jsonplaceholder.typicode.com. În realitate, acest API nu salvează datele trimise, însă răspunsul returnat 
ne permite să vedem cum ar arăta postarea dacă ar fi fost salvată. Vom încerca să creăm un post cu și fără id, 
iar apoi vom analiza răspunsul.
'''

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

'''
Explicația codului:
Endpoint-ul pentru postări noi:

Facem o cerere POST la URL-ul https://jsonplaceholder.typicode.com/posts, care este folosit pentru a crea noi postări.
Post fără ID:

În primul exemplu, creăm un post fără să specificăm un id. API-ul ar trebui să genereze un id automat, chiar dacă acest 
lucru nu salvează efectiv datele.
Post cu ID:

În al doilea exemplu, încercăm să adăugăm un id manual pentru postarea pe care o trimitem.
Analizăm răspunsurile:

Pentru ambele cazuri, afișăm statusul răspunsului și datele JSON returnate de server.

Ce observăm:
Post fără ID:
Serverul generează automat un id pentru postarea noastră și returnează acest id în răspunsul JSON. Acesta ar fi 
comportamentul dorit într-un API real, unde ID-ul este generat pe server pentru a asigura unicitatea.
Post cu ID:
Chiar dacă specificăm un id manual, API-ul de la jsonplaceholder îl acceptă și îl returnează fără a-l modifica. 
Totuși, în multe aplicații reale, serverul ar ignora id-ul specificat și ar genera unul automat, ignorând datele 
introduse de utilizator.

Observații:
În cazul unui API real, este posibil ca serverul să ignore id-ul pe care îl trimitem și să creeze unul automat 
pentru a evita conflictele. În cazul jsonplaceholder, API-ul acceptă un ID specificat și returnează datele așa 
cum le-am trimis.
'''
