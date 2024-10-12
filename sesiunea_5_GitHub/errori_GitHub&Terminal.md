# GitHub errors la incarcare repository

# Etapele necesare pentru a incarca un repository sunt:
…or create a new repository on the command line
echo "# gestionare_companie" >> README.md
git init
git add .
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/paul-git90/gestionare_companie.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/paul-git90/gestionare_companie.git
git branch -M main
git push -u origin main

## Navigarea clasica prin Terminal
c: \\     # select C directory  #  cd C:\Users\NumeleTau\Documents
d: \\     # select D directory
dir       # check Folders
ls        # ls sau Get-ChildItem - Listează fișierele și folderele din directorul curent echivalent cu dir
cd ..     # List directory contents: Afișează conținutul directorului curent
cd \      # Go to root directory: Te duce direct la rădăcina partiției curente ex: C:\
mkdir ProiectNou      # mkdir [nume_folder] - Make Directory: Creează un nou folder (director)
rmdir ProiectNou      # rmdir [nume_folder] - Remove Directory: Șterge un folder gol
del fisier.txt        # del [nume_fisier] - Delete File: Șterge un fișier
copy fisier.txt D:\Backup\      # copy [sursa] [destinatia] - Copy File: Copiază un fișier
move fisier.txt D:\Backup\      # move [sursa] [destinatia] - Move File: Mută un fișier

# commit GitHub exemplu
git init
git add .
git commit -m "comentariu: acesta este proiectul meu"
git branch -M main
git branch
git status
git log
git log --oneline
git remote add origin https://github.com/paul-git90/gestionare_companie.git  # adresa repo de pe GitHub
git branch -M main
git push -u origin main

### setare account GitHub exemplu
git config --global user.name "paul-git90"
git config --global user.email "paopau.games@gmail.com"

### check account GitHub
git config --global user.name
git config --global user.email

### if errors
error: failed to push some refs to 'https://github.com/paul-90git/Control_ENV.git' apare de obicei atunci când 
branch-ul local pe care încerci să faci push nu este sincronizat cu branch-ul remote. Cele mai comune cauze sunt:
1. Modificări noi pe branch-ul remote: S-ar putea ca alte persoane să fi făcut push între timp pe același branch remote, 
iar tu încerci să faci push fără să fi actualizat branch-ul local.
2. Conflicte de merge: Dacă ai modificări locale care intră în conflict cu modificările de pe remote, Git nu poate face 
push fără ca tu să rezolvi conflictele.

### Rezolvarea problemei
Sincronizează branch-ul local cu remote: Folosește comanda git pull pentru a aduce modificările de pe remote înainte 
de a face push:

git pull origin <nume-branch>
git push

Rezolvă conflictele (dacă apar): Dacă git pull dă naștere la conflicte, le vei vedea în fișierele afectate. 
Rezolvă manual conflictele, marchează fișierele ca rezolvate:

git add <fisier-conflict>
git commit
git push

Resetarea completă a ultimului commit (șterge complet commit-ul și modificările din staging):
git reset --hard HEAD^

Resetarea commit-ului, dar păstrarea modificărilor în working directory:
git reset --soft HEAD^

Resetarea commit-ului și mutarea modificărilor în working directory (unstaged):
git reset --mixed HEAD^


### eroare logare GitHub din cauza suprapunerii a doua conturi GitHub si conflict de credentiale si token
Eroarea pe care o întâmpini, mai exact mesajul Permission to paul-git90/exercitii_python.git denied to PaoSqL și 
codul de eroare 403, indică faptul că nu ai permisiunile necesare pentru a face push pe repository-ul respectiv.

Cauze posibile:
Cont GitHub greșit: Ești conectat la un cont GitHub diferit față de cel 
care deține repository-ul sau nu ai acces corespunzător.
Credentiale GitHub expirate sau invalide: Dacă ai stocat credentiale locale pentru autentificare pe GitHub, 
acestea ar putea fi expirate sau incorecte.
Repository-ul este privat: Dacă repository-ul este privat și utilizatorul cu care ești conectat nu are 
permisiuni de colaborator, nu vei putea face push.

### Posibile soluții:
Verifică contul GitHub folosit în terminal: Poți verifica cu ce utilizator ești autentificat folosind:
git config --global user.name
git config --global user.email

Actualizează credentialele GitHub: Poți reseta credentialele și reintroduce-le când faci git push:
Pe Windows: Deschide Credential Manager (Gestor de credentiale) și șterge credentialele GitHub stocate.
După aceea, încearcă din nou git push. Acum ar trebui să îți ceară credentialele corecte.
Verifică permisiunile pe GitHub
Reconfigurare Remote: Dacă contul curent nu are acces, 
poți elimina remote-ul curent și să configurezi din nou remote-ul corect:
git remote remove origin
git remote add origin https://github.com/[username]/[repository].git

pasi solutie:
git config --global user.name
git config --global user.email
git remote remove origin
git remote add origin https://github.com/paul-git90/exercitii_python.git
git push -u origin main

sau:
git config user.name
git config user.email
git config user.name "NumeleTau"
git config user.email "emailul_tau@example.com"

### Șterge credentialele cached
Este posibil ca sistemul să folosească credentialele vechi pentru PaoSqL. 
Poți șterge aceste credentiale din cache pentru a te autentifica din nou cu contul corect:
### Windows: Deschide Credential Manager și caută credentialele GitHub (le poți găsi sub Windows Credentials). 
Șterge-le și Git te va întreba din nou pentru credențiale la următorul git push.

git remote -v

Este important ca remote-ul să fie setat corect, cu URL-ul asociat contului GitHub pe care dorești să îl folosești. 
Verifică ce remote este configurat:

git remote remove origin
git remote add origin https://github.com/[username]/[repository].git

Reautentificare și git push
După ce ai schimbat credentialele și configurarea, încearcă din nou:

git push -u origin main

### refusing to merge unrelated histories
Eroarea "fatal: refusing to merge unrelated histories" apare atunci când încerci să îmbini două ramuri Git care 
nu au un istoric comun. Aceasta se poate întâmpla, de exemplu, atunci când ai creat un repository nou local, 
iar apoi încerci să-l aliniezi cu unul existent pe GitHub, care are deja un istoric.

git pull origin main --allow-unrelated-histories
git add nume_fisier
git commit -m "Rezolvat conflictele după pull"
git push origin main
