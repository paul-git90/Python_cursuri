# Mini Calculator

## Descriere

Această aplicație este un mini-calculator scris în Python care permite utilizatorului să efectueze operații aritmetice 
simple prin intermediul terminalului. Aplicația pornește cu o valoare inițială (implicit 0), 
care poate fi setată din linia de comandă.
- **pentru varianta v2 care este mai elaborata**
```python
Operatii:
inlocuire operatori la apelare, pentru a evita niste erori
+, -, *, /, **=sq, //=flat, %, √=rad
```



## Cerințe

Se dorește implementarea unei aplicații de tip mini-calculator în mod text în Python. La pornire aplicația afișează 
valoarea inițială care este implicit 0. Valoarea inițială se poate seta prin intermediul unui 
parametru din linia de comandă. Apoi aplicația așteaptă o operație de la utilizator și afișează rezultatul acesteia.

## Operațiile posibile sunt:

- `+număr`: adună la valoarea curentă numărul respectiv.
- `-număr`: scade din valoarea curentă numărul respectiv.
- `*număr`: înmulțește valoarea curentă cu numărul respectiv.
- `/număr`: împarte valoarea curentă la numărul respectiv.
- `%număr`: calculează restul împărțirii valorii curente la numărul respectiv.
- `//număr`: împarte valoarea curentă la numărul respectiv și returnează partea întreagă.
- `**număr`: ridică valoarea curentă la puterea specificată.
- `=număr`: setează valoarea curentă cu numărul respectiv.
- `√`: calculează radicalul pătratic al valorii curente.
- `reset`: resetează valoarea curentă la 0.
- `x`: ieșire din program.

După fiecare operație se va afișa valoarea curentă și se așteaptă din nou un input de la utilizator. 
Linia pe care se așteaptă input-ul de la utilizator începe cu semnul `>`. Dacă o comandă nu poate fi 
înțeleasă sau executată, se va afișa mesajul "Invalid operation".

## Exemple de utilizare

```plaintext
0.0
> +5
0.0 + 5 = 5.0
5.0
> *10
5.0 * 10 = 50.0
50.0
> =7
50.0 set to 7.0
7.0
> √
√7.0 = 2.6457513110645907
> %5
7.0 % 5 = 2.0
2.0
> reset
Calculator reset to zero.
0.0
> x
