```python
"""
Pasii executati in cadrul proiectului DigitalClock
"""
```
###### Terminal CMD
```commandline
mkdir ProiecteDjango
cd ProiecteDjango
pip install django
django-admin startproject ClockDigital
cd ClockDigital
python manage.py startapp clock_digital
cd ClockDigital
dir
python -m venv venv

python manage.py runserver

```
###### Fisierul settings din proiect
```python
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clock_digital',  # Am adaugat aici numele proiectului
]

# todo inca o modificare de STATIC_URL

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
###### Fisierul urls din proiect
```python
from django.contrib import admin
from django.urls import path, include  # am adaugat metoda include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clock_digital.urls')),  # am adaugat un nou path
]
```
###### In folderul proiectului digital_clock
add: urls.py
```python
from django.urls import path
from clock_digital.views import digital_clock

urlpatterns = [
    path('', digital_clock, name='clock_digital'),
]
```
complete: views.py
```python
from django.shortcuts import render
import datetime


def digital_clock(request):
    ora_curenta = datetime.datetime.now()
    ora_formatata = ora_curenta.strftime('%H:%M:%S %p')
    ora_formatata = ora_formatata.replace(':', "o")
    dict_clock = {
        '0': [' _ ',
              '| |',
              '|_|'],

        '1': ['   ',
              '  |',
              '  |'],

        '2': [' _ ',
              ' _|',
              '|_ '],

        '3': [' _ ',
              ' _|',
              ' _|'],

        '4': ['   ',
              '|_|',
              '  |'],

        '5': [' _ ',
              '|_ ',
              ' _|'],

        '6': [' _ ',
              '|_ ',
              '|_|'],

        '7': [' _ ',
              '  |',
              '  |'],

        '8': [' _ ',
              '|_|',
              '|_|'],

        '9': [' _ ',
              '|_|',
              '  |'],

        'o': ['   ',
              ' o ',
              '   ']
    }
    output_line = ['', '', '']
    for caracter in ora_formatata:
        if caracter in dict_clock:
            numar = dict_clock[caracter]
            for i in range(3):
                output_line[i] += numar[i] + '   '
    return render(request, 'clock_digital/clock.html', {'output_line': output_line})

```
###### Creare folder templates in proiectul clock_digital => templates creare folder clock_digital si fisier clock.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Digital Clock</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
<body>
    <div class="container">
        <h1 class="text">Digital Clock</h1>
        <p class="text">{{ ora_formatata }}</p>
        <pre>
            {{ output_line.0 }}
            {{ output_line.1 }}
            {{ output_line.2 }}
        </pre>
    </div>

</body>
</html>
```
###### Creare folder static in ClockDigital => folder css si fisier styles.css
```css
.container {
    display: flex;
    background-color: #66D3FA;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
h1{
    font-size: 50px !important;
    margin-bottom: 10px;
    text-align: center;

}

.text {
    font-size: 100px;
    color: #ffffff;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 10px;

}

```