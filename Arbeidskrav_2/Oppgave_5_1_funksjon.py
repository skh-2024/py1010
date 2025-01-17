"""
Created on Thu Jan 16 20:45:38 2025

PY1010_Oppgave_5
Programmet inneholder kun en funksjon, beregn_areal_og_omkrets, som kombinerer beregningene for areal og omkrets.

@author: s.honkanen
"""

import math

def beregn_areal_og_omkrets(a, b):
    """
    Beregner både arealet og den ytre omkretsen av en figur som består av en rettvinklet trekant og en halvsirkel.
    
        a: Grunnlinjen til trekanten og diameteren til halvsirkelen.
        b: Høyden til trekanten.
        
    Returnerer:
        tuple: Det totale arealet og den ytre omkretsen av figuren.
    """
    
    # Regner ut arealer
    areal_trekant = (a * b) / 2
    areal_halvsirkel = (math.pi * (a / 2)**2) / 2
    areal_total = areal_trekant + areal_halvsirkel

    # Regner ut omkretsen
    hypotenuse = math.sqrt(a**2 + b**2)
    omkrets_halvsirkel = math.pi * (a / 2)  # Omkretsen av halvsirkelen ekskl. diameteren
    omkrets_total = omkrets_halvsirkel + hypotenuse + b

    return areal_total, omkrets_total

# Tar inn lengden på grunnlinjen (a) og høyden (b) fra brukeren
a = float(input('Skriv inn lengden av grunnlinjen (a): '))
b = float(input('Skriv inn høyden til trekanten (b): '))

# Beregning av areal og omkrets
areal, omkrets = beregn_areal_og_omkrets(a, b)

# Skriver ut resultatet
print(f"Den ytre omkretsen av figuren er: {omkrets:.1f}.")
print(f"Arealet av figuren er: {areal:.1f}.")

