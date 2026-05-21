import pandas as pd
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

# 2. Wczytanie pliku danych (upewnij się, że plik german.data jest w tym samym folderze)
df = pd.read_csv('german.data', sep=r'\s+', header=None, names=columns)

# 3. Przekodowanie zmiennej zależnej (1 -> 1: Dobry, 2 -> 0: Zły)
df['Target'] = df['Target'].map({1: 1, 2: 0})

# 4. Ustawienie stylu wykresów
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 11, 'axes.labelsize': 12, 'axes.titlesize': 14})

# 5. GENEROWANIE TABELI STATYSTYCZNEJ
continuous_vars = ['Wiek', 'Kwota_kredytu', 'Okres_kredytowania']
stats_table = df.groupby('Target')[continuous_vars].agg(['mean', 'median', 'std', 'min', 'max']).round(2)

print("\n=== TABELA WYNIKOWA DO RAPORTU ===")
print(stats_table)
print("==================================\n")

# 6. GENEROWANIE WYKRESÓW (BOXPLOTY)
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# Mapowanie etykiet Targetu dla czytelności na wykresie
df_plot = df.copy()
df_plot['Status kredytu'] = df_plot['Target'].map({1: 'Dobry (Spłacony)', 0: 'Zły (Niewypłacalny)'})

# Wykres 1: Wiek
sns.boxplot(data=df_plot, x='Status kredytu', y='Wiek', ax=axes[0], palette='Set2')
axes[0].set_title('Rozkład Wieku Kredytobiorców')
axes[0].set_xlabel('Status spłaty kredytu')
axes[0].set_ylabel('Wiek (lata)')

# Wykres 2: Kwota kredytu
sns.boxplot(data=df_plot, x='Status kredytu', y='Kwota_kredytu', ax=axes[1], palette='Set2')
axes[1].set_title('Rozkład Kwoty Kredytu')
axes[1].set_xlabel('Status spłaty kredytu')
axes[1].set_ylabel('Kwota kredytu (DM)')

# Wykres 3: Okres kredytowania
sns.boxplot(data=df_plot, x='Status kredytu', y='Okres_kredytowania', ax=axes[2], palette='Set2')
axes[2].set_title('Rozkład Okresu Kredytowania')
axes[2].set_xlabel('Status spłaty kredytu')
axes[2].set_ylabel('Okres kredytowania (miesiące)')

# Dodanie źródła na dole wykresu (wymóg formalny z wytycznych projektu)
plt.figtext(0.1, 0.01, "Źródło: Opracowanie własne na podstawie zbioru German Credit (UCI).", 
            fontsize=10, style='italic')

plt.tight_layout()

# Wyświetlenie okna z wykresami
plt.show()