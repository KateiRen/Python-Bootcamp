# Notizen

## Kommentierung

"#" eine Zeile
eine mehrzeilige Kommentierung gibt es nicht

## Zahlen

Dezimalzahlen immer mit "." und nicht ","
also 1.3 statt 1,3

Umwandeln in String: str(variable)

## Strings

Verketten mit "+", also wie JavaScript
Typen werden aber nicht automatisch umgewandelt, Zahlen also erst mit str() konvertieren

Suche von Zeichen/Strings mit "in" Operator

```python
students = ["Max", "Monika", "Erik", "Franziska"]
if "Monika" in students:
    print("Ja, die Monika studiert hier!")
else:
    print("Nein, die Monika studiert hier nicht!")
```

### Upper / Lower

```python
w = "Hallo"
print(w.upper())
print("Hallo".lower())
```

### StartsWith / EndsWith

```python
sentence = "Ist das Wetter heute gut?"

if sentence[-1] == "?":
    print("Der Satz endet mit einem Fragezeichen")

if sentence.endswith("?"):
    print("Der Satz endet mit einem Fragezeichen")

if sentence.endswith("???"): # geht auch mit mehreren Zeichen
    print("Der Satz endet mit drei Fragezeichen")

if sentence.startswith("Ist"): # geht auch am Anfang
    print("Der Satz beginnt mit Ist")
```

### Strip / LStrip / RStrip

```python
word = "    Hallo.  "

print(word.strip()) # Hallo.  --> Punkt wird standardmäßig nicht entfernt
print(word.strip( .)) # Hallo --> als Parameter alle Zeichen eingeben, die gelöscht werden sollen
print(word.lstrip()) # nur auf der linken Seite werden die Zeichen entfernt
print(word.strip()) # nur auf der rechten Seite werden die Zeichen entfernt

print(sentence.rstrip("!?.,")) # alle Satzzeichen am Ende entfernen

```

### find

```python
sentence = "Ist das Wetter heute gut?"

print(sentence.find(", ")) # 20
print(sentence.find("!")) # -1 == nicht gefunden

```

### replace

```python
sentence = "Ist das Wetter heute gut?"

print(sentence.replace(",", ";")) # Komma durch Semikolon ersetzt
print(sentence.replace("und", "oder")) # geht auch mit mehreren Zeichen
```

### Lokalisierungen

```python
n = 5
print("Ich habe " + str(n) + " Hunde")
print("I got " + str(n) + " dogs")

translations = {
    "number_of_dogs": "Ich habe XXX Hunde"
}

print(translations["number_of_dogs"].replace("XXX", str(n)))

translations = {
    "number_of_dogs": "Ich habe {0} Hunde"
}

print(translations["number_of_dogs"].format(n)) # setzt die Zahl im Platzhalter ein

print("Ich habe {0} {1}").format(5, "Katzen")) # mehrere Platzhalter sind möglich
print("Ich habe {1} {0} mal").format(5, "Katzen")) # die Reihenfolge im Satzbau kann für andere Sprachen angepasst werden

print("Pi hat den Wert von {0}".format(3.141529)) # übernimmt alle Kommastellen
print("Pi hat den Wert von {0:.3f}".format(3.141529)) # übernimmt 3 Nachkommastellen

print("Ich habe {number} {animal}").format(number=5, animal="Katzen")) # man kann die Platzhalter auch benennen
```

## Typenumwandlung

`str(variable)`

`int(variable)`

`float(variable)`

## Runden

über `round(num, nachkommastellen)`
oder über `print("Dein BMI ist {0:.1f}".format(bmi))`

## Listen

Deklaration mit ["", "", ""]

Liste -> String

```python
"<seperator>".join(<array>)
students_as_string = ", ".join(students_array)
```

String -> Liste

```python
<array>.split("<seperator>")
students_array = students_as_string.split(", ")
# split() ohne Argument trennt an Leerzeichen
```

### Elemente anfügen

```python
<liste>.append("xyz")
```

### letztes Element entfernen

```python
planets.pop() # der entfernte Eintrag wird als Ergebnis zurückgegeben
```

### Länge der Liste

```python
len(liste)
```

## Kontrollstrukturen

### if

```python
n = 30

if n < 42:
    print("Die Zahl n ist kleiner als 42")
else:
    print("Die Zahl n ist größer oder gleich 42")

print("Ich werde auf jeden Fall angezeigt!")
```

