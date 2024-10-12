## ⏮️ Ceas Digital – Varinata 1: miniproiect pilonii OOP / Varianta2: miniproiect web framework Django
Să se realizeze o aplicație care afișează ora curentă sub forma unui ceas digital în mod text, 
folosind caracterele _ și | astfel: 
Ora curentă se va afișa la interval de 1 secundă. Valorile mai mici de 10 vor fi precedate de un 0. 
Atenție la fusul orar, e posibil ca la ore să trebuiască adăugată o anumită valoare pentru a obține ora României.
Pentru separatorii dintre valori se va folosi caracterul 'o’.

Fiecare cifra din afișaj ar trebui să ocupe 4 caractere, iar punctele de separare - 3 caractere. 

## Varinata 1: miniproiect pilonii OOP - structura proiect

ClockDigitalApp/
- clock-system - va fi un python package
  - __init__.py
  - clock.py 
  - clockDigital.py
- app.py -aici vom rula aplicatie

## Varinata 2: miniproiect web framework Django - structura proiect

ClockProjectApp/
- manage.py - aici va rula aplicatie, 
insa noi vom rula aplicatia din terminal folosind comanda: python3.11 manage.py runserver
- ClockProjectAPP - va fi un python package
   - __init__.py
   - settings.py 
   - urls.py 
   - wsgi.py
- clockApp - va fi un python package
   - __init__.py
   - admin.py 
   - apps.py
   - migrations - va fi un python package
          __init__.py
   - models.py
   - tests.py
   - views.py

