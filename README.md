# 🎲 Board Game Analyse (BGG Data Analysis)

**boardgame_analysis.py**
Een Python data-analyse project dat helpt bij het kiezen van het perfecte bordspel voor een specifieke spelavond. Dit script laadt een grote dataset van BoardGameGeek (BGG) in, filtert de spellen op basis van strenge criteria van een vriendengroep, en visualiseert de beste opties.

## 🎯 Het Probleem & De Vragen
Het kiezen van een bordspel voor een groep kan lastig zijn. Dit script beantwoordt de volgende vraag: 
*"Welk dobbelspel is geschikt voor een groep van 5 of meer personen, gebruikt dobbelstenen als 'main feature', is ontworpen door één van onze favoriete topdesigners (zonder co-auteurs), met een solide beoordeling?"*

Het script filtert de dataset op:
1. **Spelersaantal:** Geschikt voor groepen groter dan 4 spelers (`maxplayers > 4`).
2. **Categorie:** Moet een dobbelspel zijn (de kolom bevat het woord `'Dice'`).
3. **Designers:** Exclusief ontworpen door favoriete designers (zoals *Reiner Knizia* of *Uwe Rosenberg*), zonder co-auteurs (`.isin()`).
4. **Kwaliteit:** Een minimale BoardGameGeek rating van `6.5`.

## 📊 Resultaat & Visualisatie
Na het toepassen van de filters bleven er exact 4 spellen over die aan alle strenge eisen voldoen. Om de keuze makkelijker te maken, genereert het script automatisch een horizontale staafdiagram via `matplotlib`. 

De X-as is specifiek ingezoomd op het bereik `(6, 7)` om de onderlinge kwaliteitsverschillen tussen de top-opties direct zichtbaar te maken. Het resultaat is te zien in 'Top 4 bordspellen voorwaarden.png'.

**boardgame_analysis2.py**
Een Python data-analyse project waarin wordt onderzocht hoe de waardering van bordspellen zich door de jaren heen heeft ontwikkeld. Maakt de bordspellenwereld een kwaliteitsspurt door, of worden we milder met cijfers uitdelen? 

## 🎯 Het Doel & De Vraag
Dit script beantwoordt de vraag: 
*"Stijgt de gemiddelde beoordeling van bordspellen naarmate de jaren verstrijken?"*

Met behulp van een dataset van BoardGameGeek (BGG) berekent het script het gemiddelde rapportcijfer van alle uitgebrachte spellen per jaar, over de periode 1989 tot en met 2018.

## 🧠 Toegepaste Python & Data Technieken
Dit project laat zien hoe je grote hoeveelheden data efficiënt kunt aggregeren (samenvatten) in Pandas:

* **Data Aggregatie (`.groupby()`):** Er is gebruikgemaakt van de *Split-Apply-Combine* strategie. De dataset is opgesplitst per uniek jaar (`details.yearpublished`), waarna per jaar het gemiddelde (`.mean()`) is berekend van de rating-kolom (`stats.average`).
* **Tijdreeks Visualisatie:** Met Matplotlib is een vloeiende lijngrafiek (`plt.plot`) gebouwd met datamarkers, waarbij de index (jaren) op de X-as staat en de gemiddelde rating op de Y-as.

## 📊 Resultaat
De resulterende grafiek laat een duidelijke, stijgende trend zien. Spellen uit de jaren '90 scoren gemiddeld aanzienlijk lager dan spellen uit de jaren '10. Dit duidt op zowel een professionalisering van de bordspelindustrie als een milde vorm van 'rating-inflatie' binnen de community. Het resultaat is te zien in 'Overzicht BGG ratings in 1989 - 2018'.

## 🛠️ Gebruikte Technieken & Libraries
In dit project zijn de fundamentele technieken van data-analyse in Python toegepast:
* **Pandas:** Voor het inladen van data via absolute paden, opschonen van data, string-matching (`.str.contains`) en exacte lijst-matching (`.isin`).
* **Matplotlib:** Voor het sorteren van data en het bouwen van een op-maat-gemaakte, visueel aantrekkelijke horizontale grafiek (`plt.barh`).
