"""
4. Alege un post existent și realizează operațiunile de PUT si PATCH (atentie, modificările NU vor fi salvate,
analizăm doar răspunsul). Ce observi ca este diferit între cele 2 metode?
"""
import requests

'''
Pentru a rezolva acest exercițiu și a înțelege diferența dintre metodele HTTP PUT și PATCH, vom alege un post existent 
și vom efectua ambele cereri către API-ul jsonplaceholder.typicode.com. Vom analiza răspunsurile pentru a înțelege 
cum sunt tratate diferit cele două cereri.

PUT: Este folosit pentru a înlocui complet resursa existentă.
PATCH: Este folosit pentru a actualiza parțial resursa, fără a o înlocui în totalitate.
'''

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

'''
Explicația codului:
Endpoint-ul pentru un post existent:
Am ales postarea cu id = 1 și vom face cereri PUT și PATCH către URL-ul corespunzător.

Cererea PUT:
În această cerere, trimitem toate câmpurile necesare (id, title, body, userId). Aceasta va înlocui complet 
resursa existentă cu datele noi.

Cererea PATCH:
În cererea PATCH, trimitem doar câmpul title pe care vrem să-l actualizăm. Aceasta va actualiza doar acest câmp 
în resursa existentă, lăsând celelalte câmpuri nemodificate.

Analizăm răspunsurile:
Vom observa cum se comportă cererile PUT și PATCH diferit în ceea ce privește modificarea resursei.

Diferența între PUT și PATCH:
PUT: Înlocuiește complet resursa. Toate câmpurile trebuie trimise în cererea PUT, iar resursa existentă este 
suprascrisă complet.
PATCH: Modifică doar câmpurile specificate în cerere. Restul câmpurilor rămân nemodificate.

Observații:
PUT: Înlocuiește toate câmpurile existente cu datele noi. De exemplu, înlocuim atât title, cât și body cu noile valori.
PATCH: Actualizează doar câmpul specificat (în acest caz, doar title este modificat). Celelalte câmpuri (body, userId) 
rămân nemodificate.

Concluzie:
PUT este folosit atunci când dorim să înlocuim complet o resursă existentă.
PATCH este utilizat pentru modificări parțiale, atunci când dorim să schimbăm doar anumite câmpuri din resursa 
existentă, fără a afecta restul.
'''