### if mit mehreren Bedingungen

```python
age = 35

if age >= 30 and age <= 39:
    print("Diese Person ist in ihren 30-ern")

if age < 30 or age >= 40:
    print("Diese Person ist nicht in ihren 30-ern")
```

```python
country = "US"
age = 20

if (country == "US" and age >= 21) or (country != "US" and age >= 18):
    print("Diese Person darf Alkohol trinken")
```

### elif mit mehreren Bedingungen

```python
currency = "HKD"

if currency == "$":
    print("US-Dollar")
elif currency == "¥":
    print("Japanischer Yen")
elif currency == "€":
    print("Euro")
elif currency == "฿":
    print("Thai Baht")
else:
    print("Sonst")  
```

## Loops

### While

```python
counter = 0

while counter<10:
    print(counter)
    counter = counter +1
```

### For

```python
for i in range(0,10):  # geht von 0 bis 9. 10 ist nicht mehr dabei
    print(i)
```

```python
liste = [5, 8, 10]
for i in liste:  # 5, 8, 10
    print(i)
```

#### continue

```python
for i in range(0,10):  
    if i==3:            # der Wert 3 wird in der Ausgabe übersprungen
        continue
    print(i)
```

#### break

```python
for i in range(0,10):  
    if i==3:            # beim Wert 3 wird die Schleife abgebrochen/beendet
        break
    print(i)
```

## Funktionen

```python
def funktionsname(parameter):
    print(parameter)

funktionsname("Hallo")
```

```python
def multiprint(name, count):
    for i in range(0, count):
        print(name)
multiprint("Karsten", 11)
```

## Dateien

r = read
w = write
a = append

```python
# Wir öffnen die Datei lesen.txt zum Lesen ("r") und speichern ihren Inhalt in die Variable file
file = open("lesen.txt", "r")

# Wir gehen alle Zeilen nacheinander durch
# In der txt-Datei stehen für uns nicht sichtbare Zeilenumbruchszeichen, durch die jeweils das Ende einer Zeile markiert ist
for line in file:
    # Eine Zeile ohne Zeilenumbruch ausgeben
    print(line.strip())
```

```python
# Wir öffnen eine Datei zum Schreiben ("w": write)
file = open("schreiben.txt", "w")

students = ["Max", "Monika", "Erik", "Franziska"]

# Wir loopen mit einer for-Schleife durch die Liste students
for student in students:
    # Mit der write-Methode schreiben wir den aktuellen String student und einen Zeilenumbruch in das file-Objekt
    file.write(student + "\n")

# Abschließend müssen wir die Datei wieder schließen
file.close()
```

### robustere Version, bei der man sich nicht um das close() kümmern muss (bspw. wenn das programm vorher auf einen Fehler stößt)

```python
with open("schreiben.txt", "r") as file:
    for line in file:
        print(line)
```

### filtern beim Einlesen

```python
with open("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")

        if int(data[1]) < 2000000:
            continue

        if data[2] == "BUD":
            continue

        print(data)
```

## Listen Manipulation

### Letztes Element entfernen und zurückgeben

```python
students = ["Max", "Monika", "Erik", "Franziska"]
last_student = students.pop() # entfernt letztes Element und gibt es zurück
```

### Index für letztes Element, vorletztes etc

```python
print(students[-1]) # letztes Element der Liste
print(students[-2]) # vorletztes Element der Liste
```

"-" bedeutet also Zählweise von hinten aus nicht von vorn

### Liste erweitern

```python
students = ["Max", "Monika", "Erik", "Franziska"] + ["Jürgen"]
```

### einzelne Elemente entfernen

```python
del students[3] # wenn wir den Index kennen

students.remove["Franziska"] # über das Element selbst
```

## List Slicing

```python
students = ["Max", "Monika", "Erik", "Franziska"]

print(students[1:]) # erzeugt (und gibt aus) eine Teilliste vom 2. Element bis zum Ende der Liste

==> ["Monika", "Erik", "Franziska"]

print(students[2:4]) # erzeugt (und gibt aus) eine Teilliste vom 3. und bis vor 5. Element (Start bei 0)

==> ["Erik", "Franziska"]

print(students[1:-1]) # erstes Element überspringen und letztes Element ignorieren

==> ["Monika", "Erik"]

print(students[0:-1]) # ist identisch zu
print(students[:-1])

print(students[1:]) # ganze Liste ohne erstes Element

GEHT AUCH FÜR STRINGS!!!!

print("Hallo Welt"[-4:]) # letzte 4 Zeichen
==> Welt
```

