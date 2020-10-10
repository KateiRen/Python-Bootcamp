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

## Typenumwandlung

str(variable)
int(variable)
float(variable)

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
'kann nachträglich nicht verändert werden (Immutable)

student = ("Max Müller", 22, "Informatik")

name = student[0]
age = student [1]
subject = student[2]
```

### Entpacken eines Tupels

alternativ zum beispiel davor

```python
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



```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

