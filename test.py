prijzen = {
    'aardbei': 3,
    'vanille': 4,
    'chocolade': 5
}
aanbieding = prijzen['vanille'] * 0.8
aanbieding = "{:.2f}".format(aanbieding) # Converteer de float naar een string met 2 decimalen

reclame_tekst = f"vandaag in de aanbieding: vanille ijs, 1 liter - slechts € {aanbieding} "

# Vind de index van de eerste '0' na de komma
index_van_0 = reclame_tekst.find("0")

# Maak een slice van de string tot deze index
reclame_tekst2 = reclame_tekst[:index_van_0]

# Print de waarde van reclame_tekst2
print(reclame_tekst2)