## List Comprehensions

```python
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [x * x for x in xs] # erstellt neue Liste aus Berechnung auf Basisliste ohne extra Schleife
print(ys)

students = ["Max", "Monika", "Erik", "Franziska"]
buchstaben = [len(name) for name in students]
print(buchstaben)

xs = [ x/10 for x in range(0,100)]
ys = [ x * x for x in xs]
print(xs)
print(ys)
```

## Dictionaries

```python
d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
print (d)
print (d["Helsinki"])  # Indexform liefert kritischen Fehler, wenn Key nicht existiert
print (d.get("Helsinki")) # Abfrage mit get() liefert "None" wenn Key nicht existiert
```

### Element ergänzen

```python
d["Budapest"] = "BUD"
```

### Element entfernen

```python
del d["Budapest"]
```

### Abfrage ob Key existiert

```python
if "Budapest" in d:
    print("Budapest ist im Dictionary")
```

## Tupel

```python
t = (1, 2, 3)  # Liste hat eckige Klammern, Dictionary {} und Tupel ()
# kann nachträglich nicht verändert werden (Immutable)

student = ("Max Müller", 22, "Informatik")

name = student[0]
age = student [1]
subject = student[2]
```

### Entpacken eines Tupels

```python
# alternativ zum Beispiel davor
name, age, subject = student
print(name)
print(age)
print(subject)
```

### Nutzung für mehrere Rückgabewerte

```python
def get_student():
    return ("Max Müller", 22, "Informatik")

name, age, subject = get_student()
```

### Liste von Tupels

```python
students = [
    ("Max Müller", 22),
    ("Monika Mustermann", 23)
]

for student in students:
    print student
    name, age  = student
    print(name)
    print(age)

oder gleich

for name, age in students:
    print(name)
    print(age)
```

### Dictionary in Liste von Tupeln umwandeln

```python
d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}

print(d.items())

for key, value in d.items():
    print(key + ": " + value)
```

## Listen verschachteln

```python
liste = [
    ["Berlin", "München", "Köln"],
    ["budapest", "Pecs", "Sopron"]
]

print(liste[1][0])

students = {
    "Informatik": ["Max", "Monika"],
    "BWL": ["Erik", "Franziska"]
}

print(students["BWL"])
```

## Objektorientierung

```python
class Student(): # erster Buchstabe sollte groß sein
    pass         # pass sagt aus "es ist ok, dass hier noch nichts steht"

erik = Student()
erik.firstname = "Erik"
erik.lastname = "Mustermann"

print(erik.firstname)
```

```python
class Student(): # erster Buchstabe sollte groß sein
    def print_name(self):
        print(self.firstname + " " + self.lastname)
```

### Hier mit Konstruktor

```python
class Student(): # erster Buchstabe sollte groß sein
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.term = 1
    def print_name(self):
        print(self.firstname + " " + self.lastname + " (Semester: " + str(self.term) + ")")
    def increase_term(self):
        self.term = self.term +1

erik = Student("Erik", "Mustermann")
erik.increase_term()
erik.print_name()
```

### Private Eigenschaften und Methoden

Komplexität nach außen reduzieren. Interne Funktionen nicht nach außen sichtbar machen.

Konvention ist die Variable mit einem Unterstrich zu beginnen, wenn ein Zugriff von außen nicht erwünscht ist.
Interaktion von außen ist noch möglich, sollte aber wenn möglich vermieden werden

Startet die Variable mit zwei Unterstrichen, dann kann von außen nicht zugegriffen werden (lesend oder schreibend).

```python
class Student(): # externe Verwendung von term sollte vermieden werden
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._term = 1
```

```python
class Student(): # externe Verwendung von term nicht möglich
    def __init__ (self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1
```

```python
class PhoneBook():
    def __init__(self):
        self.__entries = {}
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
    def get(self, name):
        if name in self.__entries:
            return self.__entires[name]
        else:
            return None

book = PhoneBook()
book.add("Mustermann", "08912345")
book.add("Müller", "04012345")

print(book.get("Mustermann"))
```

### Besondere Methoden __str__, __repr__, __len__

print(book) # zeigt an, dass es sich um ein objekt der Klasse Phonebook ist und an Speicheradresse xyz liegt

