# Creare proiect Django - comenzi de baza

1. Deschidem terminalul sau command prompt
2. Instalezi django folosind comanda <span style="color:orange;">pip install django
3. Selectezi locația unde vrei sa creezi proiectul folosind framework-ul Django 
4. Creezi proiectul folosind comanda de mai jos <span style="color:orange;">django-admin startproject numeproiect </span>- aceasta este numele proiectului
5. Mergi în folderul proiectului <span style="color:orange;">cd numeproiect 
6. Creezi aplicația folosind comanda <span style="color:orange;">python3.11 manage.py startapp numeaplicatie </span>- aceasta este numele aplicației
7. Creezi venv folosind comanda <span style="color:orange;">python3.11 -m venv venv</span>
8. Activezi venv folosind comanda de mai jos
   * <span style="color:orange;">source venv/bin/activate </span>- pt macOS/linux
   * <span style="color:orange;">venv\Scripts\activate </span>- pt windows
9. Deschidem proiectul folosind pyCharm, vom merge pe open, apoi selectam folderul proiectului aplicatiei creat cu django
10. Facem <span style="color:orange;">setup-ul bazei de date in fisierul settings.py
    1. django foloseste default libraria sqlite3 - aici trebuie sa scriem numele bazei de date
    2. putem folosi si alte baze de date- aici avem link access la documentatie https://docs.djangoproject.com/en/4.1/ref/settings/#databases
11. Rulam aplicația folosind comanda <span style="color:orange;">python3.11 manage.py runserver</span>, aceasta comanda o vom rula in terminalul aplicatie PyCharm

<span style="color:orange;">OOP</span>
###  Baza de date 
- Generarea migrărilor pentru modele bazei de date se va face utilizand comanda <span style="color:orange;">python3.11 manage.py makemigrations</span> pentru a genera fișiere de migrare. Acest lucru va crea fișiere în directorul migrations/ al fiecărei aplicații.
- Aplicarea migrărilor se va face utilizand comanda <span style="color:orange;">python3.11 manage.py migrate</span> pentru a aplica migrările și a crea tabelele efective în baza de date.