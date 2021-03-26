# Pandas

## Basics

```python
import pandas as pd

df = pd.read_csv("xyz.csv", delimiter=",")

df # gibt ganzes dataframe aus

df.head() # nur erste Zeilen ausgeben

len(df)

df["Name"] #gibt die Spalte Name zurück

df.iloc[0] # ganze Zeile an index location zurückgeben

entry = df.iloc[0]
print(entry["Name"])


df.iloc[4:8] # wie beim List Slicing (Positionen 4, 5, 6, 7)

```

## Über Datensatz iterieren

```python
for row in df.iterrows():
    print(row) 
    pos, d = row # row ist ein tupel aus zeile und daten
    break # für den Test nur erste Zeile ausgeben

for pos, d in df.iterrows(): # das Tupel können wir direkt im Aufruf zerlegen
    print(pos)
    print(d)

for pos, d in df.iterrows():
    print(d["Name"]) # je Zeile nur die Werte der Spalte "Name" ausgeben
    # hat den Typ pandas.core.series.Series
```

## Spalte ausgeben

```python
# in einer Schleife
for pos, d in df.iterrows():
    print(d["Name"])

# am Stück
df["Year"]
```

## nach Spalte filtern

```python
df["Year"] < 1990 # ergibt eine Liste mit False/True für jede Zeile

df[df["Year"] < 1990] # gib mir ein neues df mit allen Zeilen wo die Bedingung erfüllt ist und gibt es aus

df2 = df[df["Year"] < 1990] # in neuem df speichern...
df3 = df2[df2["Gender"] == "Male"] # mehrfaches Filtern am besten in mehreren Stufen...





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