```python
class PhoneBook():
    def __str__(self):
        return "Phonebook(" + str(self.__entries) + ")"

print(book) # Zeigt jetzt meine Beschreibung mit Auflistung des Dictionaries

book # zeigt immernoch die alte Ausgabe (Objekt-Klasse und Speicher)
```

```python
class PhoneBook():
    def __repr__(self):
        return self.__str__()

print(book) # Zeigt jetzt meine Beschreibung mit Auflistung des Dictionaries

print(len(book)) # liefert Fehlermeldung
```

```python
class PhoneBook():
    def __len__(self):
        return len(self.__entries)

print(len(book)) # liefert die korrekte Anzahl der Einträge
```

### Vererbung

```python
class Student(): # externe Verwendung von term nicht möglich
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1
    def name(self):
        return self.name + " " + self.surname

class WorkingStudent(Student):
    def __init__(self, firstname, surname, company):
        super().__init_(firstname, surname)
        self.company = company

student = WorkingStudent("Max", "Müller", "ABC GmbH")
print(student.name()) # da keine eigene Funktion definiert ist, wird die Funktion aus der Super-Klasse Student genutzt
```

```python
class WorkingStudent(Student):
    def __init__(self, firstname, surname, company):
        super().__init_(firstname, surname)
        self.company = company
    def name(self):
        return super().name() + " (" + self.company +")"

student = WorkingStudent("Max", "Müller", "ABC GmbH")
print(student.name()) # Jetzt wird die neue name Methode genutzt
```

Jetzt können wir eine Liste gemischt aus Students und WorkingStudents füllen und über alle Elemente iterieren und jeweils .name() aufrufen, ohne dass es Probleme gibt.

## Variablentypen prüfen

```python
w_student = WorkingStudent("Max", "Müller", "ABC GmbH")
student = Student("Monika", "Mustermann")

# ohne Berücksichtigung der Vererbung
print(type(w_student))
print(type(student))

# mit Berücksichtigung der Vererbung
print(isinstance(w_student, WorkingStudent)) # True
print(isinstance(w_student, Student)) # True
print(isinstance(student, WorkingStudent)) # False
print(isinstance(student, Student)) # True
```

## Bennung von Klassen und Variablen

...gemäß styleguide
**PascalCase** vs **camelCase** vs **sneak_case**

Klassennamen: **PascalCase**
Variablen: **sneak_case**
Funktionsname: **sneak_case**

**camelCase** kommt in Python nicht vor!

## Statische Variablen

```python
class Car:
    price = "expensive" # ohne "self" gilt für alle Instanzen der Klasse

c = Car()
print(c.price)

Car.price  ="cheap" # ändern der Variable in der Klasse
print(c.price) # ändert alle Instanzen

# das will man meistens nicht, also drauf achten:

class Car:
    def __init__(self):
        self.price = "expensive" # für jede Instanz separat
```

## Berechnungen

```python
import math
print(math.pi)

volumen = side ** 3 # Exponent 3
flaeche = side ** 2 # Exponent 2
flaeche += 15 # um 15 erhöhen
flaeche -= 5 # um 5 verringern
```

## Module

```python
import hallo
hallo.welt() # Aufruf der Funktionen über den Modulnamen
hallo.mars()
```

```python
from hallo import welt, mars
welt() # Bei diesem Import sind die Funktionen direkt nutzbar
mars()
```

```python
import matplotlib.pyplot as plt # Importieren eines Teilbereichs und gleichzeitig umbenennen
plt.plot([1, 2, 3], [5, 4, 5])
plt.show()
```

```python
from matplotlib import pyplot # Importieren eines Teilbereichs
pyplot.plot([1, 2, 3], [5, 4, 5])
pyplot.show()
```

### Module in Ordnern

Ordner: hallom
hallom/__init__.py
    __all__ = ["datei"] # erlaubt den Import mit *
    from . import datei # erlaubt den Import des ganzen Moduls über den Namen
hallom/datei.py
    print("datei.py - Funktion f()")

```python
from hallom import datei
datei.f()
```

```python
from hallom import * # muss in der __init__.py erlaubt werden
datei.f()
```

```python
import hallom # muss in der __init__.py erlaubt werden
hallom.datei.f()
```

### Vorstellung Modul CSV

