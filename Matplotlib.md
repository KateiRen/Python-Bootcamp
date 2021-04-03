# Matplotlib

## Ofizielle Doku

[https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot)

## Basics

```python
# mit diesem Steuerzeichen legen wir fest, dass Grafiken direkt im Notebook angezeigt werden
# Alternativ notebook (interaktiv) oder tk (eigenes Fenster)
# dafür ggf. den Kernel erst neustarten
%matplotlib inline

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [5, 4, 3])
plt.show()
```

### Linienfarbe, -type, Marker und Legende

```python
# Farbe der Lini efestlegen
plt.plot([1, 2, 3], [4, 5, 4], color = "#ff00ff")
plt.show()
```

```python
# Linientyp ändern
plt.plot([1, 2, 3], [4, 5, 4], color="#f27126", linestyle="dashed")
plt.show()
```

```python
# Datenpunkte auf der Linie markieren
plt.plot([1, 2, 3], [4, 5, 4], color="#f27126", linestyle="dashed", marker="o")
plt.show()
```

```python
# Legende anzeigen
plt.plot([1, 2, 3], [4, 5, 4], color="#f27126", linestyle="dashed", marker="o", label="Umsatz")
plt.legend()
plt.show()

# Bei Daten aus Pandas wird der Name automatisch übernommen und muss nicht angegeben werden
import pandas as pd

df = pd.read_excel("daten.xlsx")

year = df["Jahr"]
sales = df["Umsatz"]

plt.plot(year, sales)
plt.legend()
plt.show()
```

### Diagrammtypen

```python
# Kreisdiagramm
plt.pie([1, 2, 3])
plt.show()
```

```python
# Tortendiagramm
plt.bar([1, 2, 4], [5, 6, 5])
plt.show
```

```python
# Punktediagramm
plt.scatter([1, 2, 4], [5, 6, 5])
plt.show()

plt.scatter([1, 2, 4], [5, 6, 5], color = "#ff0000", marker = "x")
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
