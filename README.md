# 🎲 Board Game Picker (BGG Data Analysis)

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

De X-as is specifiek ingezoomd op het bereik `(6, 7)` om de onderlinge kwaliteitsverschillen tussen de top-opties direct zichtbaar te maken:

## 🛠️ Gebruikte Technieken & Libraries
In dit project zijn de fundamentele technieken van data-analyse in Python toegepast:
* **Pandas:** Voor het inladen van data via absolute paden, opschonen van data, string-matching (`.str.contains`) en exacte lijst-matching (`.isin`).
* **Matplotlib:** Voor het sorteren van data en het bouwen van een op-maat-gemaakte, visueel aantrekkelijke horizontale grafiek (`plt.barh`).
