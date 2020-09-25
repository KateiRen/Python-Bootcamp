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
