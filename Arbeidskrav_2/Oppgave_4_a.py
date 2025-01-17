"""
Created on Thu Jan 16 20:39:48 2025

PY1010_Arbeidskrav_2_Oppgave_4_a
Programmet ber brukeren skrive inn navnet på et land og gir informasjon om hovedstaden og antall innbyggere i hovedstaden dersom landet finnes i databasen.

@author: s.honkanen
"""

# Oppretter dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

# Ber brukeren skrive inn et land
land = input("Skriv inn et land: ")

# Sjekker om landet finnes i dictionaryen og skriver ut informasjon
if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere:.3f} mill. innbyggere i {hovedstad}.")
else:
    print(f"Beklager, {land} finnes ikke i databasen.")
