# Aplicație Ceas Digital

## Descriere

Această aplicație are ca scop afișarea orei curente sub forma unui ceas digital în mod text. Ora va fi actualizată la fiecare secundă și va respecta următoarele specificații:

- Valorile mai mici de 10 vor fi precedate de un 0.
- Separatorii dintre ore, minute și secunde vor fi reprezentați de caracterul `o`.
- Fiecare cifră din afișaj va ocupa 4 caractere, iar separatorii vor ocupa 3 caractere.
- Aplicația va ține cont de fusul orar, având posibilitatea de a adăuga o valoare specifică pentru a obține ora locală în România.

## Cerințe Funcționale

1. **Afișarea orei**:
    - Formatul orei va fi `HHoMMoSS`, unde `HH` reprezintă orele, `MM` reprezintă minutele și `SS` reprezintă secundele.
    - Exemplu: `12o34o56`

2. **Gestionarea orei**:
    - Utilizatorul poate specifica fusul orar (opțional) pentru a corecta ora locală.
    - Ora va fi actualizată la fiecare secundă.

3. **Formatul Afișajului**:
    - Fiecare cifră va ocupa 4 caractere.
    - Separatorii vor ocupa 3 caractere, astfel încât să existe o distanțare corespunzătoare între cifre.

## Exemple de Afișare

