import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Definiowanie oficjalnych nazw kolumn (zgodnie ze specyfikacją UCI)
columns = [
    'Status_konta', 'Okres_kredytowania', 'Historia_kredytowa', 'Cel_kredytu',
    'Kwota_kredytu', 'Konto_oszczednosciowe', 'Staz_pracy', 'Rata_do_dochodu',
    'Stan_cywilny_plec', 'Gwaranci', 'Okres_zamieszkania', 'Majatek',
    'Wiek', 'Inne_zobowiazania', 'Mieszkanie', 'Liczba_kredytow',
    'Zawod', 'Liczba_osob_utrzymaniu', 'Telefon', 'Pracownik_zagraniczny', 'Target'
]

# 2. Wczytanie pliku (dane są rozdzielane spacjami)
df = pd.read_csv('german.data', sep=r'\s+', header=None, names=columns)

# 3. Przekodowanie zmiennej zależnej (1 -> 1: Dobry, 2 -> 0: Zły)
df['Target'] = df['Target'].map({1: 1, 2: 0})

# 4. Sprawdzenie podstawowych informacji o zbiorze
print(f"Wymiary zbioru danych: {df.shape}")
print(f"Liczba braków danych: {df.isnull().sum().sum()}")
print("\nRozkład zmiennej zależnej:")
print(df['Target'].value_counts(normalize=True))