Dokumentation aller Standard-Module
[https://docs.python.org/3.6/py-modindex.html](https://docs.python.org/3.6/py-modindex.html)

- [CSV Modul Doku](https://docs.python.org/3.6/library/csv.html#module-csv)

```python
import csv
with open("datei.csv", newline="") as file:
    csv_file = csv_reader(file, delimiter=",")
    for line in csv_file:
        print(line)
```

## Python Version auslesen

```python
import sys
print(sys.version)
```

## Herausfinden, welche Methoden ein Objekt hat

```python
print(objekt.__dict__)
```

## Request Modul

...ist mit Anaconda bereits installiert
[https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)

Beispielseite ["http://python.beispiel.programmierenlernen.io/index.php"]("http://python.beispiel.programmierenlernen.io/index.php")

```python
import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
print(r.status_code)
print(r.headers)
print(r.text)
```

## Beatiful Soup Modul

...ist mit Anaconda bereits installiert
[https://www.crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/)

```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p>Ich bin ein Absatz</p>
        <p>Ich bin noch ein Absatz</p>
    </body>
</html>
"""

doc = BeautifulSoup(html, "html.parser")

for p in doc.find_all("p"):
    print(p)

for p in doc.find_all("p"):
    print(p.text)

```

```python
import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
from bs4 import BeautifulSoup
doc = BeautifulSoup(r.text, 'html.parser')
print(doc)

for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title = card.select(".card-title span")[1].text # h4 enthält zwei Spans, wir brauchen den zweiten
    image = card.select_one("img").attrs["src"]

    print(emoji)
    print(title)
    print(image)
    print(content)
```

```python
import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
from bs4 import BeautifulSoup
doc = BeautifulSoup(r.text, 'html.parser')

class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

articles = []

for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title = card.select(".card-title span")[1].text # h4 enthält zwei Spans, wir brauchen den zweiten
    image = card.select_one("img").attrs["src"]

    crawled = CrawledArticle(title, emoji, content, image)
    articles.append(crawled)

for article in articles:
    print(article.title)

```

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        r = requests.get(url)
        doc = BeautifulSoup(r.text, 'html.parser')

        articles = []

        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text # h4 enthält zwei Spans, wir brauchen den zweiten
            image = urljoin(url, card.select_one("img").attrs["src"]) # relativen Pfad des Bildes auf volle URL erweitern

            crawled = CrawledArticle(title, emoji, content, image)
            articles.append(crawled)
        return articles

fetcher = ArticleFetcher()
fetcher.fetch()

for article in articles:
    print(article.title)
```

## Exceptions

Ohne Exception Handling wird das Programm bei Eintreten einer Exception beendet

```python
try:
    print(5/0)
    print(4) # wird nicht mehr ausgeführt
except ZeroDivisionError:
    print("Durch null teilen ist nicht erlaubt!")
print(5) # Rest des Programms wird trotzdem noch ausgeführt
```

### eigene Exception

```python
class InvalidEmailError(Exception):
    pass # erweitert die Exception-Klasse, braucht aber keinen eigenen Code, außer den eigenen Namen

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("email does not contain an @")

try:
    send_mail("hallo", "Betreff", "Inhalt")
except InvalidEmaiLError:
    print("Bitte gebe eine gültige E-Mail ein")
```

```python
try:
    file=open("existiert.txt","r")
    print(File)
    print(5/0)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")
finally:
    file.close() # egal was passiert, am Ende wird auf jeden Fall die Datei geschlossen
```

## With Konstrukt

```python
# Wenn der Block verlassen wird (warum auch immer), wird die Datei geschlossen
with open("existiert.txt", "r") as file:
    print(file)
    print(5/0)
```

```python
# Auch hier analog - wenn der Block verlassen wird (hier mit return), wird die Datei geschlossen
def do_something():
    with open("existiert.txt", "r") as file:
        print(file)
        return "Hallo"

do_something()
```

## Das Set

Die Reihenfolge ist nicht bestimmt (bei einer Liste kommt das neue Element mit append immer an das Ende).
Ein Element kann nicht doppelt enthalten sein.

```python
s = {"Hallo", "Welt"}
s.add("Mars")
s.add("Mars")
print(s)

if "Mars" in s: # ist performancemäßig mit einem Set optimal
    print("Mars ist im Set")
```

```python
# Wie viele verschiedene Wörter sind im Text?
text="Hallo Welt Hallo Mars Hallo Welt"
words = set()
for word in text.split(" "):
    words.add(words) # doppelte Werte werden irgnoriert
    print(len(words))
```

## Die Queue

Eintrag vom Anfang wegnehmen, neue Einträge hinzufügen

```python
import queue
q = queue.Queue()

q.put("Hallo")
q.put("Welt")
q.put("Hallo")
q.put("Mars")
q.put("Hallo")
q.put("Pluto")

print(q)
print(q.get())
print(q.get())

while not q.empty():
    element=q.get()
    print(element)
```

## Die Priority Queue

```python
import queue
q = queue.PriorityQueue()

# ein Tupel mit Priorität, Wert wird erwartet
q.put((10,"Hallo Welt"))
q.put((15,"Mars"))
q.put((5,"Wichtig"))

print(q.get()) # 5, "Wichtig"
print(q.get()) # 10, "Hallo Welt"
```

## Optionale Parameter, benannte Parameter

```python
def multi_print(number=3, word="Hello")
    for i in range(0,number):
        print(word)

multi_print() # Alles Standard
multi_print(5) # number überschreiben
multi_print(word="Welt") # um führende Parameter nich neu beschreiben zu müssen, einfach den zu ändernden Parameter mit Namen zuweisen, alles andere bleibt Standard
```

## Kopie vs Referenz

Primitive Datentypen (Zahl, String, Boolean, Tupel) werden bei der Übergabe in eine Funktion kopiert.
Bei Datenstrukturen wird die Referenz auf das Objekt übergeben, eine Änderung des Objekts ist also auch außerhalb der Funktion sichtbar

```python
a=5

def f(a):
    a=3
    print(a)

f(a) # 3
print(a) # 5
```

```python
l=["Hallo", "Welt"]

def f(x): # Nur eine Kopie der Referenz, nicht der Liste
    x.append("!!!") # verändert die Liste auch außerhalb der Funktion
    print(x)

f(l) # ["Hallo", "Welt", "!!!"]
print(l) # ["Hallo", "Welt", "!!!"]
```

```python
l=["Hallo", "Welt"]

def f(x): # Nur eine Kopie der Referenz, nicht der Liste
    x=["Hallo", "Welt", "!!!"] # erzeugt eine neue Liste, Original bleibt unversehrt
    print(x)

f(l) # ["Hallo", "Welt", "!!!"]
print(l) # ["Hallo", "Welt"]

```

## Variable Funktionsparameter

```python
def f(a, b, c):
    print(a)
    print(b)
    print(c)

f(1,2,3) # 1 2 3

l= [1, 2, 3]
# ziemlich umständlich
f(l[0], l[1], l[2]) # 1 2 3

#besser
f(*l)  # zerlege die Liste und setze sie als Parameter ein
```

```python
#def calc_max(a, b, c, d, e, f, g, h, ....) wäre ziemlich umständlich

def calc_max(*params):
    print(params)

calc_max(1, 2, 3, 4, 5, 6, 7, 8) # gibt ein Tupel mit allen Werten aus
```

```python
def calc_max(current_max, *params): # ersten Wert als Parameter übernehmen, Rest in das Tupel packen
    print(current_max)
    print(params)
    for item in params:
        if item>current_max:
            current_max=item
    return current_max

calc_max(1,2,3)
```

```python
def f(**args): # erlaubt variable Parameter, die in Form eines Dictionaries übergeben werden
    print(args)

f(key="value", key2="Value")
```

```python
def g(key, param2):
    print(key)
    print(param2)

d = {"key": "Ich bin der Schlüssel", "param2": "Ich bin der Parameter"}

g(key=d["key"],param2=d["param2"]) # geht, aber ist umständlich
g(**d) # so kann direkt das Dictionary direkt übergeben werden
```

```python
%matplotlib inline
import matplotlib.pyplot as plt

def create_plot(**plot_params): # plt.plot unterstützt sehr viele Parameter, die wollen wir nicht alle explizit abfragen und 1:1 durchreichen. Stattdessen nehmen wir die Parameter als Dictionary entgegen und geben das Dictionary einfach an plt.plot weiter
    print(plot_params)
    plt.plot([1, 2, 3], [5, 6, 5], **plot_params)
    plt.show()

create_plot(color="r", linewidth=10, linestyle="dashed")
```

## Sortieren

```python
l = ["Max", "Monika", "Erik", "Franziska"]
l.sort() # aufsteigend
print(l)
l.sort(reverse = True) # absteigend
print(l)
```

```python
def get_length(item): # Eigene Funktion um Sortier-Parameter zu erstellen
    return len(item)

l = ["Max", "Monika", "Erik", "Franziska"]

l.sort(key = get_length) # ohne () übergeben. Funktion wird wie eine Variable übergeben
print(l)

# geht auch einfacher, da wir ja nur die len() Funktion nutzen, also
l.sort(key=len)
```

```python
# Dictionary hat keine sort-Methode, hier nutzen wir sorted()
d ={"Köln": "CGN", "Budapest": "BUD", "Saigon": "SGN"}
print(sorted(d))
print(sorted(d, reverse=True))

# sorted() sortiert nicht die Liste/Dictionary in place, sondern gibt ein neues, sortiertes Objekt zurück ohne das Original zu ändern
l = ["Max", "Monika", "Erik", "Franziska"]
l2 = sorted(l)
print(l)
print(l2)
```

### Lambda Funktion

```python
students = [
    ("Max", 3),
    ("Monika", 2),
    ("Erik", 3),
    ("Franziska", 1)
]

def students_key(student):
    return(student[1])

students.sort(key=students_key)
print(students)

# >> geht einfacher, wenn wir die Funktion direkt als Parameter definieren

students.sort(key= lambda student: student[1]) # lambda <eingabewert>: <ausgabe>
print(students)

# kann auch einer Variablen zugewiesen werden
f = lambda student: student[1]
f(("Max", 1))
# gibt 1 aus
```

## Reguläre Ausdrücke

[https://pythex.org](https://pythex.org)
[RegExr](https://regexr.com/)

```python
import re
sentence = "Ich habe 30 Hunde, die jeweils 4 Liter Wasser brauchen und 2 kg Nahrung."
sentence.find("") # kann ich nur nutzen, wenn ich genau weiß auf welche Zahl ich suchen will

re.findall("[0-9]+", sentence) # ["30", "4", "2"]
re.search("[0-9]+", sentence) # findet nur des erste Auftreten, zeigt aber genau wo es gefunden wurde
```

```python
re.search("der", "Hallo der Hallo") # suche "der" im String
re.search("der?", "Hallo der Hallo") # suche "der" oder "de" im String (r ist Optional)
re.search("der*", "Hallo derrrrrrrrr Hallo") # suche "der" oder "de" oder "derrrrrrr" im String (r ist Optional oder kann beliebig oft auftreten)
re.search("der+", "Hallo der Hallo") # suche "der" oder "derrrr" im String (r muss mindestens 1x da sein, kann sich aber beliebig oft wiederholen)

print(re.search(["1234567890"]), "Hallo 123 Hallo" )) # irgendwas aus dem String in [] muss da sein
print(re.search(["1234567890"]+), "Hallo 123 Hallo" )) # Ziffer muss mindestens einmal da sein, kann sich beliebig oft wiederholen
print(re.search(["0-9"]+), "Hallo 123 Hallo" )) # Ziffer muss mindestens einmal da sein, kann sich beliebig oft wiederholen
```

## Datumswerte

```python
from datetime imort datetime
now = datetime.now()
print(now)

