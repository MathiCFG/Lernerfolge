import pandas as pd
raw_data = pd.read_csv("pokemon_data.csv")
print(raw_data.head(10))

# Überschriften ausgeben
print(raw_data.columns)


# Spezielle Spalten ausgeben [Eine]
print(raw_data.Name)


# Spezielle Spalten ausgeben [Mehrere]
print(raw_data[["Name", "Type 1"]])


# Datensätze in einen Zahlen Interval einlesen (Ziwschen Zahl1 und Zahl2)
print(raw_data.iloc[0:5])


# Datensätze in einen Zahlen Interval einlesen, jedoch eine GEWISSE SPALTE (Zwischen Zahl1 und Zahl2, 1) <---- 1 Für Spalte Name
print(raw_data.iloc[0:2, 1])


# Ganze Tabelle einlesen, wo z.B der Typ des Pokemons feuer ist
print(raw_data.loc[raw_data["Type 1"] == "Fire"])

# Alphabetisch und Nummerisch sortieren von Datensätze nach Spalte
print(raw_data.sort_values(["Type 1", "HP"], ascending=False)) # <-- ascending=False (Z-A)  |||  ascending=True (A-Z)