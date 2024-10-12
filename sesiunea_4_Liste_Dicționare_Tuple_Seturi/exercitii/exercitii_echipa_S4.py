"""
Structuri de date
Exerciții - studiu în workshopul de weekend
Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
"""
"""
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
●	Afișeaz-o.
●	Inversează ordinea folosind slicing și suprascrie această listă.
●	Printează varianta actuală (inversată).
●	Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie 
să o suprascrii în acest caz, deoarece metoda face asta automat.
●	Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
"""
# 1. Declarăm lista note_muzicale
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# 2. Afișăm lista
print("Lista inițială:", note_muzicale)
# 3. Inversăm ordinea folosind slicing și suprascriem lista
note_muzicale = note_muzicale[::-1]
# 4. Afișăm lista inversată
print("Lista inversată prin slicing:", note_muzicale)
# 5. Aplicăm metoda care inversează ordinea listei
note_muzicale.reverse()
# 6. Afișăm lista actuală (ar trebui să fie varianta inițială)
print("Lista după aplicarea metodei reverse:", note_muzicale)
"""
2. De câte ori apare ‘do’?
"""
# Declarăm lista note_muzicale
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# Calculăm de câte ori apare 'do' în listă
numar_aparitii_do = note_muzicale.count("do")
# Afișăm rezultatul
print(f"Nota 'do' apare de {numar_aparitii_do} ori în listă.")
"""
3. Transforma lista de mai sus intr-un tuple. Incearca sa adaugi o nota noua.
"""
# Declarăm lista note_muzicale
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# Transformăm lista într-un tuple
note_muzicale_tuple = tuple(note_muzicale)
# Afișăm tuple-ul
print("Tuple-ul note_muzicale:", note_muzicale_tuple)
# Încercăm să adăugăm o notă nouă la tuple (aceasta va genera o eroare)
try:
    note_muzicale_tuple.append("re")
except AttributeError as e:
    print(f"Nu putem adăuga o notă nouă la tuple: {e}")
"""
4. Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata 
de cate ori apare nota in gama. Afiseaza-l.
"""
# Declarăm lista note_muzicale
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# Creăm un dicționar pentru a stoca numărul de apariții ale fiecărei note
dict_note_muzicale = {}
# Iterăm prin fiecare notă din listă
for nota in note_muzicale:
    if nota in dict_note_muzicale:
        dict_note_muzicale[nota] += 1
    else:
        dict_note_muzicale[nota] = 1
# Afișăm dicționarul
print("Dicționarul notelor muzicale:", dict_note_muzicale)