day= datetime(2017,8,20,20,0,0) # Jahr, Monat, Tag, Stunde, Minute, Sekunde
print(day.year)
print(day.minute)

print(day.timestamp()) # Unix timestamp 1.1.1970, jede Sekunde eins erhöht
print(day.timestamp()-now.timestamp())
```

```python
from datetime import date, time
d = date(2017,8,20)
print(d)

t = time(20,1,4)
print(t)

print(date(2017,8,20) < date(2018,2,14))

# zerlegen von datetime
dt = datetime(2017, 8, 20, 20, 0, 0)
print(dt.time()) # 20:00:00
print(dt.date()) # 2017-08-20

# combinieren zu datetime
print(datetime.combine(d, t))
```

### formatierte Ausgabe

[https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-strptime-behavior](https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-strptime-behavior)

```python
from datetime import datetime

now = datetime.now()

print(now)
print(now.strftime("%d.%m.%Y"))
```

### formatierte Datumswerte einlesen

```python
d = "18.07.2017" # bspw. eingelesene Werte in CSV Datei...
dt = datetime.strptime(d, "%d.%m.%Y")
print(dt)
```

### Rechnen mit Datumswerten

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now + timedelta(days = 20, hours = 3, seconds = 1))

day = datetime(2017,8,20)
td = day - now # timedelta Objekt

print(td)
print(td.total_seconds())

```

