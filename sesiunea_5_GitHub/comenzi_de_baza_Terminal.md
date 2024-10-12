# Terminal / Command prompt - Comenzi de baza

### 📌 ls (sau dir în Windows): - aceasta comanda ne ajuta sa stim ce avem in directorul curent 
     Exemplu comanda in terminal => ls / dir

### 📌 cd: - aceasta comanda ne ajuta sa schimbam  directorul curent. 
     Exemplu comanda in terminal =>  cd nume-director

### 📌 cd . . : - aceasta comanda ne ajuta sa revenim in directorul anterior
     Exemplu comanda in terminal => cd . .

###  📌 mkdir: - aceasta comanda ne ajuta sa cream un nou director
    Exemplu comanda in terminal => mkdir nume-director

### 📌 touch: - aceasta comanda ne ajuta sa cream un fișier gol cu un anumit nume.
    Exemplu comanda in terminal => touch nume-fisier

### 📌 rm: -aceasta  comanda ne ajuta sa stergem fișiere sau directoare.
    Exemplu comanda in terminal => rm nume-fisier
    Exemplu comanda in terminal => rm -r nume-director

### 📌 cp: - aceasta comanda ne ajuta sa copiem fisiere si directoare, va trebui sa ii spunem unde vrem sa copiem fisierele respective
    Exemplu comanda in terminal => cd sursa destinatie

### 📌 clear: - aceasta comanda ne ajuta sa curățăm ecranul terminalului pentru a face vizualizarea mai ușoară.
    Exemplu comanda in terminal => mkdir nume-director

### 📌 echo: - aceasta comanda ne ajuta sa scriem continut in fisierul nostru, vom suprascrie continutul folosind aceasta comanda
    Exemplu comanda in terminal => echo “print(‘hello, hello ‘)”  >  nume-fisier.py  

### 📌 cat: - aceasta comanda ne ajuta sa afisam continutul unui fisier 
    Exemplu comanda in terminal => cat >> nume-fisier  - dupa ENTER scriem continutul in fisier, iar cand am terminat de scris folosim Ctrl + D pt linux sau Ctrl + Z pt Windows

### 📌 vim: - aceasta comanda ne ajuta sa deschidem fisierul si sa putem scrie in el - folosim pt linux
    Exemplu comanda in terminal => vim nume-fisier.py  
    Notepad: - aceasta comanda ne ajuta sa deschidem fisierul si sa putem scrie in el - folosim pt windows
    Exemplu comanda in terminal => notepad nume-fisier.py  

- apoi se va deschide fisierul si putem scrie continut in fisierul nostru dupa ce apasam tasta “i”
- putem sa iesit din fisier urmand pasii de mai jos:
  - Pasul 1: ne asiguram ca suntem in modul de editare, vom apasa tasta “esc” 
  - Pasul 2: ne asiguram ca salvam datele folosind comanda :w sau :w! - salvam fortat continutul din fisier 
  - Pasul 3: ne asiguram ca nu există mesaje de eroare: Vim poate afișa mesaje de eroare în partea de jos a ecranului. Verificați dacă există vreun mesaj de eroare care să indice motivul pentru care comanda nu funcționează 
  - Pasul 4: cand vrem sa iesim din fisier vom folosi comanda :q sau :q! n - fortam sa iesim din fisier fara sa salvam

- Informativ: cand vrem sa iesim din fisier si sa salvam automat vom folosi comanda :wq sau :wq! - fortam sa iesim din fisier si sa salvam automat