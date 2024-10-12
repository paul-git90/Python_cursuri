# Aplicație de Administrare a Citirilor Contoarelor de Apă

## Descriere

Se dorește să se implementeze o aplicație de administrare a citirilor contoarelor de apă caldă și apă rece pentru o familie. În fiecare lună, o familie trebuie să predea valorile contoarelor de apă caldă și apă rece la administrator împreună cu consumul pe luna curentă. Aplicația simplifică această activitate printr-o interfață ușor de utilizat.

## Funcționalități

Aplicația oferă următoarele funcționalități:

- **Adăugare citire**: Utilizatorul poate adăuga citiri pentru o anumită lună, introducând anul, luna (în format `ian`, `feb`, `mar`, etc.), valoarea contorului de apă rece și valoarea contorului de apă caldă.
  
- **Ștergere citire**: Utilizatorul poate șterge o citire pentru o anumită lună, introducând anul și luna corespunzătoare.
  
- **Afișare consum**: Utilizatorul poate afișa consumul de apă pe o anumită lună, vizualizând valorile contoarelor pentru luna curentă și luna precedentă, precum și consumul.

- **Iesire**: Aplicația permite utilizatorului să iasă din program.

## Cerințe

La adăugarea unei citiri, utilizatorul trebuie să introducă:

1. Anul (fără validare).
2. Luna în format abreviat (ex: `ian`, `feb`, `mar`, ... `dec`).
3. Valoarea contorului de apă rece.
4. Valoarea contorului de apă caldă.

### Validări

- Utilizatorul va primi un mesaj de eroare dacă:
  - Anul sau luna nu sunt corecte.
  - Există deja o citire pentru luna respectivă.
  - Valoarea contoarelor este invalidă (valoarea curentă a contorului este mai mică decât valoarea de pe luna precedentă).

La ștergerea unei citiri, utilizatorul trebuie să introducă:

- Anul și luna. Se va primi un mesaj de eroare dacă anul și luna sunt invalide sau dacă nu există o citire pentru anul și luna introduse.

La afișarea consumului, aplicația va prezenta:

- Valorile contoarelor pe luna precedentă și luna curentă.
- Consum total pe luna curentă.

### Exemple de Utilizare

```plaintext
> add ian 2023 100 105
Citire adăugată pentru ian 2023: Apa caldă 100, Apă rece 105

> add feb 2023 104 110
Citire adăugată pentru feb 2023: Apa caldă 104, Apă rece 110

> show feb 2023
ian 2023
Apa caldă: 100
Apă rece: 105
feb 2023 consum
Apa caldă: 104
Apă rece: 110
Consum: 4 (apa caldă), 5 (apă rece)

> delete feb 2023
Citire ștearsă pentru feb 2023

> exit
Aplicația s-a încheiat.
