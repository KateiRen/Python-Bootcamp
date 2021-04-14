# OpenCV

## Installation

```cmd
pip install opencv-python
```

## Basics

```python
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")
# in img steckt nun ein multi-dimensionales (numpy) Array jeden Bildpunkt des Bildes

print(img) # Zeigt das Array an
print(img.shape) # Zeigt Dimensionen in Zeilen, Spalten und Fabrkanälen

plt.imshow(img) # Einfachste Art die Grafik im Notebook inline anzuzeigen
plt.show() # Farbwerte stimmen noch nicht da OpenCV die Farbkanäle in umgekehrter Reihenfolge ablegt und erwartet (BGR)
```


```python
print(img[0][0]) # Farbkanäle des Pixels 0,0 ausgeben

# Statt Array-Transformation gibt es eine extra Funktion um die Farbkanäle umzusortieren
i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(i[0][0]) # Farbkanäle des Pixels 0,0 ausgeben

# Bild jetzt mit korrekter Farbdarstellung ausgeben
plt.imshow(i)
plt.show()
```

```python
# Farbdarstellung in Graustufen
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(g.shape) # das Bild-Array ist jetzt nur noch zweidimensional

plt.imshow(g, "gray")
plt.show()
```

```python
# um die große Anzahl an Zahlen für ein Bild effizient speichern und verarbeiten zu können, beschränken wir den Zahlenraum bewusst auf 1 Byte pro Farbkanal (überlassen also nicht Python die Auswahl wie die Zahlen gespeichert werden und ermöglichen beliebig große Zahlen auch speichern zu können)
r = np.array([1, 2, 3, 100], dtype="uint8")

# Eine Addition im beschränkten Zeichenraum (8 Bit) führt hier zum Überlauf
r = r + 250 
print(r) # [251 252 253  94]
```

```python
# für eine Addition ohne Überlauf bietet OpenCV eine eigene Additionsmethode um zwei Arrays zu addieren
# Der einfachste Weg um die Helligkeit zu erhöhen ist also ein zweites Array mit den gleichen Dimensionen anzulegen und dort schon einen Grauwert > 0 zu hinterlegen, der dann Pixel für Pixel zum Zielbild aufaddiert wird
z = np.zeros((1000, 1500, 3), dtype="uint8") + 50
increased = cv2.add(img, z)

i = cv2.cvtColor(increased, cv2.COLOR_BGR2RGB)
plt.imshow(i)
plt.show()
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

```python
```

```python
```
