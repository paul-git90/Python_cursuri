## Curs: Recap OOP + Miniproiect: Gestionare angajati companie

1. Implementati o clasa Angajat() tinand cont de urmatoarele cerinte:
   1. atribute: nume, prenume, salariu 
   2. Constructor pentru toate atributele 
   3. Metode:
      - descrie() - afiseaza informatii despre angajat
      - nume_complet() - afiseaza numele complet al angajatului
      - salariu_lunar() - seteaza si retuneaza salariul lunar
      - salariu_anual() - calculeaza si retuneaza salariul anual
      - marire_salariu(procent) - calculeaza si returneaza salariul marit cu un anumit procent


2. Implementati o clasa Factura() tinand cont de urmatoarele cerinte:
   1. Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc 
   2. Constructor: toate atributele, fără serie 
   3. Metode:
      - schimbă_cantitatea(cantitate) - seteaza noua cantitate pe factura si modifica valoarea totala a produsului per bucata, respectiv valoarea totala a facturii
      - schimbă_prețul(pret) -seteaza noul pret pe factura si modifica valoarea totala a produsului per bucata, respectiv valoarea totala a facturii
      - schimbă_nume_produs(nume) - seteaza noul nume a produsului
      - generează_factura() - va afisa tabelar 


3.Extra - dezvolta un proiect nou pornind de la cerintele ex 1 si adauga noi functionalitati folosing Pilonii OOP
- gestionare_angajati/ --- acesta este numele proiectului
  - companie/ --acesta este un pachet python
    - __init__.py -----acesta este un fisier python gol care se creaza automat cand creem un pachet python
    - companie.py -----acesta este un modul/fisier python
  - departament/     --acesta este un pachet python
    - __init__.py -----acesta este un fisier python gol care se creaza automat cand creem un pachet python
    - departament.py -----acesta este un modul/fisier python
    - departament_hr.py -----acesta este un modul/fisier python
    - departament_vanzari.py -----acesta este un modul/fisier python
    - departament_operational.py -----acesta este un modul/fisier python
  - informatii_angajati/   --acesta este un pachet python
    - __init__.py -----acesta este un fisier python gol care se creaza automat cand creem un pachet python
    - persoana.py -----acesta este un modul/fisier python
    - angajat.py -----acesta este un modul/fisier python
    - manager.py -----acesta este un modul/fisier python
  - tests/
    - __init__.py -----acesta este un fisier python gol care se creaza automat cand creem un pachet python
    - test_companie.py -----acesta este un modul/fisier python
  - main.py ----- aceste este un fisier python in care vom rula aplicatia