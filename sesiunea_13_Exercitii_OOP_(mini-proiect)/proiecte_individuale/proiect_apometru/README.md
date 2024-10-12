# Aplicație de Administrare a Citirilor Contoarelor de Apă

## Descriere

Această aplicație permite administrarea citirilor contoarelor de apă caldă și apă rece pentru o familie. Aplicația simplifică activitatea de predare a valorilor contoarelor la administrator, oferind o interfață ușor de utilizat.

## Funcționalități

- **Adăugare citire**: Utilizatorul poate adăuga citiri pentru o anumită lună.
- **Ștergere citire**: Utilizatorul poate șterge o citire existentă.
- **Afișare consum**: Utilizatorul poate vizualiza consumul de apă.
- **Iesire**: Termină aplicația.

## Cerințe

Utilizatorul trebuie să introducă:

1. Anul (fără validare).
2. Luna (în format abreviat, ex: `ian`, `feb`, etc.).
3. Valoarea contorului de apă rece.
4. Valoarea contorului de apă caldă.

## Exemple de Utilizare

```plaintext
> adauga citire
Introduceti luna (ex: ian, feb, ...): feb
Introduceti anul: 2023
Introduceti valoarea contorului de apa rece: 105
Introduceti valoarea contorului de apa calda: 100
Citire adăugată pentru feb 2023: Apa caldă 100, Apă rece 105

> afiseaza consum
Introduceti luna (ex: ian, feb, ...): feb
Introduceti anul: 2023
Valorile contoarelor pentru feb 2023:
Apa caldă: 100
Apă rece: 105
Consum apă caldă: 0
Consum apă rece: 0

> sterge citire
Introduceti luna (ex: ian, feb, ...): feb
Introduceti anul: 2023
Citire ștearsă pentru feb 2023.

> iesire
Iesire din aplicatie.