### Lokale Datumswerte

```python
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "de_DE")
# kann auch "de_DE.UTF-8" oder "deu" oder "german" sein

now = datetime.now()

print(now.strftime("%A, %d. %B"))
# Sonntag, 24. September
```

## defaultdict

```python
from collections import defaultdict

d = {}

d["existiertNicht"] # wirft eine KeyError Exception

def generate():
    print("generate() wurde aufgerufen!")
    return 0

d = defaultdict(generate) # ohne () übergeben!

print(d["existiertNicht"]) # generate Funktion wird aufgerufen und für den Key der Wert 0 hinterlegt

p = defaultdict(int) # int() erzeugt eine 0
words = ["Hallo", "Hallo", "Welt"]
for word in words:
    p[word] = p[word] + 1 # beim ersten Mal automatisch mit 0 initialisiert

print(p) # "Hallo": 2, "Welt": 1
```

## Input

```python
print("Hallo Welt")

age = input("Alter eingeben")
print(age)
```

## Kommandozeilenergumente

```python
import sys
print(sys.argv) # gibt Liste aller Prameter (0 ist das Python Skript selbst) aus

if len(sys.argv) >= 2: # Mindestens ein weiterer Parameter nach dem Skriptnamen
    print("Der Parameter " + sys.argv[1] + " wurde übergeben")
else:
    print("Bitte einen Parameter angeben")
```

