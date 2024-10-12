# Pachete Python. Interacțiune cu fișiere.

#### Cerinte

Pachete python. Interacțiune cu fișiere. 

1.	Create a text file called “hello.txt” and add the following text inside of it:
Python                                                                                              
Java
Javascript                                                                                              
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file
2.	Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file.
3.	Write a short program that reads the “hello.txt” file and displays every other line (only odd lines).
4.	Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)

## 1. Crearea unui fișier text

Se va crea un fișier text numit `hello.txt` și se va adăuga următorul text în interiorul său:

```python
### Program pentru citirea și afișarea conținutului fișierului

```python
# Creare și scriere în fișierul hello.txt
with open("hello.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("Javascript\n")
    file.write("C/C++/C#\n")
    file.write("PHP\n")
    file.write("Node.js\n")

# Citire și afișare a fișierului
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
```

## 2. Adăugarea unor linii la fișierul hello.txt
Se va scrie un program scurt pentru a adăuga următoarele linii în hello.txt:
Go
Kotlin
Swift

Program pentru adăugarea liniilor
```python
# Lista de noi limbaje de programare
new_languages = ["Go", "Kotlin", "Swift"]

# Adăugarea noilor linii în fișier
with open("hello.txt", "a") as file:
    for language in new_languages:
        file.write(language + "\n")

# Afișarea noului conținut al fișierului
with open("hello.txt", "r") as file:
    new_content = file.read()
    print(new_content)

```

## 3. Afișarea fiecărei a doua linii (linii impare)
Se va scrie un program care citește fișierul hello.txt și afișează fiecare a doua linie (doar liniile impare).

Program pentru afișarea liniilor impare
```python
# Citirea fișierului și afișarea liniilor impare
with open("hello.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):  # Pas de 2 pentru a obține liniile impare
        print(lines[i].strip())  # strip() pentru a elimina newline-ul
```

## 4. Generarea fișierelor A.txt, B.txt, ..., Z.txt
Se va scrie un program care generează 26 de fișiere text, numite A.txt, B.txt, … Z.txt. 
Fiecare fișier va conține propozițiile:
```csharp
My name is letter X.
I am the 24th letter of the alphabet.
```
Program pentru generarea fișierelor
```python
# Generarea fișierelor A.txt - Z.txt
for i in range(26):
    letter = chr(65 + i)  # 65 este codul ASCII pentru 'A'
    with open(f"{letter}.txt", "w") as file:
        ordinal_suffix = "th"  # Default suffix
        if i == 0:
            ordinal_suffix = "st"
        elif i == 1:
            ordinal_suffix = "nd"
        elif i == 2:
            ordinal_suffix = "rd"
        
        file.write(f"My name is letter {letter}.\n")
        file.write(f"I am the {i + 1}{ordinal_suffix} letter of the alphabet.\n")
```
### Concluzie
Aceste programe demonstrează cum să interacționezi cu fișiere în Python, inclusiv crearea, citirea, scrierea și 
manipularea conținutului fișierelor. Aceste abilități sunt esențiale pentru lucrul cu datele în aplicațiile Python.