# Eerst de te gebruiken libaries importeren
import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.max_columns', None)

df_bg = pd.read_csv(r'C:\Users\lisan\OneDrive\Documents\Python\Projecten\Board Games\bgg_topics.csv')

# print(df_bg.info())

# We willen weten hoe of de gemiddelde ratings van alle spellen in de afgelopen 30 jaar gestegen is
# Het resultaat van de groupby is een pands Series
jaar_analyse = df_bg.groupby('details.yearpublished')['stats.average'].mean().tail(30) 
print(jaar_analyse)
print(type(jaar_analyse))

# Hiervan willen we een lijngrafiek maken
# Stap 1: Maak de grafiek
plt.figure(figsize=(10,4))

# Stap 2: Het is een lijngrafiek
# jaar_analyse.index is hier details.yearpublished en jaar_analyse is hier stats.average
plt.plot(jaar_analyse.index, jaar_analyse, marker='o', color = 'maroon')

# Stap 3: Voeg een titel toe
plt.title('Overzicht van gemiddelde rating van bordspellen in 1989-2018', fontsize=16, fontweight='bold')

# Stap 4: Label de assen
plt.xlabel('Jaar', fontsize=12)
plt.ylabel('Rating', fontsize=12)

# Stap 5: Laat de grafiek zien
plt.tight_layout()
plt.show()