## Das Modul os

```python
import os
print(os.listdir(".")) # gibt mir alle Dateien im aktuellen Ordner aus
# das ist nicht zwingend der Ordner, wo das Python Skript liegt

print(__file__) # das ist der absolute Pfad zum aktuellen Python Skript
print(os.path.dirname(__file__)) # das ist der absolut Pfad zum Ordner, in dem das Skript liegt

with open(os.path.join(os.path.dirname(__file__), "datei.txt"), "r") as file:
    for line in file:
        print(line)

print(os.listdir(os.path.dirname(__file__))) # gibt mir alle Dateien im Ordner des Python Skrips aus
```

```python
import os

folder = os.path.join(os.path.dirname(__file__), "ordner")
print(os.listdir(folder)) # Zeigt alle Dateien und Ordner an - ohne Unterscheidung

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):
        print(file + " ist ein Ordner")
    else:
        print(file + " ist eine Datei")

```

```python
import os

maxcount=0

folder = os.path.join(os.path.dirname(__file__), "names")
print(os.listdir(folder))
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    print(file_path)
    if os.path.isdir(file_path):
        print(file + " ist ein Ordner")
    else:
        print("Ich durchsuche die Datei: " + file)
        with open(file_path, "r", encoding="utf-8") as quelle:
            for line in quelle:
                if line.split(" ")[0] == "Max":
                    maxcount+=1

print("Der Name Max wurde " + str(maxcount) + " mal als Vorname gefunden")
```

## Umlaute und Kodierungen

```python
import os

filename = os.path.join(os.path.dirname(__file__), "umlaute.txt")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(line)

filename_out = os.path.join(os.path.dirname(__file__), "umlaute_out.txt")

with open(filename_out, "w", encoding="utf-8") as file:
    file.write("Müller")
```

## Jupyther Widgets

[https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Complete-list](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Complete-list)

```python
import ipywidgets as widgets
from IPython.display import display
import csv

vorname = widgets.Text(description="Vorname:", value="")
display(vorname)

name = widgets.Text(description="Name:", value="")
display(name)

studienfach = widgets.RadioButtons(
    options=['Bitte auswählen', 'Mathe', 'Informatik', 'Philosophie', 'Kulturwissenschaften', 'Psychologie'],
    description='Studienfach:',
    disabled=False
)
display(studienfach)

button = widgets.Button(description="Student Eintragen")
display(button)

def save_entry(event):
    if vorname.value =="":
        print("Bitte einen Vornamen eingeben")

    elif name.value =="":
        print("Bitte einen Namen eingeben")

    elif studienfach.value =="Bitte auswählen":
        print("Bitte ein Fach wählen")

    else:
        with open("students.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([vorname.value, name.value, studienfach.value])
            print([vorname.value, name.value, studienfach.value])
        vorname.value=""
        name.value=""
        studienfach.value="Bitte auswählen"

button.on_click(save_entry)
```
c