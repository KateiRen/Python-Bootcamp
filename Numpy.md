# Numpy

## Basics

```python
import numpy as np

print(np.arrange(10)) # Array von 0 - 9

print(np.arrange(10)) + 3 # Array von 3 - 12

print(np.arrange(10)) * 3 # Array von 0 - 27

np.array([1, 2, 3, 4, 5]) # normales Array übergeben

np.array([1, 2, 3, 4, 5]) **2 # normales Array mit Berechnung übergeben...

np.array([1, 2, 3, 4, 5]).mean() # Mittelwert
# min / max / std

np.zeros(10) # Array aus Nullen

xs = np.arrange(10)
ys = xy **2 # neues Array, Berechnugn wird für jeden Einzelwert aufgeführt

```

## Filtern

```python
a = np.array([1, 2, 3, 4])
b = np.array([False, True, True, False])

a[b] # array([2, 3])

a >= 3 # array([False, False, True, True])

a[a >= 3] # Array a gefiltert nach allen Werten ab 3
```

## Reshape

```python
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

reshaped = a.reshape((2,4)) # Tupel übergeben

# array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(reshaped[0]) # [1 2 3 4]
print(reshaped[0]) # [5 6 7 8]

a.reshape((-1, 4)) # 4 Elemente je Ebene, Anzahl Ebenen je nach Anzahl der Elemente in a

a.reshape((4, -1)) # 4 Ebenen, Anzahl Elemente je Ebene je nach Anzahl der Elemente in a


b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(b.reshape(8)) # wieder in eine Dimension reduziert (weil es 8 Elemente sind) [1 2 3 4 5 6 7 8]

print(b.reshape(-1)) # wieder in eine Dimension reduziert, egal wie viele Elemente da sind


b.shape # (2, 4) --> 2 Ebenen, je 4 Elemente

```

## Behind the scenes

```python
import nympy as np

a  =np.array([1, 2, 3])
print(a * 2) # Warum geht das?!


class MyArray():
    def __init__(self, liste):
        self.liste = liste

a = MyArray([1, 2, 3])
b = a * 2 # Fehler

class MyArray():
    def __init__(self, liste):
        self.liste = liste
    def __mul__(self, other):
        return MyArray([element * other for element in self.liste])

b = a * 2 # [2, 4, 6]

```


```python
```


```python
```
