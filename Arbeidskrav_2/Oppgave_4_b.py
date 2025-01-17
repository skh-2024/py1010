"""
Created on Thu Jan 16 20:41:34 2025

PY1010_Arbeidskrav_2_oppgave_4_b
Programmet lar brukeren legge til informasjon om et nytt land som ikke finnes i databasen. Programmet oppdater deretter oversikten med den nye informasjonen og skriver ut hele oppdatert oversikt.

@author: s.honkanen
"""

# Oppretter dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }

# Ber brukeren skrive inn et nytt land 
nytt_land = input("Skriv inn et nytt land: ")

# Sjekker om landet finnes i databasen
if nytt_land not in data:
    hovedstad = input(f"Skriv inn hovedstaden i {nytt_land}: ")
    innbyggere = float(input(f"Skriv inn antall innbyggere i mill. i {hovedstad}: "))
    #Legger til informasjonen i databasen
    data[nytt_land] = (hovedstad, innbyggere)
    print("Databasen er oppdatert: ")
    print("\nOppdatert database:")
    for land, info in data.items():
        print(f"{land}: Hovedstad - {info[0]}, Innbyggere - {info[1]:.3f} mill.")
        
else:
    print(f"{nytt_land} finnes allerede i databasen.")
