"""
Created on Thu Jan 16 20:43:12 2025

PY1010_Arbeidskrav_2_oppgave_4_del_a_og_b_i samme_program
Programmet ber brukeren skrive inn navnet på et land og gir informasjon om hovedstaden og innbyggertallet hvis landet finnes i databasen.
Dersom landet ikke finnes i databasen, kan brukeren legge til informasjon, og databasen oppdateres med den nye informasjonen før den vises i en oppdatert oversikt.

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

# Sjekker om landet finnes i databasen
if land in data:
    hovedstad, innbyggere = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere:.3f} mill. innbyggere i {hovedstad}.")
   

else:
    print(f"{land} finnes ikke i databasen.")
    hovedstad = input(f"Skriv inn hovedstaden i {land}: ")
    innbyggere = float(input(f"Skriv inn antall innbyggere i mill. i {hovedstad}: "))
    #Legger til informasjonen i databasen
    data[land] = [hovedstad, innbyggere]
    print("Databasen er oppdatert.")
    
    print("\nOppdatert database:")
    for land, info in data.items():
        print(f"{land}: Hovedstad - {info[0]}, Innbyggere - {info[1]:.3f} mill.")
