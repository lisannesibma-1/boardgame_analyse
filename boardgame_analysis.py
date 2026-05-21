import pandas as pd

# Sla dit ergens bovenin je script op, net onder import pandas:
pd.set_option('display.max_columns', None)

df_bg = pd.read_csv(r'C:\Users\lisan\OneDrive\Documents\Python\Projecten\Board Games\bgg_topics.csv')

#print(df_bg.head())

#print(df_bg.info())

# Situatie: Ik wil een spel spelen met meer dan 4 mensen, en het moet met dobbelstenen zijn
# Onze favoriete designers zijn Uwe Rosenberg, Alan R. Moon en Reiner Knizia, dus de ontwerper moet 1 van die 3 zijn

# Eerst filteren op meer dan 4 mensen
filter_groep = df_bg[df_bg['details.maxplayers']>4]

# Dan op dat het met dobbelstenen moet zijn
filter_dice = filter_groep[filter_groep['attributes.boardgamecategory'].str.contains('Dice', na=False)]

# Dan op dat het van Uwe, Alan of Reiner moet zijn
favority_designer = ['Uwe Rosenberg', 'Alan R. Moon', 'Reiner Knizia']
filter_designer = filter_dice[filter_dice['attributes.boardgamedesigner'].isin(favority_designer)]

# Dan op dat het minstens 6.5 rating moet hebben
filter_stats = filter_designer[filter_designer['stats.average']>=6.5]

print(filter_stats[['details.name', 'details.maxplayers', 'attributes.boardgamedesigner', 'stats.average']])

# En nu een plot
import matplotlib.pyplot as plt

# Sorteer de 4 spellen zodat de hoogste score bovenaan staat
jouw_top_spellen = filter_stats.sort_values(by='stats.average', ascending=True)

# Maak de grafiek
plt.figure(figsize=(10, 4))

# We gebruiken barh (horizontal) in plaats van bar
plt.barh(jouw_top_spellen['details.name'], jouw_top_spellen['stats.average'], color='royalblue', edgecolor='black')

# Zet de lat op de X-as tussen de 0 en 10 (omdat BGG cijfers tot 10 geeft)
plt.xlim(6, 7)

# Voeg titels en labels toe
plt.title('De perfecte dobbelspellen voor onze spelavond (>4 spelers)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('BGG Rating', fontsize=12)

# Een raster helpt om de cijfers makkelijker af te lezen
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Laat de grafiek zien!
plt.tight_layout() # Zorgt dat de spelnamen er netjes opvallen
plt.show()